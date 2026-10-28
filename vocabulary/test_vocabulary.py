"""Offline validation fixtures; no personal data or third-party dependencies."""
import ast
import re
import copy
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent

def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

validator = load('vocabulary_check', HERE / 'check.py')
generator = load('vocabulary_generate', HERE / 'generate.py')
alignment = load('alignment', HERE.parent / 'standards/check_alignment.py')


class VocabularyTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name)
        shutil.copytree(HERE, self.root / 'vocabulary', ignore=shutil.ignore_patterns('__pycache__'))
        shutil.copytree(HERE.parent / 'standards', self.root / 'standards', ignore=shutil.ignore_patterns('__pycache__'))
        # The one authored width list the generator makes a Zod module of.
        (self.root / 'zod').mkdir()
        shutil.copy(HERE.parent / 'zod/media-widths.json', self.root / 'zod/media-widths.json')
        self.path = self.root / 'vocabulary/sourced-entities.json'
        self.data = json.loads(self.path.read_text(encoding='utf-8'))
        # The released version these tests start from, and the next one a proposal takes.
        self.released = self.data['version']
        major, minor, _ = (int(part) for part in self.released.split('.'))
        self.following = f'{major}.{minor + 1}.0'
        self.site_path = self.root / 'vocabulary/site-content.json'
        self.site = json.loads(self.site_path.read_text(encoding='utf-8'))
        self.site_released = self.site['version']

    def check(self):
        self.path.write_text(json.dumps(self.data), encoding='utf-8')
        return validator.check(self.root)

    def test_repository(self):
        self.assertEqual(self.check(), [])
        self.assertEqual(alignment.check(self.root), [])

    def test_duplicate(self):
        self.data['groups']['fact_types'].append(copy.deepcopy(self.data['groups']['fact_types'][0]))
        self.assertTrue(any('duplicate' in e for e in self.check()))

    def test_mapping_forms(self):
        for mapping in ({}, {'rico': 'hasBirthDate', 'ehri': 'Person'}, {'local': 'pc:missing'}, {'rico': None}, {'rico': 'hasBirthDate', 'extra': 'bad'}):
            with self.subTest(mapping=mapping):
                self.data['groups']['fact_types'][0]['mapping'] = mapping
                self.assertTrue(any('mapping form' in e for e in self.check()))

    def test_local_declaration_and_reason(self):
        entry = self.data['groups']['fact_types'][0]
        for mapping in ({'local': 'pc:missing', 'reason': 'A reason.'}, {'local': 'pc:missing', 'reason': 'Two\nlines'}):
            entry['mapping'] = mapping
            self.assertTrue(self.check())

    def test_unknown_replacement(self):
        self.data['groups']['fact_types'][0]['replaced_by'] = 'missing'
        self.assertTrue(any('replacement' in e for e in self.check()))

    def next_proposal(self):
        self.data.update(version=self.following, status='proposed', released_on=None)

    def test_valid_deprecation(self):
        self.next_proposal()
        self.data['groups']['fact_types'][0].update(deprecated_in=self.following, replaced_by='other')
        self.assertEqual(self.check(), [])

    def test_cross_group_deprecation(self):
        self.next_proposal()
        entry = self.data['groups']['fact_types'][0]
        entry.update(deprecated_in=self.following, replaced_by={
            'group': 'relationship_types', 'id': 'parent_of',
            'reason': 'Use a relation to the child as a person.'})
        self.assertEqual(self.check(), [])
        for replacement in [
                {'group': 'missing', 'id': 'parent_of', 'reason': 'A child person.'},
                {'group': 'relationship_types', 'id': 'missing', 'reason': 'A child person.'},
                {'group': 'relationship_types', 'id': 'parent_of'},
                {'group': 'relationship_types', 'id': 'parent_of', 'reason': ' '},
                {'group': [], 'id': 'parent_of', 'reason': 'A child person.'},
                {'group': 'relationship_types', 'id': 'parent_of', 'reason': 'A child person.', 'extra': 'bad'},
                None, []]:
            with self.subTest(replacement=replacement):
                entry['replaced_by'] = replacement
                self.assertTrue(any('replacement' in e for e in self.check()))

    def test_deprecation_requires_replacement(self):
        self.next_proposal()
        self.data['groups']['fact_types'][0]['deprecated_in'] = self.following
        self.assertTrue(any('deprecation requires replacement' in e for e in self.check()))

    def test_owner_batch_and_historical_mappings(self):
        groups = self.data['groups']
        parenthood = next(e for e in groups['fact_types'] if e['id'] == 'parenthood')
        self.assertEqual(parenthood['deprecated_in'], '1.2.0')
        self.assertEqual(parenthood['replaced_by']['group'], 'relationship_types')
        self.assertEqual(parenthood['replaced_by']['id'], 'parent_of')
        self.assertIn('child as a person', parenthood['replaced_by']['reason'])
        for version in ['1.0.0', '1.1.0']:
            old = json.loads((HERE / f'released/{version}.json').read_text())['groups']
            self.assertEqual(parenthood['mapping'], next(e for e in old['fact_types']
                                                       if e['id'] == 'parenthood')['mapping'])
            for entry in old['relationship_types']:
                if entry['id'] in {'grandparent_of', 'grandchild_of', 'great_grandparent_of', 'great_grandchild_of'}:
                    self.assertEqual(entry['mapping'], {'rico': 'hasFamilyAssociationWith', 'via': 'FamilyRelation'})

    def test_mapping_change_needs_a_new_version_but_is_allowed_in_it(self):
        entry = next(e for e in self.data['groups']['relationship_types'] if e['id'] == 'grandparent_of')
        entry['mapping'] = {'rico': 'hasFamilyAssociationWith', 'via': 'FamilyRelation'}
        self.assertTrue(any('snapshot must equal' in e for e in self.check()))
        self.next_proposal()
        self.assertEqual(self.check(), [])

    def test_released_part_checks_follow_the_terms_out_of_site_content(self):
        self.next_proposal()
        part = self.data['groups']['event_parts'][0]
        for field, value, error in [('applies_to', ['unknown'], 'released event kinds'),
                                    ('applies_to', ['birth', 'birth'], 'released event kinds'),
                                    ('rico_parent', 'rico:hasChild', 'participant parent'),
                                    ('range_class', 'rico:Family', 'needs a person')]:
            with self.subTest(field=field, value=value):
                original = part[field]
                part[field] = value
                self.assertTrue(any(error in e for e in self.check()))
                part[field] = original
        path = self.root / 'vocabulary/profile.ttl'
        path.write_text(path.read_text().replace('rdfs:domain rico:Event', 'rdfs:domain rico:Person'))
        self.assertTrue(any('part profile' in e for e in self.check()))

    def test_released_concept_classes_are_checked(self):
        self.next_proposal()
        for group, id in [('event_types', 'memorial'), ('name_kinds', 'supplied')]:
            entry = next(e for e in self.data['groups'][group] if e['id'] == id)
            entry['concept_class'] = 'owl:Class'
            self.assertTrue(any(f'{group}.{id}: incorrect concept class' in e for e in self.check()))

    def test_inverse_symmetry(self):
        self.data['groups']['relationship_types'][0]['inverse'] = 'child_of'
        self.assertTrue(any('inverse' in e for e in self.check()))

    def snapshot(self):
        folder = self.root / 'vocabulary/released'
        folder.mkdir(exist_ok=True)
        (folder / f'{self.released}.json').write_text(json.dumps(self.data), encoding='utf-8')

    def test_released_removal_and_rename(self):
        self.snapshot()
        self.data['groups']['fact_types'][0]['id'] = 'renamed_birth'
        self.assertTrue(any('released ids removed' in e for e in self.check()))

    def test_released_group_removal(self):
        self.snapshot()
        del self.data['groups']['gender']
        self.assertTrue(any('released ids removed' in e for e in self.check()))

    def test_released_addition_and_deprecation(self):
        self.snapshot()
        self.next_proposal()
        new = copy.deepcopy(self.data['groups']['fact_types'][0])
        new.update(id='new_birth', added_in=self.following)
        self.data['groups']['fact_types'].append(new)
        self.data['groups']['fact_types'][0].update(deprecated_in=self.following, replaced_by='new_birth')
        self.assertEqual(self.check(), [])

    def test_generator_snapshot_lifecycle(self):
        outputs = generator.generated(self.root)
        snapshot = self.root / f'vocabulary/released/{self.released}.json'
        self.assertEqual(json.loads(outputs[snapshot]), self.data)
        self.next_proposal()
        self.check()
        outputs = generator.generated(self.root)
        self.assertEqual({path for path in outputs if path.parent.name == 'released'},
                         {self.root / f'vocabulary/released/site-content-{self.site_released}.json'})

    def test_current_snapshot_must_match(self):
        self.data['groups']['fact_types'][0]['label'] = 'Changed label'
        self.assertTrue(any('snapshot must equal' in e for e in self.check()))

    def test_current_snapshot_required(self):
        (self.root / f'vocabulary/released/{self.released}.json').unlink()
        self.assertTrue(any('snapshot is missing' in e for e in self.check()))

    def test_kinship_crosswalk_direction_and_name(self):
        path = self.root / 'vocabulary/crosswalks/fan-out-fact-kinds.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        row = next(r for r in data['mappings'] if r['fact_kind'] == 'parent_name')
        self.assertEqual(row['target'], {'group': 'fact_types', 'id': 'kinship'})
        self.assertEqual(row['relationship_type'], 'child_of')
        row['relationship_type'] = 'parent_of'
        row['requires'].remove('related_name')
        path.write_text(json.dumps(data), encoding='utf-8')
        errors = self.check()
        self.assertTrue(any('kinship relationship direction' in e for e in errors))
        self.assertTrue(any('related_name' in e for e in errors))

    def test_teacher_direction(self):
        relationships = {e['id']: e for e in self.data['groups']['relationship_types']}
        self.assertEqual(relationships['teacher_of']['mapping'],
                         {'rico': 'hasOrHadStudent', 'via': 'TeachingRelation'})
        self.assertEqual(relationships['student_of']['mapping'],
                         {'rico': 'hasOrHadTeacher', 'via': 'TeachingRelation'})
        self.assertEqual(len(relationships), 20)

    def test_crosswalk_destination_and_privacy(self):
        path = self.root / 'vocabulary/crosswalks/fan-out-fact-kinds.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['mappings'][0]['target']['id'] = 'missing'
        next(r for r in data['mappings'] if r['fact_kind'] == 'giver_of_record')['publish'] = True
        path.write_text(json.dumps(data), encoding='utf-8')
        errors = self.check()
        self.assertTrue(any('unknown crosswalk' in e for e in errors))
        self.assertTrue(any('private' in e for e in errors))

    def test_nested_mapping_and_via_alignment(self):
        self.data['groups']['fact_types'][0]['mapping'] = {'rico': 'hasBirthDate', 'via': 'UnknownRelation'}
        self.check()
        self.assertTrue(any('UnknownRelation' in e for e in alignment.check(self.root)))
        self.data['groups']['fact_types'][0]['mapping']['via'] = 'hasBirthDate'
        self.check()
        self.assertTrue(any('Relation class' in e for e in alignment.check(self.root)))

    def test_production_profile_alignment(self):
        with (self.root / 'vocabulary/profile.ttl').open('a') as stream:
            stream.write('\npc:bad a rico:UnknownClass .\n')
        self.assertTrue(any('UnknownClass' in e for e in alignment.check(self.root)))

    def test_production_compatibility_values(self):
        root = HERE.parent
        groups = self.data['groups']
        def ids(group):
            return [e['id'] for e in groups[group]]
        def ts_enum(file, name):
            text = (root / file).read_text(encoding='utf-8')
            body = re.search(r'\b' + name + r' = z.enum\(\[(.*?)\]\)', text, re.S)[1]
            return re.findall(r"'([^']+)'", body)
        self.assertEqual(ids('holocaust_fate_types'), ts_enum('zod/shared.schema.ts', 'HolocaustFateSchema'))
        tree = ast.parse((root / 'pydantic/shared.py').read_text(encoding='utf-8'))
        fate = next(n for n in tree.body if isinstance(n, ast.Assign) and n.targets[0].id == 'HolocaustFate')
        self.assertEqual(ids('holocaust_fate_types'), list(ast.literal_eval(fate.value.slice)))
        self.assertNotIn('left_before', ids('fate_outcomes'))

    def test_generation_is_deterministic_and_current(self):
        first = generator.generated()
        self.assertEqual(first, generator.generated())
        for path, content in first.items():
            self.assertEqual(path.read_bytes(), content.encode('utf-8'))
            self.assertNotIn('\r', content)
        compile(first[HERE.parent / 'pydantic/sourced_entities_vocabulary.py'], '<generated>', 'exec')

    def site_check(self):
        self.site_path.write_text(json.dumps(self.site), encoding='utf-8')
        return validator.check(self.root)

    def site_proposal(self):
        self.site.update(version='1.1.0', status='proposed')
        self.site.pop('released_on', None)
        self.site.pop('approved_by', None)
        path = self.root / 'vocabulary/site-content.profile.ttl'
        path.write_text(path.read_text().replace(
            f'{self.site_released} released 2026-10-25', '1.1.0 proposed; unreleased'))

    def test_site_release_requires_snapshot_date_and_approval(self):
        snapshot = self.root / f'vocabulary/released/site-content-{self.site_released}.json'
        snapshot.unlink()
        self.assertTrue(any('site-content: current released snapshot is missing' in e for e in self.site_check()))
        for key, message in [('released_on', 'requires a date'), ('approved_by', 'requires approval')]:
            with self.subTest(key=key):
                original = self.site.pop(key)
                self.assertTrue(any(message in e for e in self.site_check()))
                self.site[key] = original

    def test_site_current_snapshot_must_match(self):
        self.site['groups']['subjects'][0]['label'] = 'Changed label'
        self.assertTrue(any('snapshot must equal' in e for e in self.site_check()))

    def test_site_released_ids_cannot_be_removed_or_renamed(self):
        for group in self.site['groups']:
            with self.subTest(group=group):
                self.site_proposal()
                original = self.site['groups'][group][0]['id']
                self.site['groups'][group][0]['id'] = 'renamed'
                self.assertTrue(any(f'released ids removed from {group}' in e for e in self.site_check()))
                self.site['groups'][group][0]['id'] = original

    def test_site_snapshot_history_is_independent(self):
        outputs = generator.generated(self.root)
        snapshot = self.root / f'vocabulary/released/site-content-{self.site_released}.json'
        self.assertEqual(json.loads(outputs[snapshot]), self.site)
        self.site_proposal()
        self.assertEqual(self.site_check(), [])
        outputs = generator.generated(self.root)
        self.assertEqual({path for path in outputs if path.parent.name == 'released'},
                         {self.root / f'vocabulary/released/{self.released}.json'})
        self.site['released_on'] = '2026-10-26'
        self.assertTrue(any('proposed vocabulary cannot have a release date' in e for e in self.site_check()))
        self.site.pop('released_on')
        (self.root / 'vocabulary/released/site-content-1.1.0.json').write_text(json.dumps(self.site))
        self.assertTrue(any('proposed vocabulary cannot have a release snapshot' in e for e in self.site_check()))

    def test_site_released_entry_cannot_remain_proposed(self):
        self.site['groups']['subjects'][0]['status'] = 'proposed'
        self.assertTrue(any('released entry cannot remain proposed' in e for e in self.site_check()))

    def test_site_release_names_approved_groups_and_keeps_titles_proposed(self):
        self.assertEqual(self.site['released_groups'], ['content_item_subtypes', 'subjects'])
        self.assertTrue(all(e['status'] == 'proposed' for e in self.site['groups']['title_types']))
        self.site['groups']['title_types'][0].pop('status')
        self.assertTrue(any('unapproved entry must remain proposed' in e for e in self.site_check()))
        for groups in [[], ['missing'], ['subjects', 'subjects'], [None], 'subjects']:
            with self.subTest(groups=groups):
                self.site['released_groups'] = groups
                self.assertTrue(any('release must name its approved concept groups' in e for e in self.site_check()))

    def test_site_compatible_versions_are_explicit(self):
        for versions in [['0.1.0', '0.1.0'], [self.site_released], [''], [None], '0.1.0']:
            with self.subTest(versions=versions):
                self.site['compatible_versions'] = versions
                self.assertTrue(any('compatible versions' in e for e in self.site_check()))

    def test_released_batch_cannot_be_proposed_again(self):
        path = self.root / 'vocabulary/site-content.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        for group, released_group in [('proposed_event_types', 'event_types'),
                                      ('proposed_name_kinds', 'name_kinds'), ('event_parts', 'event_parts')]:
            with self.subTest(group=group):
                data['groups'][group] = copy.deepcopy(self.data['groups'][released_group])
                path.write_text(json.dumps(data), encoding='utf-8')
                self.assertTrue(any('unexpected concept groups' in e for e in self.check()))
                del data['groups'][group]

    def test_owner_chosen_subtype_parent(self):
        path = self.root / 'vocabulary/site-content.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['groups']['content_item_subtypes'][0]['parent_type'] = 'article'
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertTrue(any('owner decision' in e for e in self.check()))

    def test_owner_parent_rule_comes_from_data(self):
        self.site_proposal()
        self.site_check()
        path = self.root / 'vocabulary/site-content.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        entry = next(e for e in data['groups']['content_item_subtypes'] if e['id'] == 'poem')
        entry['owner_fixed_parent'] = {'type': 'entertainment', 'on': '2026-10-22'}
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertTrue(any('owner decision' in e for e in self.check()))
        entry['parent_type'] = 'entertainment'
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertEqual(self.check(), [])

    def test_impresso_parents_come_from_data(self):
        self.site_proposal()
        self.site_check()
        path = self.root / 'vocabulary/site-content.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['impresso_types'].append('fictional_type')
        entry = next(e for e in data['groups']['content_item_subtypes'] if e['id'] == 'poem')
        entry['parent_type'] = 'fictional_type'
        # poem's parent is fixed by the owner, so the recorded decision moves with it.
        entry['owner_fixed_parent']['type'] = 'fictional_type'
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertEqual(self.check(), [])
        data['impresso_types'].remove('fictional_type')
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertTrue(any('exactly one' in e for e in self.check()))

    def test_impresso_types_are_unique(self):
        path = self.root / 'vocabulary/site-content.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['impresso_types'].append(data['impresso_types'][0])
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertTrue(any('unique identifiers' in e for e in self.check()))

    def test_subtype_needs_one_parent(self):
        path = self.root / 'vocabulary/site-content.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['groups']['content_item_subtypes'][0]['parent_type'] = ['ad', 'article']
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertTrue(any('exactly one' in e for e in self.check()))

    def test_title_type_is_a_declared_concept(self):
        path = self.root / 'vocabulary/site-content.profile.ttl'
        text = path.read_text(encoding='utf-8').replace('skos:Concept, rico:TitleType', 'owl:Class')
        path.write_text(text, encoding='utf-8')
        self.assertTrue(any('concept class' in e for e in self.check()))

    def test_proposed_profile_is_checked_for_alignment(self):
        with (self.root / 'vocabulary/site-content.profile.ttl').open('a') as stream:
            stream.write('\npc:bad a rico:UnknownClass .\n')
        self.assertTrue(any('site-content.profile.ttl' in e and 'UnknownClass' in e
                            for e in alignment.check(self.root)))

    def test_profile_must_match_release_status(self):
        path = self.root / 'vocabulary/site-content.profile.ttl'
        path.write_text(path.read_text().replace(
            f'{self.site_released} released 2026-10-25', f'{self.site_released} proposed; unreleased'))
        self.assertTrue(any('profile must match vocabulary version and release status' in e for e in self.check()))

    def test_proposed_bindings_need_declared_reasons(self):
        path = self.root / 'vocabulary/site-content.profile.ttl'
        text = path.read_text(encoding='utf-8')
        path.write_text('\n'.join(line for line in text.splitlines()
                                 if not line.startswith('pc:site_translation ')), encoding='utf-8')
        self.assertTrue(any('bindings.translation' in e for e in self.check()))
        self.assertTrue(any('site_translation' in e or 'bindings[' in e
                            for e in alignment.check(self.root)))

    def test_local_reason_is_not_a_copy_of_the_definition(self):
        path = self.root / 'vocabulary/site-content.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        entry = next(e for e in data['bindings'] if e['id'] == 'translation')
        entry['mapping']['reason'] = entry['definition']
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertTrue(any('not repeat the definition' in e for e in self.check()))


    # The LinkML form of the vocabulary (linkml/schema/vocabulary.yaml). These tests need the
    # standard library alone; linkml/tests/test_vocabulary.py reads the same file with PyYAML
    # and LinkML in the linkml step's locked environment.

    def linkml_groups(self):
        """Every group the LinkML module is made from: (file, group, entries), as the files hold them."""
        reading = json.loads((self.root / 'vocabulary/reading-status.json').read_text(encoding='utf-8'))
        site = json.loads(self.site_path.read_text(encoding='utf-8'))
        data = json.loads(self.path.read_text(encoding='utf-8'))
        return ([('sourced-entities', group, entries) for group, entries in data['groups'].items()]
                + [('site-content', 'impresso_types', [{'id': value} for value in site['impresso_types']])]
                + [('site-content', group, entries) for group, entries in site['groups'].items()]
                + [('reading-status', 'reading_status_value',
                    [{'id': key, **entry} for key, entry in reading.items() if key != 'reading_status'])])

    def test_linkml_enums_hold_every_group_and_every_id(self):
        schema = generator.linkml_vocabulary(self.root)
        groups = self.linkml_groups()
        self.assertEqual(list(schema['enums']), [generator.contract_name(group) for _, group, _ in groups])
        self.assertEqual(len(schema['enums']), 24)
        prefixes = {'rico': 'rico:', 'ehri': 'ehri:'}
        for source, group, entries in groups:
            enum = schema['enums'][generator.contract_name(group)]
            self.assertTrue(enum['description'].strip())
            self.assertEqual(list(enum['permissible_values']), [entry['id'] for entry in entries])
            for entry in entries:
                value = enum['permissible_values'][entry['id']]
                with self.subTest(source=source, group=group, id=entry['id']):
                    self.assertEqual(value['description'], entry.get('definition') or entry.get('label')
                                     or f"The Impresso type {entry['id']}.")
                    mapping = entry.get('mapping')
                    if mapping is None:
                        self.assertEqual(group, 'impresso_types')
                        self.assertNotIn('meaning', value)
                    elif 'local' in mapping:
                        self.assertEqual(value['meaning'], mapping['local'])
                        self.assertEqual(value['comments'], [mapping['reason']])
                    else:
                        prefix = next(p for p in prefixes if p in mapping)
                        self.assertEqual(value['meaning'], prefixes[prefix] + mapping[prefix])
                    if mapping and 'via' in mapping:
                        self.assertEqual(value['annotations'], {'via': 'rico:' + mapping['via']})
                    else:
                        self.assertNotIn('annotations', value)
                    self.assertEqual('deprecated' in value, 'deprecated_in' in entry)
                    self.assertEqual(value.get('status'), entry.get('status'))
        relationships = schema['enums']['RelationshipTypes']['permissible_values']
        self.assertEqual(relationships['teacher_of']['meaning'], 'rico:hasOrHadStudent')
        self.assertEqual(relationships['teacher_of']['annotations'], {'via': 'rico:TeachingRelation'})
        self.assertEqual(schema['enums']['LocationTypes']['permissible_values']['city']['meaning'], 'ehri:City')
        parenthood = schema['enums']['FactTypes']['permissible_values']['parenthood']
        self.assertTrue(parenthood['deprecated'].startswith('Deprecated in 1.2.0; replaced by parent_of'))
        self.assertEqual(schema['enums']['TitleTypes']['permissible_values']['printed']['status'], 'proposed')
        self.assertIn(self.released, schema['version'])
        self.assertIn(self.site_released, schema['version'])

    def test_linkml_enums_are_named_as_the_other_contracts_name_them(self):
        root = HERE.parent
        schema = generator.linkml_vocabulary(root)
        zod = ''.join((root / name).read_text(encoding='utf-8') for name in (
            'zod/sourced-entities.vocabulary.ts', 'zod/site-content.vocabulary.ts', 'zod/content-item.schema.ts'))
        python = ''.join((root / name).read_text(encoding='utf-8') for name in (
            'pydantic/sourced_entities_vocabulary.py', 'pydantic/site_content_vocabulary.py',
            'pydantic/content_item.py'))
        for name, enum in schema['enums'].items():
            with self.subTest(enum=name):
                body = re.search(r'export const ' + name + r'Schema = z\.enum\(\[(.*?)\]\)', zod, re.S)
                self.assertIsNotNone(body)
                self.assertEqual(re.findall(r"""['"]([^'"]+)['"]""", body[1]), list(enum['permissible_values']))
                literal = re.search(r'^' + name + r' = Literal\[(.*?)\]$', python, re.M)
                self.assertIsNotNone(literal)
                self.assertEqual(list(ast.literal_eval(f'({literal[1]},)')), list(enum['permissible_values']))

    def test_a_hand_edit_of_the_linkml_vocabulary_fails_the_check(self):
        for path, content in generator.generated(self.root).items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding='utf-8', newline='\n')
        self.assertEqual(generator.stale(self.root), [])
        self.assertIsNone(generator.main(['--check'], root=self.root))
        target = self.root / generator.LINKML_VOCABULARY
        text = target.read_text(encoding='utf-8')
        for edited in (text.replace('"rico:isChildOf"', '"rico:hasChild"', 1),  # another meaning
                       text.replace('\n', '\r\n'),  # the same text with Windows line ends
                       text.rstrip('\n')):  # one byte fewer
            with self.subTest(edit=edited[-40:]):
                self.assertNotEqual(edited, text)
                target.write_text(edited, encoding='utf-8', newline='')
                self.assertEqual(generator.stale(self.root), [target])
                with self.assertRaises(SystemExit) as stopped:
                    generator.main(['--check'], root=self.root)
                self.assertEqual(str(stopped.exception), 'stale generated vocabulary: linkml/schema/vocabulary.yaml')
        target.unlink()
        self.assertEqual(generator.stale(self.root), [target])

    def test_the_linkml_vocabulary_follows_the_json(self):
        self.next_proposal()
        self.data['groups']['gender'].append({
            'id': 'planted', 'label': 'Planted', 'definition': 'A value planted by this test.',
            'added_in': self.following, 'status': 'proposed',
            'mapping': {'rico': 'hasSibling', 'via': 'SiblingRelation'}})
        self.check()
        text = generator.generated(self.root)[self.root / generator.LINKML_VOCABULARY]
        self.assertIn('      planted:\n        title: "Planted"\n'
                      '        description: "A value planted by this test."\n'
                      '        meaning: "rico:hasSibling"\n        status: "proposed"\n'
                      '        annotations:\n          via: "rico:SiblingRelation"\n', text)
        self.assertIn(f'version: "sourced-entities {self.following}, site-content {self.site_released}"', text)

    def test_the_linkml_vocabulary_is_written_in_block_style_with_every_word_quoted(self):
        self.assertEqual(generator.yaml_key('birth'), 'birth')
        for word in ('on', 'Off', 'yes', 'NO', 'true', 'False', 'y', 'n', 'null', '~', '1.3.0', '0',
                     '2026-10-28', 'a key', '-', ''):
            with self.subTest(word=word):
                self.assertEqual(generator.yaml_key(word), json.dumps(word))
                self.assertEqual(generator.yaml_scalar(word), json.dumps(word))
        # YAML folds these line breaks into a space inside quotes, and refuses DEL: each is escaped.
        self.assertEqual(generator.yaml_scalar('a\u2028b\x85c\x7fd'), r'"a\u2028b\u0085c\u007fd"')
        self.assertEqual(generator.yaml_scalar('ייִדיש'), '"ייִדיש"')
        for value in (1.5, ['a'], {'a': 1}):
            with self.assertRaises(TypeError):
                generator.yaml_scalar(value)
        self.assertEqual(generator.to_yaml({'a': {'b': ['x', {'c': None}], 'd': {}, 'e': []}}).splitlines()[2:], [
            'a:', '  b:', '    - "x"', '    -', '      c: null', '  d: {}', '  e: []'])
        text = (HERE.parent / generator.LINKML_VOCABULARY).read_text(encoding='utf-8')
        self.assertNotRegex(text, r'[\[{](?![\]}])')  # no flow style but an empty {} or []

    def test_the_generator_stops_on_what_it_cannot_write(self):
        for mapping in ({'rico': 'hasSibling', 'ehri': 'Person'}, {'local': 'xx:term', 'reason': 'A reason.'},
                        {'rico': 'http://example.org/ns#hasSibling'}, {'rico': 'ehri:Person'}, {'ehri': ''},
                        {'via': 'SiblingRelation'}, {}):
            with self.subTest(mapping=mapping), self.assertRaises(SystemExit):
                generator.meaning(mapping, 'planted')
        self.assertEqual(generator.meaning(
            {'rico': 'https://www.ica.org/standards/RiC/ontology#hasSibling'}, 'planted'), 'rico:hasSibling')
        self.site['groups']['fact_types'] = self.site['groups'].pop('subjects')
        self.site_path.write_text(json.dumps(self.site), encoding='utf-8')
        with self.assertRaises(SystemExit) as stopped:
            generator.linkml_vocabulary(self.root)
        self.assertIn('FactTypes', str(stopped.exception))
        reading = self.root / 'vocabulary/reading-status.json'
        states = json.loads(reading.read_text(encoding='utf-8'))
        del states['reading_status']
        reading.write_text(json.dumps(states), encoding='utf-8')
        self.site_path.write_text(json.dumps(json.loads((HERE / 'site-content.json').read_text(encoding='utf-8'))),
                                  encoding='utf-8')
        with self.assertRaises(SystemExit) as stopped:
            generator.linkml_vocabulary(self.root)
        self.assertIn('reading_status', str(stopped.exception))


if __name__ == '__main__':
    unittest.main()
