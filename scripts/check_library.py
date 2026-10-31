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
        # Active pointers must use the new repository; historical evidence links stay untouched.
        for f in [folder / 'README.md', folder / 'plugin.json', folder / '.codex-plugin/plugin.json']:
            if 'ios3kov/production-engineering' in f.read_text():
                errors.append('Stale installation/provider pointer: ' + str(f.relative_to(root)))
    general = root / 'plugins/general-skills'
    version = json.loads((general / 'plugin.json').read_text())['version']
    if ('## Current version: ' + version) not in (general / 'README.md').read_text():
        errors.append('Current General Skills README version mismatch')
    if ('## ' + version + ' —') not in (general / 'CHANGELOG.md').read_text():
        errors.append('Current General Skills changelog entry missing')
    for f in [root / 'skills/production-engineering/README.md', root / 'skills/production-engineering/docs/GENERAL_SKILLS.md']:
        if re.search(r'(?:git clone https://github.com/|marketplace add )ios3kov/production-engineering', f.read_text()):
            errors.append('Stale standalone installation command: ' + str(f.relative_to(root)))
    return errors

if __name__ == '__main__':
    try:
        problems = check(ROOT)
    except (OSError, ValueError, KeyError) as error:
        print(json.dumps({'status': 'ERROR', 'error': str(error)}))
        raise SystemExit(2)
    print(json.dumps({'status': 'FAIL' if problems else 'PASS', 'errors': problems}))
    raise SystemExit(1 if problems else 0)
