"""What the linkml step's tests share: the folders, the modules under test and the Zod shapes.

The tests run in the linkml step's locked environment (bin/verify linkml), from the checkout's
root, with `python -I -m unittest discover -s linkml/tests`.
"""

import atexit
import functools
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

TESTS = Path(__file__).resolve().parent
LINKML = TESTS.parent
ROOT = LINKML.parent
FIXTURES = TESTS / 'fixtures'
LINT_CONFIG = LINKML / 'linkml-lint.yaml'


def load(name):
    """Import linkml/<name>.py under a name of its own (the folder is not a package)."""
    spec = importlib.util.spec_from_file_location(f'linkml_step_{name}', LINKML / f'{name}.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def linkml_lint(path, config=LINT_CONFIG):
    """Run `linkml lint` (the module behind it) on one file; return its exit status and output."""
    command = [sys.executable, '-I', '-m', 'linkml.linter.cli']
    if config is not None:
        command += ['--config', str(config)]
    result = subprocess.run([*command, str(path)], capture_output=True, text=True, cwd=ROOT)
    return result.returncode, result.stdout + result.stderr


@functools.cache
def zod_exports():
    """The JSON Schema of the five site documents, exported once a run from this checkout's Zod.

    Keys are the paths pruzhany-steps keeps them under (schemas/site/pages.schema.json, ...).
    """
    bun = shutil.which('bun')
    if bun is None:
        raise RuntimeError('bun is needed to export the Zod shapes; bin/verify installs it')
    folder = Path(tempfile.mkdtemp())
    atexit.register(shutil.rmtree, folder, True)
    subprocess.run([bun, str(LINKML / 'export_zod.ts'), str(folder)], cwd=ROOT, check=True)
    return {f'schemas/{path.relative_to(folder).as_posix()}': json.loads(path.read_text(encoding='utf-8'))
            for path in sorted(folder.rglob('*.schema.json'))}


def walk(node, pointer=''):
    """Yield (JSON Pointer, node) for every schema object under `node`, `node` first."""
    if not isinstance(node, dict):
        return
    yield pointer, node
    for key, value in node.items():
        if key in ('properties', '$defs', 'patternProperties') and isinstance(value, dict):
            for name, sub in value.items():
                escaped = name.replace('~', '~0').replace('/', '~1')
                yield from walk(sub, f'{pointer}/{key}/{escaped}')
        elif key in ('anyOf', 'oneOf', 'allOf', 'prefixItems') and isinstance(value, list):
            for index, sub in enumerate(value):
                yield from walk(sub, f'{pointer}/{key}/{index}')
        elif key in ('items', 'additionalProperties', 'propertyNames', 'not') and isinstance(value, dict):
            yield from walk(value, f'{pointer}/{key}')


def resolve(document, pointer):
    """The node a JSON Pointer names, or None when it names nothing."""
    node = document
    for part in pointer.split('/')[1:]:
        part = part.replace('~1', '/').replace('~0', '~')
        if isinstance(node, list) and part.isdigit() and int(part) < len(node):
            node = node[int(part)]
        elif isinstance(node, dict) and part in node:
            node = node[part]
        else:
            return None
    return node
