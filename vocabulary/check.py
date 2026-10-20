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
