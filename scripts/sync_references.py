"""Check declared bundled copies; write only with an explicit --write."""
import argparse
import json
from pathlib import Path
import tempfile

ROOT = Path(__file__).resolve().parents[1]

def safe(root, name):
    relative = Path(name)
    if relative.is_absolute() or '..' in relative.parts:
        raise ValueError('Reference path must stay inside the repository: ' + name)
    target = root / relative
    if not target.resolve().is_relative_to(root.resolve()) or any(p.is_symlink() for p in [target, *target.parents] if p != root.parent):
        raise ValueError('Linked or escaping reference path: ' + name)
    return target

def synchronize(root, write=False):
    root = Path(root).resolve()
    groups = json.loads((root / 'reference-groups.json').read_text())['groups']
    drift = []
    plan = []
    # Check every source/target before changing any copy.
    for group in groups:
        source = safe(root, group['source'])
        data = source.read_bytes()
        for name in group['copies']:
            target = safe(root, name)
            if not target.is_file() or target.read_bytes() != data:
                drift.append({'source': group['source'], 'copy': name})
                mode = (target if target.exists() else source).stat().st_mode & 0o777
                plan.append((name, target, data, mode))
    updated = []
    if write:
        for name, target, data, mode in plan:
            temporary = None
            try:
                target.parent.mkdir(parents=True, exist_ok=True)
                with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as f:
                    temporary = Path(f.name)
                    f.write(data)
                temporary.chmod(mode)
                temporary.replace(target)
                updated.append(name)
            except OSError as error:
                raise RuntimeError('Sync failed at ' + name + '; already updated: ' + repr(updated) + '; ' + str(error)) from error
            finally:
                if temporary is not None:
                    temporary.unlink(missing_ok=True)
    return drift

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--write', action='store_true')
    args = parser.parse_args(argv)
    try:
        drift = synchronize(ROOT, args.write)
    except (ValueError, OSError, KeyError, RuntimeError) as error:
        print(json.dumps({'status': 'ERROR', 'error': str(error)}))
        return 2
    print(json.dumps({'status': 'UPDATED' if args.write and drift else ('FAIL' if drift else 'PASS'), 'drift': drift}))
    return 0 if args.write or not drift else 1

if __name__ == '__main__':
    raise SystemExit(main())
