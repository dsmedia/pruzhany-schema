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
        self.path = self.root / 'vocabulary/sourced-entities.json'
        self.data = json.loads(self.path.read_text(encoding='utf-8'))
        # The released version these tests start from, and the next one a proposal takes.
        self.released = self.data['version']
        major, minor, _ = (int(part) for part in self.released.split('.'))
        self.following = f'{major}.{minor + 1}.0'

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
        self.assertFalse(any(path.parent.name == 'released'
                             for path in generator.generated(self.root)))

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
        for group, file, name in [
            ('holocaust_fate_types', 'zod/shared.schema.ts', 'HolocaustFateSchema'),
            ('holocaust_fate_types', 'zod/edition-bundle.schema.ts', 'HolocaustFateSchema'),
            ('location_types', 'zod/enrichment.schema.ts', 'LocationTypeSchema'),
            ('location_types', 'zod/edition-bundle.schema.ts', 'LocationTypeSchema'),
            ('compatibility_event_types', 'zod/enrichment.schema.ts', 'EventTypeSchema'),
            ('compatibility_event_types', 'zod/edition-bundle.schema.ts', 'EventTypeSchema'),
            ('content_unit_roles', 'zod/edition-bundle.schema.ts', 'ContentUnitRoleSchema'),
        ]:
            self.assertEqual(ids(group), ts_enum(file, name))
        tree = ast.parse((root / 'pydantic/project_output.py').read_text(encoding='utf-8'))
        aliases = {n.targets[0].id: ast.literal_eval(n.value.slice)
                   for n in tree.body if isinstance(n, ast.Assign)
                   and isinstance(n.value, ast.Subscript)
                   and isinstance(n.value.value, ast.Name) and n.value.value.id == 'Literal'}
        for group, alias in [('holocaust_fate_types', 'HolocaustFate'), ('location_types', 'LocationType'),
                             ('life_event_types', 'LifeEventType'), ('content_unit_roles', 'ContentUnitRole'),
                             ('gender', 'Gender'), ('compatibility_event_types', 'EnrichedEventType')]:
            self.assertEqual(ids(group), list(aliases[alias]))
        life = (root / 'zod/life-event.schema.ts').read_text(encoding='utf-8')
        self.assertEqual(ids('life_event_types'), re.findall(r"'([^']+)'", re.search(r'type: z.enum\(\[(.*?)\]\)', life, re.S)[1]))
        self.assertEqual(ids('content_unit_roles'), re.findall(r"'([^']+)'", re.search(r'role: z.enum\(\[(.*?)\]\)', life, re.S)[1]))
        self.assertNotIn('left_before', ids('fate_outcomes'))

    def test_generation_is_deterministic_and_current(self):
        first = generator.generated()
        self.assertEqual(first, generator.generated())
        for path, content in first.items():
            self.assertEqual(path.read_bytes(), content.encode('utf-8'))
            self.assertNotIn('\r', content)
        compile(first[HERE.parent / 'pydantic/sourced_entities_vocabulary.py'], '<generated>', 'exec')

    def test_site_vocabulary_stays_proposed(self):
        path = self.root / 'vocabulary/site-content.json'
        data = json.loads(path.read_text(encoding='utf-8'))
        data['released_on'] = '2026-10-22'
        path.write_text(json.dumps(data), encoding='utf-8')
        self.assertTrue(any('proposed' in e for e in self.check()))

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

    def test_proposed_profile_cannot_claim_release(self):
        path = self.root / 'vocabulary/site-content.profile.ttl'
        path.write_text(path.read_text().replace('proposed; unreleased', 'released'))
        self.assertTrue(any('profile must be marked proposed' in e for e in self.check()))

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


if __name__ == '__main__':
    unittest.main()
