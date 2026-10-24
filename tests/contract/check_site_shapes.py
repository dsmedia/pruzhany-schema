"""The same fictional JSON is accepted/rejected and round-tripped by both twins."""
import copy
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def fixture_cases():
    for filename in ['site-shapes.fixtures.json', 'life-event-shapes.fixtures.json', 'sources-citations.fixtures.json']:
        yield from cases_from_file(filename)


def cases_from_file(filename):
    data = json.loads((ROOT / 'tests/contract' / filename).read_text(encoding='utf-8'))
    for case in data['cases']:
        value = data['example']
        for part in data['models'][case['model']]:
            value = value[part]
        value = copy.deepcopy(value)
        for change in case['changes']:
            target = value
            for part in change['path'][:-1]:
                target = target[part]
            if not change['path']:
                value = copy.deepcopy(change['value'])
            elif change.get('remove'):
                del target[change['path'][-1]]
            else:
                target[change['path'][-1]] = copy.deepcopy(change['value'])
        yield dict(name=case['name'], model=case['model'], valid=case['valid'], value=value,
                   error=case.get('error'))


def run_zod(cases):
    result = subprocess.run(['bun', str(ROOT / 'tests/contract/check_site_shapes.ts')],
                            input=json.dumps(cases, ensure_ascii=False), capture_output=True,
                            text=True, check=True, cwd=ROOT)
    return json.loads(result.stdout)


def check_site_shapes(package):
    cases = list(fixture_cases())
    zod = run_zod(cases)
    roundtrips = []
    errors = []
    for case, result in zip(cases, zod, strict=True):
        model = getattr(package, case['model'])
        try:
            parsed = model.model_validate_json(json.dumps(case['value']))
            accepted = True
        except ValueError as exc:
            accepted = False
            python_error = str(exc)
        if accepted != case['valid'] or result['valid'] != case['valid']:
            errors.append(f'{case["name"]}: expected {case["valid"]}, Pydantic={accepted}, Zod={result["valid"]}')
        if case.get('error') and (accepted or result['valid'] or
                                  case['error'] not in python_error or
                                  case['error'] not in result.get('error', '')):
            errors.append(f'{case["name"]}: both twins must refuse for {case["error"]!r}')
        if case['valid'] and accepted and result['valid']:
            try:
                from_zod = model.model_validate_json(json.dumps(result['value']))
            except ValueError as exc:
                errors.append(f'{case["name"]}: Zod output rejected by Pydantic: {exc}')
                continue
            if parsed.model_dump(mode='json') != from_zod.model_dump(mode='json'):
                errors.append(f'{case["name"]}: round trip changed data')
            # Existing page models have defaults their old Zod twins do not accept as
            # explicit null. Preserve omitted page fields; do not change that contract.
            roundtrips.append(dict(case, value=parsed.model_dump(
                mode='json', exclude_unset=case['model'] in {'SiteIssue', 'SiteArchive'})))
    for case, result in zip(roundtrips, run_zod(roundtrips), strict=True):
        if not result['valid']:
            errors.append(f'{case["name"]}: Pydantic output rejected by Zod')
    if errors:
        raise SystemExit('\n'.join(errors))
    basis = package.TextBasis.model_validate_json(json.dumps(dict(source_text='Original text', addresses=[dict(image_uri='fictional.png', bbox=[0, 0, 1, 1], text='Original text')])))
    assert package.text_basis_matches(basis, 'Original text')
    assert not package.text_basis_matches(basis, 'Changed text')
    rich = next(c for c in cases if c['name'] == 'all hand-written forms remain sourced and pending')
    record = package.SharedRecord.model_validate_json(json.dumps(rich['value']))
    prose = [f for f in record.facts if f.representation == 'prose']
    assert len(prose) == 3 and all(package.is_unreviewed_prose(f) for f in prose)
    later_naming = next(c for c in cases if c['name'] ==
                        'local 13: later naming on the same child id retains supplied description')
    child = package.SiteArchive.model_validate_json(json.dumps(later_naming['value'])).shared_record.persons[2]
    assert [n.value for n in child.names if package.is_printed_name(n)] == ['צעסקעלע']
    print(f'contract: {len(cases)} site-shape cases and {len(roundtrips)} round trips agree')
    advisory = json.loads((ROOT / 'tests/contract/citation-requirements.fixtures.json').read_text(encoding='utf-8'))['cases']
    zod_advisory = json.loads(subprocess.run(['bun', str(ROOT / 'tests/contract/check_citation_requirements.ts')],
        input=json.dumps(advisory), capture_output=True, text=True, check=True, cwd=ROOT).stdout)
    for case, actual in zip(advisory, zod_advisory, strict=True):
        citation = package.Citation.model_validate_json(json.dumps(case['citation']))
        source = package.Source.model_validate_json(json.dumps(case['source']))
        via = package.Source.model_validate_json(json.dumps(case['via'])) if case.get('via') else None
        python = package.statement_citation_shortfalls(citation, source, via)
        assert python == actual == case['shortfalls'], (case['name'], python, actual, case['shortfalls'])
    print(f'contract: {len(advisory)} advisory citation reports agree')
