"""A platform limitation is a skip; unrelated filesystem failures stay errors."""
import errno
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'skills/production-engineering/scripts/tests'))
import test_temp_path_regression as fixtures

class SymlinkSkipReporting(unittest.TestCase):
    def run_fixture(self, error):
        case = fixtures.LinkedTemporaryParentRegression('test_adapter_fixture_resolves_linked_parent_before_admission')
        result = unittest.TestResult()
        with patch.object(Path, 'symlink_to', side_effect=error):
            case.run(result)
        return result

    def test_permission_limit_is_visible_skip(self):
        result = self.run_fixture(PermissionError(errno.EPERM, 'symlinks denied by test fixture'))
        self.assertEqual(len(result.skipped), 1)
        self.assertIn('Symlink creation unavailable', result.skipped[0][1])
        self.assertFalse(result.errors)
        self.assertFalse(result.failures)

    def test_unrelated_io_failure_is_not_hidden_as_skip(self):
        result = self.run_fixture(OSError(errno.EIO, 'simulated I/O failure'))
        self.assertEqual(len(result.errors), 1)
        self.assertFalse(result.skipped)
