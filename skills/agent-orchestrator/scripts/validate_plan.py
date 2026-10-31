"""Validate declared file ownership and dependencies without executing tasks."""
from __future__ import annotations

import argparse
import json
from pathlib import Path, PurePosixPath


def validate_plan(plan):
    errors = []
    if not isinstance(plan, dict) or not isinstance(plan.get('tasks'), list) or not plan['tasks']:
        return ['tasks must be a nonempty list']
    tasks = {}
    for index, task in enumerate(plan['tasks']):
        if not isinstance(task, dict):
            errors.append(f'task {index}: expected an object')
            continue
        ident = task.get('id')
        if not isinstance(ident, str) or not ident.strip() or ident != ident.strip():
            errors.append(f'task {index}: id must be a nonempty trimmed string')
            continue
        if ident in tasks:
            errors.append(f'duplicate id: {ident}')
            continue
        tasks[ident] = task
        if not isinstance(task.get('acceptance'), str) or not task['acceptance'].strip():
            errors.append(f'{ident}: acceptance must be nonempty text')
        for field in ('depends_on', 'reads', 'writes'):
            values = task.get(field, [])
            if not isinstance(values, list) or any(not isinstance(v, str) or not v for v in values):
                errors.append(f'{ident}: {field} must be a list of nonempty strings')
                continue
            if len(set(values)) != len(values):
                errors.append(f'{ident}: duplicate {field} entry')
            if field == 'depends_on':
                continue
            for value in values:
                path = PurePosixPath(value)
                if (path.is_absolute() or '..' in path.parts or '\\' in value
                        or any(c in value for c in ('*', '?', '[', '\x00'))
                        or value.startswith('~') or ':' in value
                        or path.as_posix() != value):
                    errors.append(f'{ident}: {field} path must be normalized and workspace-relative: {value!r}')
    if errors:
        return errors
    for ident, task in tasks.items():
        for dep in task.get('depends_on', []):
            if dep not in tasks:
                errors.append(f'{ident}: unknown dependency {dep}')
    if errors:
        return errors

    ancestors = {}
    pending = set(tasks)
    while pending:
        ready = sorted(ident for ident in pending if all(d in ancestors for d in tasks[ident].get('depends_on', [])))
        if not ready:
            return ['dependency cycle involving: '+', '.join(sorted(pending))]
        for ident in ready:
            deps = tasks[ident].get('depends_on', [])
            ancestors[ident] = set(deps)
            for dep in deps:
                ancestors[ident].update(ancestors[dep])
            pending.remove(ident)

    def overlaps(a, b):
        x, y = PurePosixPath(a), PurePosixPath(b)
        return x == y or x in y.parents or y in x.parents

    ids = sorted(tasks)
    for index, left in enumerate(ids):
        for right in ids[index+1:]:
            if left in ancestors[right] or right in ancestors[left]:
                continue
            a, b = tasks[left], tasks[right]
            accesses = [(w, p) for w in a.get('writes', []) for p in b.get('reads', [])+b.get('writes', [])]
            accesses += [(p, w) for p in a.get('reads', []) for w in b.get('writes', [])]
            for x, y in accesses:
                if overlaps(x, y):
                    errors.append(f'unordered resource conflict: {left} {x!r} / {right} {y!r}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plan', type=Path)
    args = parser.parse_args()
    try:
        errors = validate_plan(json.loads(args.plan.read_text(encoding='utf-8')))
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    print(json.dumps({'valid': not errors, 'errors': errors, 'scope': 'declared file paths and dependency graph only'}, ensure_ascii=False))
    return 2 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
