"""Refresh payload bookkeeping only. Default/check mode is read-only; no hooks/network."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile

from check_library import ROOT, payload


class UpdateError(RuntimeError):
    def __init__(self, message, updated=()):
        super().__init__(message)
        self.updated = list(updated)


def plain_path(root, path):
    relative = path.relative_to(root)
    cursor = root
    for part in relative.parts:
        cursor = cursor / part
        if cursor.is_symlink():
            raise ValueError('Refusing symlink: ' + str(relative))
    return path


def records(root):
    files = payload(root)
    # Validate every path before reading any payload bytes.
    for path in files.values():
        plain_path(root, path)
    return {name: {'sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
                   'bytes': path.stat().st_size,
                   'executable': bool(path.stat().st_mode & 0o100)}
            for name, path in sorted(files.items())}


def plan(root):
    root = Path(root).resolve()
    names = ('verification.json', 'manifest.json', 'README.md')
    before = {name: plain_path(root, root / name).read_bytes() for name in names}
    manifest = json.loads(before['manifest.json'])
    verification = json.loads(before['verification.json'])
    baseline = json.loads(plain_path(root, root / 'snapshot-baseline.json').read_text())
    files = records(root)
    entries = manifest['skills']
    actual_skills = {name for name in files if Path(name).name == 'SKILL.md'}
    declared = [row['entrypoint'] for row in entries]
    if (set(declared) != actual_skills or len(declared) != len(set(declared))
            or len({row['id'] for row in entries}) != len(entries)):
        raise ValueError('Curate manifest skill identities before refresh; no identities or licenses are inferred')
    if baseline['snapshot_payload_commit'] != verification['original_installed_snapshot']['snapshot_payload_commit']:
        raise ValueError('Snapshot baseline identity mismatch')
    old_files = manifest['files']
    payload_changed = old_files != files
    order = [name for name in old_files if name in files] + sorted(files.keys() - old_files.keys())
    manifest['files'] = {name: {**old_files.get(name, {}), **files[name]} for name in order}
    manifest['standalone_count'] = sum(row['kind'] == 'standalone' for row in entries)
    manifest['owned_plugin_skill_count'] = sum(row['kind'] == 'owned-plugin' for row in entries)
    fingerprint = hashlib.sha256(json.dumps(files, sort_keys=True, separators=(',', ':')).encode()).hexdigest()
    current = verification['current_repository']
    identity_changed = payload_changed or current.get('payload_fingerprint', fingerprint) != fingerprint
    current['payload_fingerprint'] = fingerprint
    current['payload_files'] = len(files)
    old = baseline['files']
    current['additional_payload_files_since_snapshot'] = sorted(files.keys() - old.keys())
    current['removed_payload_files_since_snapshot'] = sorted(old.keys() - files.keys())
    current['modified_existing_payload_files_since_snapshot'] = sum(old[n] != files[n] for n in old.keys() & files.keys())
    if identity_changed:
        current['recorded_on'] = datetime.now(timezone.utc).date().isoformat()
        for field in ('local_installed_parity', 'cloud_parity'):
            current[field] = 'NOT VERIFIED for refreshed payload ' + fingerprint + '; historical records retain their original scope'
    readme = before['README.md'].decode()
    for pattern, value in [
        (r'(\| Current payload manifest \| \*\*)\d+( entries\*\*)', len(files)),
        (r'(\| Package maintenance \| \*\*)\d+( added files\*\*)', len(files.keys() - old.keys())),
    ]:
        readme, count = re.subn(pattern, lambda match: match[1] + str(value) + match[2], readme)
        if count != 1:
            raise ValueError('Expected one README payload-count table row per field')
    content = {'verification.json': (json.dumps(verification, ensure_ascii=False, indent=2)+'\n').encode(),
               'manifest.json': (json.dumps(manifest, ensure_ascii=False, indent=2)+'\n').encode(),
               'README.md': readme.encode()}
    return before, {name: content[name] for name in names if content[name] != before[name]}, fingerprint


def refresh(root, write=False):
    root = Path(root).resolve()
    before, changes, fingerprint = plan(root)
    updated, prepared = [], []
    try:
        if write:
            # Prepare everything before replacing anything. Verification goes first so a
            # partial write cannot leave stale current PASS pointers with a fresh manifest.
            for name, data in changes.items():
                target = plain_path(root, root / name)
                if target.read_bytes() != before[name]:
                    raise ValueError('Bookkeeping changed during refresh: ' + name)
                with tempfile.NamedTemporaryFile(dir=root, prefix='.library-refresh-', delete=False) as f:
                    temporary = Path(f.name)
                    prepared.append((name, temporary, target))
                    f.write(data)
                temporary.chmod(target.stat().st_mode & 0o777)
            if records(root) != json.loads(changes.get('manifest.json', before['manifest.json']))['files']:
                raise ValueError('Payload changed during refresh; no files replaced')
            for name, temporary, target in prepared:
                if target.read_bytes() != before[name]:
                    raise ValueError('Bookkeeping changed during refresh: ' + name)
                os.replace(temporary, target)
                updated.append(name)
    except (OSError, ValueError) as error:
        raise UpdateError(str(error), updated) from error
    finally:
        for _, temporary, _ in prepared:
            temporary.unlink(missing_ok=True)
    return {'status': 'UPDATED' if write and changes else ('STALE' if changes else 'CURRENT'),
            'scope': 'payload bookkeeping only; no tests or installation checks performed',
            'changed': list(changes), 'updated': updated, 'payload_fingerprint': fingerprint}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--check', action='store_true')
    mode.add_argument('--write', action='store_true')
    args = parser.parse_args(argv)
    try:
        result = refresh(ROOT, write=args.write)
    except (OSError, ValueError, KeyError, UpdateError) as error:
        print(json.dumps({'status': 'ERROR', 'error': str(error), 'updated': getattr(error, 'updated', [])}))
        return 2
    print(json.dumps(result))
    return 1 if result['status'] == 'STALE' else 0


if __name__ == '__main__':
    raise SystemExit(main())
