"""Offline integrity checks for the consolidated skill library; no installation."""
import hashlib
import json
from pathlib import Path
import re
from sync_references import synchronize

ROOT = Path(__file__).resolve().parents[1]
IGNORED = {'.git', '__pycache__', '.DS_Store', '.pytest_cache', '.mypy_cache', '.ruff_cache'}

def payload(root):
    return {str(p.relative_to(root)): p for folder in ['skills', 'plugins'] for p in (root / folder).rglob('*')
            if p.is_file() and not any(x in IGNORED for x in p.parts) and p.suffix not in {'.pyc', '.pyo'}}

def check_release_docs(folder, version):
    errors = []
    if ('## Current version: ' + version) not in (folder / 'README.md').read_text():
        errors.append('Current README version mismatch: ' + folder.name)
    changelog = folder / 'CHANGELOG.md'
    if not changelog.is_file() or not re.search(r'^## ' + re.escape(version) + r' —', changelog.read_text(), re.MULTILINE):
        errors.append('Current changelog entry missing: ' + folder.name)
    return errors

def check(root):
    root = Path(root)
    errors = []
    manifest = json.loads((root / 'manifest.json').read_text())
    actual = payload(root)
    expected = manifest['files']
    for name in sorted(actual.keys() ^ expected.keys()):
        errors.append('Manifest file-set mismatch: ' + name)
    for name in sorted(actual.keys() & expected.keys()):
        if hashlib.sha256(actual[name].read_bytes()).hexdigest() != expected[name]['sha256']:
            errors.append('Manifest SHA-256 mismatch: ' + name)
        if actual[name].stat().st_size != expected[name]['bytes']:
            errors.append('Manifest byte-size mismatch: ' + name)
        if bool(actual[name].stat().st_mode & 0o100) != expected[name]['executable']:
            errors.append('Manifest executable-mode mismatch: ' + name)
    entrypoints = {name for name in actual if Path(name).name == 'SKILL.md'}
    declared = {entry['entrypoint'] for entry in manifest['skills']}
    if declared != entrypoints or len(declared) != len(manifest['skills']):
        errors.append('Skill inventory differs from packaged entrypoints')
    for f in [root / 'README.md', root / 'ROUTING.md', *root.glob('skills/**/*.md'), *root.glob('plugins/**/*.md')]:
        for link in re.findall(r'\]\(([^)]+)\)', f.read_text()):
            if '://' in link or link.startswith(('#', 'mailto:', 'data:')):
                continue
            target = link.split('#', 1)[0]
            if target and not (f.parent / target).exists():
                errors.append('Missing local link: ' + str(f.relative_to(root)) + ' -> ' + link)
    for row in synchronize(root):
        errors.append('Shared reference drift: ' + row['copy'])
    for package in ['general-skills', 'product-intelligence']:
        folder = root / 'plugins' / package
        current = json.loads((folder / 'plugin.json').read_text())
        codex = json.loads((folder / '.codex-plugin/plugin.json').read_text())
        if current['version'] != codex['version']:
            errors.append('Plugin version mismatch: ' + package)
        errors.extend(check_release_docs(folder, current['version']))
        # Active pointers must use the new repository; historical evidence links stay untouched.
        for f in [folder / 'README.md', folder / 'plugin.json', folder / '.codex-plugin/plugin.json']:
            if 'ios3kov/production-engineering' in f.read_text():
                errors.append('Stale installation/provider pointer: ' + str(f.relative_to(root)))
    for f in [root / 'skills/production-engineering/README.md', root / 'skills/production-engineering/docs/GENERAL_SKILLS.md']:
        if re.search(r'(?:git clone https://github.com/|marketplace add )ios3kov/production-engineering', f.read_text()):
            errors.append('Stale standalone installation command: ' + str(f.relative_to(root)))
    verification = json.loads((root / 'verification.json').read_text())
    snapshot = verification['original_installed_snapshot']
    if not re.fullmatch(r'[0-9a-f]{40}', snapshot['snapshot_payload_commit']):
        errors.append('Invalid historical snapshot commit')
    current = verification['current_repository']
    if current['payload_files'] != len(expected):
        errors.append('Current verification payload count mismatch')
    for record in verification['repository_ci_evidence']['records']:
        if not re.fullmatch(r'[0-9a-f]{40}', record['tested_commit']):
            errors.append('Invalid CI tested commit')
        if record['run_url'] != 'https://github.com/ios3kov/codex-skills/actions/runs/' + str(record['run_id']):
            errors.append('CI run ID and URL mismatch')
    return errors

if __name__ == '__main__':
    try:
        problems = check(ROOT)
    except (OSError, ValueError, KeyError) as error:
        print(json.dumps({'status': 'ERROR', 'error': str(error)}))
        raise SystemExit(2)
    print(json.dumps({'status': 'FAIL' if problems else 'PASS', 'errors': problems}))
    raise SystemExit(1 if problems else 0)
