"""Exercise the actual Zod-exported JSON Schema, including closed people."""
import copy
import json
import sys
from jsonschema import Draft202012Validator
schema=json.load(open(sys.argv[1]))
fixtures=json.load(open(sys.argv[2]))
Draft202012Validator.check_schema(schema)
validator=Draft202012Validator(schema)
validator.validate(fixtures['full'])
validator.validate(fixtures['baseline'])
bad=copy.deepcopy(fixtures['full'])
bad['shared_record']['persons'][0]['unexpected']='must fail'
assert not validator.is_valid(bad)
print(f"entities: {len(fixtures['cases'])} shared cases, {len(fixtures['legacy'])} legacy mappings; exported SiteArchive JSON Schema accepts the current carrier and rejects unknown person fields")
