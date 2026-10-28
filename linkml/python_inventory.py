"""Find retained Python rules and prove that generated models still call them."""

import ast
import json
import re
from pathlib import Path

RETAINED = re.compile(r'^_(.+)__(.+)$')


def retained_checks(text):
    """The old Class.method identity follows a function when fields are generated."""
    for node in ast.parse(text).body:
        if isinstance(node, ast.FunctionDef) and (match := RETAINED.fullmatch(node.name)):
            args = node.args.args
            kind = 'field_validator' if args and args[0].arg == 'cls' else 'model_validator'
            yield '.'.join(match.groups()), kind


def binding_problems(root, profile=None):
    """Every function exists and is bound; no rule can silently disappear."""
    root = Path(root)
    profile = profile or json.loads((root / 'linkml/python-compatibility.json').read_text())
    problems = []
    called = set()
    functions = {}
    for name, cfg in profile['models'].items():
        hooks = [*cfg.get('validators', []), *cfg.get('field_validators', [])]
        hooks += [h for f in cfg.get('fields', {}).values() for h in f.get('type_hooks', [])]
        for hook in hooks:
            module, function = hook['module'], hook['function']
            if module not in functions:
                path = root / 'pydantic' / f'{module}.py'
                functions[module] = {n.name for n in ast.parse(path.read_text()).body if isinstance(n, ast.FunctionDef)}
            if function not in functions[module]:
                problems.append(f'{name}: Python callback {module}.{function} is missing')
            called.add((module, function))
    for path in (root / 'pydantic').glob('*.py'):
        for node in ast.parse(path.read_text()).body:
            if isinstance(node, ast.FunctionDef) and RETAINED.fullmatch(node.name) and (path.stem, node.name) not in called:
                problems.append(f'{path.stem}.{node.name}: retained rule has no generated binding')
    return problems
