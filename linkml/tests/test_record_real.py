"""The real shared record, from the site's checkout, against the generated JSON Schema.

The site keeps the shared record in 256 shards, pruzhany-svelte
static/data/private/shared-record/shard-00.json to shard-ff.json. Each shard has the record's
own shape: the version and vocabulary version, and every list of the record holding the rows
whose id falls in that shard (holders and media only where the record has them). The site's
reader (scripts/shared-record-shards.ts, readSharedRecordShards, read 28 October 2026) joins
them into one record, refusing a missing or extra shard, a shard with other keys or another
version, and an id met twice, and then validates the whole: references cross shards. This test
reads them the same way, validates the joined record with the validator the generated JSON
Schema names (Draft 2019-09), and validates each shard's own shape (its keys and stamps, with
its rows, which the joined record has already checked, left out).

It is skipped when the site's checkout is not found: $PRUZHANY_SVELTE, else a folder
pruzhany-svelte beside this checkout or one of its parents. Validating the joined record takes
about 80 seconds.
"""

import json
import os
import unittest
from pathlib import Path

from jsonschema import Draft201909Validator

from support import LINKML, ROOT

SCHEMA = json.loads((LINKML / 'generated' / 'json-schema' / 'shared_record.schema.json').read_text(encoding='utf-8'))
PARTS = ['persons', 'families', 'places', 'organizations', 'events', 'sources', 'facts', 'relations']
OPTIONAL_PARTS = ['holders', 'media']
HEADERS = ['version', 'vocabulary_version']
SHARDS = 256


def site_checkout():
    if os.environ.get('PRUZHANY_SVELTE'):
        return Path(os.environ['PRUZHANY_SVELTE'])
    return next((folder / 'pruzhany-svelte' for folder in ROOT.parents if (folder / 'pruzhany-svelte').is_dir()), None)


SITE = site_checkout()
FOLDER = SITE / 'static' / 'data' / 'private' / 'shared-record' if SITE else None


def read_shards(folder):
    """The shards as they are, after the site reader's checks of the files and their keys."""
    expected = [f'shard-{index:02x}.json' for index in range(SHARDS)]
    if sorted(path.name for path in folder.iterdir()) != expected:
        raise ValueError('missing or extra shared record shard')
    shards, present = [], None
    for name in expected:
        shard = json.loads((folder / name).read_text(encoding='utf-8'))
        these = PARTS + [part for part in OPTIONAL_PARTS if part in shard]
        if sorted(shard) != sorted(HEADERS + these) or (present is not None and these != present):
            raise ValueError(f'{name}: unexpected shared record fields')
        present = these
        shards.append(shard)
    return shards


def join(shards):
    """One record, as readSharedRecordShards assembles it: headers agree, ids are met once."""
    record = {part: [] for part in PARTS + [p for p in OPTIONAL_PARTS if p in shards[0]]}
    seen = set()
    for index, shard in enumerate(shards):
        for key in HEADERS:
            if index and shard[key] != record[key]:
                raise ValueError(f'shard {index:02x}: inconsistent {key}')
            record[key] = shard[key]
        for part in record.keys() - set(HEADERS):
            for row in shard[part]:
                if row['id'] in seen:
                    raise ValueError(f'duplicate id {row["id"]}')
                seen.add(row['id'])
                record[part].append(row)
    return record


@unittest.skipUnless(FOLDER and FOLDER.is_dir(), 'the site checkout is not found (set PRUZHANY_SVELTE to it)')
class TheRealSharedRecord(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.shards = read_shards(FOLDER)
        cls.record = join(cls.shards)
        cls.validator = Draft201909Validator(SCHEMA, format_checker=Draft201909Validator.FORMAT_CHECKER)

    def test_the_schema_names_the_validator_used(self):
        self.assertEqual(SCHEMA['$schema'], 'https://json-schema.org/draft/2019-09/schema')

    def test_the_joined_record_passes(self):
        self.assertGreater(len(self.record['facts']), 0)
        found = [f'{"/".join(map(str, error.absolute_path))}: {error.message[:200]}'
                 for error in self.validator.iter_errors(self.record)]
        self.assertEqual(found[:20], [], f'{len(found)} error(s) in the joined shared record')

    def test_each_shard_has_the_record_s_shape(self):
        for index, shard in enumerate(self.shards):
            with self.subTest(shard=f'{index:02x}'):
                outline = {key: (value if key in HEADERS else []) for key, value in shard.items()}
                self.assertTrue(self.validator.is_valid(outline))

    def test_a_planted_fault_in_a_real_row_is_refused(self):
        """Control: the validation can fail on this record."""
        fact = dict(self.record['facts'][0], type='kinship')
        fact.pop('relationship_type', None)
        planted = dict(self.record, facts=[fact], persons=[], relations=[], places=[], organizations=[])
        self.assertFalse(self.validator.is_valid(planted))
        outline = {key: (value if key in HEADERS else []) for key, value in self.shards[0].items()}
        self.assertFalse(self.validator.is_valid(dict(outline, vocabulary_version='0')))


if __name__ == '__main__':
    unittest.main()
