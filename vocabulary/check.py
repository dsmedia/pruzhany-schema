"""Validate the vocabulary, crosswalk and released identifier history."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORMS = ({'rico'}, {'ehri'}, {'rico', 'via'}, {'local', 'reason'})
FAN_OUT = {'parent_name', 'spouse_name', 'sibling_name', 'child_name', 'giver_of_record',
           'birth_year_or_age', 'street_or_address', 'schooling_or_pupil', 'occupation', 'other'}


def check(root=ROOT):
    folder = root / 'vocabulary'
    vocabulary = json.loads((folder / 'sourced-entities.json').read_text(encoding='utf-8'))
    groups = vocabulary['groups']
    profile = (folder / 'profile.ttl').read_text(encoding='utf-8')
    errors = []
    if vocabulary.get('status') not in {'proposed', 'released'}:
        errors.append('invalid vocabulary status')
    if vocabulary.get('status') == 'proposed' and vocabulary.get('released_on') is not None:
        errors.append('proposed vocabulary cannot have a release date')
    if vocabulary.get('status') == 'released' and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', vocabulary.get('released_on') or ''):
        errors.append('released vocabulary requires a date')
    current_snapshot = folder / 'released' / (vocabulary['version'] + '.json')
    if vocabulary.get('status') == 'released':
        if not vocabulary.get('approved_by'):
            errors.append('released vocabulary requires approval metadata')
        if not current_snapshot.exists():
            errors.append('current released snapshot is missing')
        elif json.loads(current_snapshot.read_text(encoding='utf-8')) != vocabulary:
            errors.append('current released snapshot must equal current vocabulary')
    ids = {}
    for group, entries in groups.items():
        ids[group] = {entry['id'] for entry in entries}
        if len(ids[group]) != len(entries):
            errors.append(f'{group}: duplicate ids')
        if not entries:
            errors.append(f'{group}: empty group')
        for entry in entries:
            where = f'{group}.{entry["id"]}'
            for key in ('id', 'label', 'definition', 'added_in'):
                if not isinstance(entry.get(key), str) or not entry[key].strip():
                    errors.append(f'{where}: missing {key}')
            mapping = entry.get('mapping')
            if not isinstance(mapping, dict) or set(mapping) not in FORMS or not all(isinstance(v, str) and v.strip() for v in mapping.values()):
                errors.append(f'{where}: invalid mapping form')
                continue
            if 'local' in mapping:
                term, reason = mapping['local'], mapping['reason']
                if not re.fullmatch(r'pc:[A-Za-z_][\w-]*', term) or not re.search(re.escape(term) + r'\s+a\s+', profile):
                    errors.append(f'{where}: local term must be declared in profile.ttl')
                if len(reason.splitlines()) != 1:
                    errors.append(f'{where}: local reason must be one line')
                declaration = re.search(re.escape(term) + r'\s+a\s+.*?\.\s*(?:\n|$)', profile)
                if declaration and json.dumps(reason, ensure_ascii=False) not in declaration[0]:
                    errors.append(f'{where}: profile must document local reason')
            if 'replaced_by' in entry and entry['replaced_by'] not in ids[group]:
                errors.append(f'{where}: unknown replacement')
            if 'deprecated_in' in entry and 'replaced_by' not in entry:
                errors.append(f'{where}: deprecation requires replacement mapping')
    relationships = {e['id']: e for e in groups.get('relationship_types', [])}
    for id, entry in relationships.items():
        inverse = entry.get('inverse')
        if inverse not in relationships or relationships[inverse].get('inverse') != id:
            errors.append(f'{id}: inverse must exist and be symmetric')
    for snapshot in sorted((folder / 'released').glob('*.json')):
        previous = json.loads(snapshot.read_text(encoding='utf-8'))
        for group, entries in previous['groups'].items():
            missing = {e['id'] for e in entries} - ids.get(group, set())
            if missing:
                errors.append(f'{snapshot.name}: released ids removed from {group}: {sorted(missing)}')
    crosswalk = json.loads((folder / 'crosswalks/fan-out-fact-kinds.json').read_text(encoding='utf-8'))['mappings']
    kinds = [row['fact_kind'] for row in crosswalk]
    if set(kinds) != FAN_OUT or len(kinds) != len(FAN_OUT):
        errors.append('crosswalk must contain exactly the ten fan-out fact kinds')
    expected = {'parent_name': ('fact_types', 'kinship'), 'child_name': ('fact_types', 'kinship'),
                'spouse_name': ('fact_types', 'kinship'), 'sibling_name': ('fact_types', 'kinship'),
                'giver_of_record': ('citation_remark_kinds', 'private_source_remark'),
                'birth_year_or_age': ('fact_types', 'birth'), 'street_or_address': ('fact_types', 'residence'),
                'schooling_or_pupil': ('fact_types', 'education'), 'occupation': ('fact_types', 'occupation'),
                'other': ('fact_types', 'other')}
    for row in crosswalk:
        target = row['target']
        if target['id'] not in ids.get(target['group'], set()):
            errors.append(f'{row["fact_kind"]}: unknown crosswalk target')
        if (target['group'], target['id']) != expected.get(row['fact_kind']):
            errors.append(f'{row["fact_kind"]}: incorrect crosswalk destination')
        kinship_types = {'parent_name': 'child_of', 'spouse_name': 'spouse',
                         'sibling_name': 'sibling', 'child_name': 'parent_of'}
        if row['fact_kind'] in kinship_types:
            relationship_type = row.get('relationship_type')
            if relationship_type not in relationships or relationship_type != kinship_types[row['fact_kind']]:
                errors.append(f'{row["fact_kind"]}: incorrect kinship relationship direction')
            if row.get('direction') != 'subject_to_named_relative':
                errors.append('kinship crosswalk must state subject-to-relative direction')
            if not {'relationship_type', 'related_name'} <= set(row.get('requires', [])):
                errors.append('kinship crosswalk requires relationship_type and related_name')
        if row['fact_kind'] == 'giver_of_record' and row.get('publish') is not False:
            errors.append('giver_of_record must remain private')
        if row['fact_kind'] == 'birth_year_or_age' and row.get('inferred') is not True:
            errors.append('birth_year_or_age must be inferred')
        if row['fact_kind'] == 'other' and 'proposed_type' not in row.get('requires', []):
            errors.append('other requires proposed_type')
    errors.extend(check_site_content(root))
    return errors


def check_site_content(root=ROOT):
    folder = root / 'vocabulary'
    vocabulary = json.loads((folder / 'site-content.json').read_text(encoding='utf-8'))
    profile = (folder / 'site-content.profile.ttl').read_text(encoding='utf-8')
    errors = []
    if vocabulary.get('status') != 'proposed' or vocabulary.get('released_on') or vocabulary.get('approved_by'):
        errors.append('site-content: this vocabulary is proposed, not approved or released')
    if (folder / 'released' / ('site-content-' + vocabulary['version'] + '.json')).exists():
        errors.append('site-content: proposed vocabulary cannot have a release snapshot')
    if f'owl:versionInfo "{vocabulary["version"]} proposed; unreleased"' not in profile:
        errors.append('site-content: profile must be marked proposed and unreleased at this version')
    types = vocabulary['impresso_types']
    if (not isinstance(types, list) or not types
            or any(not isinstance(value, str) or not value.strip() for value in types)
            or len(set(types)) != len(types)):
        errors.append('site-content: Impresso types must be a nonempty list of unique identifiers')
        types = []

    def local_declaration(entry, where):
        term, reason = entry['mapping']['local'], entry['mapping']['reason']
        declaration = re.search(re.escape(term) + r'\s+a\s+.*?\.\s*(?:\n|$)', profile)
        if not re.fullmatch(r'pc:[A-Za-z_][\w-]*', term) or not declaration or json.dumps(reason, ensure_ascii=False) not in declaration[0]:
            errors.append(f'{where}: site-content.profile.ttl must declare local term and reason')
        if not reason.strip() or len(reason.splitlines()) != 1:
            errors.append(f'{where}: reason must be one line')
        if reason == entry.get('definition'):
            errors.append(f'{where}: local reason must explain the mapping, not repeat the definition')
        return declaration

    expected_classes = {'content_item_subtypes': 'rico:DocumentaryFormType',
                        'subjects': 'skos:Concept', 'title_types': 'rico:TitleType',
                        'proposed_event_types': 'rico:EventType', 'proposed_name_kinds': 'skos:Concept'}
    if set(vocabulary['groups']) != set(expected_classes) | {'event_parts'}:
        errors.append('site-content: unexpected concept groups')
    for group, entries in vocabulary['groups'].items():
        if not entries or len({e['id'] for e in entries}) != len(entries):
            errors.append(f'{group}: empty group or duplicate ids')
        for entry in entries:
            where = f'{group}.{entry["id"]}'
            for key in ('id', 'label', 'definition', 'added_in'):
                if not isinstance(entry.get(key), str) or not entry[key].strip():
                    errors.append(f'{where}: missing {key}')
            mapping = entry.get('mapping', {})
            if not isinstance(mapping, dict) or set(mapping) != {'local', 'reason'} or not all(isinstance(v, str) for v in mapping.values()):
                errors.append(f'{where}: concept needs a local identifier and reason')
                continue
            declaration = local_declaration(entry, where)
            cls = expected_classes.get(group)
            if group == 'event_parts':
                known_kinds = {e['id'] for e in vocabulary['groups']['proposed_event_types']} | {
                    e['id'] for e in json.loads((folder / 'sourced-entities.json').read_text())['groups']['event_types']}
                if (not entry.get('applies_to') or len(set(entry['applies_to'])) != len(entry['applies_to'])
                        or not set(entry['applies_to']) <= known_kinds):
                    errors.append(f'{where}: part must fit known event kinds')
                if entry.get('rico_parent') not in {'rico:affectsOrAffected', 'rico:hasOrHadParticipant'}:
                    errors.append(f'{where}: part needs a RiC-O participant parent')
                if entry.get('range_class') != 'rico:Person':
                    errors.append(f'{where}: main part needs a person')
                if not declaration or not all(term in declaration[0] for term in [
                        'owl:ObjectProperty', 'rdfs:domain rico:Event',
                        'rdfs:range rico:Person', 'rdfs:subPropertyOf ' + entry.get('rico_parent', '')]):
                    errors.append(f'{where}: part profile must declare its parent, domain and range')
            elif entry.get('concept_class') != cls or not declaration or cls not in declaration[0] or 'skos:Concept' not in declaration[0]:
                errors.append(f'{where}: incorrect concept class')
            if group in {'event_parts', 'proposed_event_types', 'proposed_name_kinds'} and entry.get('status') != 'proposed':
                errors.append(f'{where}: new term must remain proposed')
            if group == 'content_item_subtypes':
                parent = entry.get('parent_type')
                if not isinstance(parent, str) or parent not in types:
                    errors.append(f'{where}: subtype needs exactly one Impresso parent')
                if 'owner_fixed_parent' in entry:
                    decision = entry['owner_fixed_parent']
                    if (not isinstance(decision, dict) or set(decision) != {'type', 'on'}
                            or decision.get('type') not in types
                            or not isinstance(decision.get('on'), str)
                            or not re.fullmatch(r'\d{4}-\d{2}-\d{2}', decision['on'])):
                        errors.append(f'{where}: owner decision needs an Impresso type and date')
                    elif parent != decision['type']:
                        errors.append(f'{where}: parent differs from the owner decision')
    for entry in vocabulary['bindings']:
        where = f'bindings.{entry["id"]}'
        mapping = entry.get('mapping')
        if not isinstance(mapping, dict) or set(mapping) not in FORMS or not all(isinstance(v, str) and v.strip() for v in mapping.values()):
            errors.append(f'{where}: invalid mapping form')
        elif 'local' in mapping:
            local_declaration(entry, where)
    if {e['id'] for e in vocabulary['groups']['title_types']} != {'printed', 'supplied'}:
        errors.append('site-content: both title types are required')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    try:
        errors = check(args.root)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        raise SystemExit(f'vocabulary: invalid input: {exc}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print('vocabulary: entries, mappings, inverses, crosswalk and released ids pass')


if __name__ == '__main__':
    main()
