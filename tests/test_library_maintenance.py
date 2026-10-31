"""Regression checks for missing/stale bundled references and path boundaries."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('sync_references', ROOT / 'scripts/sync_references.py')
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)

class BundledReferences(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        (self.root / 'owner.md').write_text('canonical reference\n')
        (self.root / 'copy.md').write_text('outdated reference\n')
        (self.root / 'reference-groups.json').write_text(json.dumps({'groups': [{'source': 'owner.md', 'copies': ['copy.md', 'nested/new.md']}]}))

    def test_check_reports_drift_without_modifying_files(self):
        result = sync.synchronize(self.root)
        self.assertEqual({x['copy'] for x in result}, {'copy.md', 'nested/new.md'})
        self.assertEqual((self.root / 'copy.md').read_text(), 'outdated reference\n')
        self.assertFalse((self.root / 'nested/new.md').exists())

    def test_explicit_sync_restores_self_contained_copies(self):
        (self.root / 'copy.md').chmod(0o644)
        sync.synchronize(self.root, write=True)
        self.assertEqual((self.root / 'copy.md').stat().st_mode & 0o777, 0o644)
        self.assertEqual(sync.synchronize(self.root), [])
        self.assertEqual((self.root / 'owner.md').read_bytes(), (self.root / 'nested/new.md').read_bytes())

    def test_outside_or_symlink_target_is_rejected(self):
        for name in ['../outside.md', str(self.root / 'absolute.md')]:
            with self.subTest(name=name), self.assertRaises(ValueError):
                sync.safe(self.root, name)
        (self.root / 'linked.md').symlink_to(self.root / 'owner.md')
        with self.assertRaises(ValueError):
            sync.safe(self.root, 'linked.md')

    def test_missing_owner_is_an_error_not_empty_success(self):
        (self.root / 'owner.md').unlink()
        with self.assertRaises(FileNotFoundError):
            sync.synchronize(self.root)

    def test_invalid_later_group_prevents_any_write(self):
        config = json.loads((self.root / 'reference-groups.json').read_text())
        config['groups'].append({'source': 'absent.md', 'copies': ['other.md']})
        (self.root / 'reference-groups.json').write_text(json.dumps(config))
        with self.assertRaises(FileNotFoundError):
            sync.synchronize(self.root, write=True)
        self.assertEqual((self.root / 'copy.md').read_text(), 'outdated reference\n')
