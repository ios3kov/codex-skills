"""Snapshot counters are checked against a frozen baseline without Git/network access."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_library import check_snapshot_delta

class SnapshotDelta(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        (self.root / 'snapshot-baseline.json').write_text(json.dumps({
            'snapshot_payload_commit': 'a' * 40,
            'files': {'skills/a/file': {'sha256': 'old'}, 'skills/a/unchanged': {'sha256': 'same'}}}))
        self.manifest = {'files': {'skills/a/file': {'sha256': 'new'}, 'skills/a/unchanged': {'sha256': 'same'}, 'skills/a/added': {'sha256': 'added'}}}
        self.verification = {'original_installed_snapshot': {'snapshot_payload_commit': 'a' * 40, 'payload_files': 2},
                             'current_repository': {'modified_existing_payload_files_since_snapshot': 1,
                                                    'additional_payload_files_since_snapshot': ['skills/a/added']}}

    def test_exact_delta_passes(self):
        self.assertEqual(check_snapshot_delta(self.root, self.manifest, self.verification), [])

    def test_stale_modified_count_fails(self):
        self.verification['current_repository']['modified_existing_payload_files_since_snapshot'] = 0
        self.assertIn('Modified snapshot payload count mismatch', check_snapshot_delta(self.root, self.manifest, self.verification))

    def test_added_and_removed_files_must_be_recorded(self):
        self.manifest['files'].pop('skills/a/added')
        self.manifest['files'].pop('skills/a/unchanged')
        errors = check_snapshot_delta(self.root, self.manifest, self.verification)
        self.assertTrue(any('additional_payload' in e for e in errors))
        self.assertTrue(any('removed_payload' in e for e in errors))
        self.verification['current_repository']['additional_payload_files_since_snapshot'] = []
        self.verification['current_repository']['removed_payload_files_since_snapshot'] = ['skills/a/unchanged']
        self.assertEqual(check_snapshot_delta(self.root, self.manifest, self.verification), [])

    def test_baseline_identity_must_match(self):
        self.verification['original_installed_snapshot']['snapshot_payload_commit'] = 'b' * 40
        self.assertIn('Snapshot baseline commit mismatch', check_snapshot_delta(self.root, self.manifest, self.verification))

    def test_baseline_count_must_match_original_record(self):
        self.verification['original_installed_snapshot']['payload_files'] = 3
        self.assertIn('Snapshot baseline file count mismatch', check_snapshot_delta(self.root, self.manifest, self.verification))
