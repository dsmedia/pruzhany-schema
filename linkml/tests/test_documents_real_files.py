"""Every real issue document and the catalog of pruzhany-svelte, against the generated JSON Schemas.

The site's static/data/ holds, for each of its issues, a pages, a content items, a mentions and a
life events document, and one editions catalog. Each is validated by the JSON Schema
linkml/generate.py made for it, with the validator its "$schema" names (draft 2019-09). Every
file must pass: the definition marks optional every key the files hold null in
(known-looser.yaml), and where it is stricter than the exports (a box of exactly four numbers, a
whole number where the exports say a number) the real files hold it too.

The site checkout is found at $PRUZHANY_SVELTE or /home/user/pruzhany-svelte; without one, the
test is skipped and says so. The comparison of verdicts both ways with the Zod exports is
pruzhany-steps' (record compare linkml, ticket 05).
"""

import json
import os
import unittest
from pathlib import Path

from test_documents import generated, refusals, validator

PATTERNS = {
    'pages': '*-pages.json',
    'content_items': '*-content-items.json',
    'mentions': '*-mentions.json',
    'life_events': '*-life-events.json',
    'editions': 'editions-catalog.json',
}


def site_data():
    for candidate in (os.environ.get('PRUZHANY_SVELTE'), '/home/user/pruzhany-svelte'):
        if candidate and (Path(candidate) / 'static' / 'data' / 'editions-catalog.json').is_file():
            return Path(candidate) / 'static' / 'data'
    return None


@unittest.skipIf(site_data() is None,
                 'the site checkout is not at hand: set PRUZHANY_SVELTE to a pruzhany-svelte checkout')
class RealFiles(unittest.TestCase):
    def test_every_real_document_is_accepted(self):
        counts = {}
        for module, pattern in PATTERNS.items():
            schema = generated(module)
            check = validator(schema)
            files = sorted(site_data().glob(pattern))
            refused = {}
            for path in files:
                document = json.loads(path.read_text(encoding='utf-8'))
                if not check.is_valid(document):
                    refused[path.name] = refusals(schema, document)[:3]
            counts[module] = (len(files), len(files) - len(refused), len(refused))
            with self.subTest(module=module):
                self.assertTrue(files, f'no {pattern} in {site_data()}')
                self.assertEqual(refused, {})
        issues = counts['pages'][0]
        self.assertTrue(all(counts[m][0] == issues for m in ('content_items', 'mentions', 'life_events')), counts)
        print(f'\nreal files (files, accepted, refused): {counts}')

    def test_a_real_file_with_a_planted_fault_is_refused(self):
        """Control: the same validation refuses the first real file of each kind once a key is wrong."""
        plants = {
            'pages': lambda d: d['pages'][0]['blocks'][0].update(bbox=[1, 2, 3]),
            'content_items': lambda d: d.update(vocabulary_version='9.9.9'),
            'mentions': lambda d: d['mentions'][0].update(roles=[]),
            'life_events': lambda d: d['life_events'][0].update(content_items=[]),
            'editions': lambda d: d['editions'][0].update(hebrewMonth=14),
        }
        for module, plant in plants.items():
            path = next(path for path in sorted(site_data().glob(PATTERNS[module]))
                        if module not in ('mentions', 'life_events')
                        or json.loads(path.read_text(encoding='utf-8'))[module])
            document = json.loads(path.read_text(encoding='utf-8'))
            plant(document)
            with self.subTest(module=module, file=path.name):
                self.assertNotEqual(refusals(generated(module), document), [])


if __name__ == '__main__':
    unittest.main()
