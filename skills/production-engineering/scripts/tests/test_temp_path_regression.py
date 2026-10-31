"""Reproduce macOS-style linked TMPDIR parents on any symlink-capable CI host."""
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import test_rea_adapter as adapter_fixtures
import test_rea_qualified as qualified_fixtures

class LinkedTemporaryParentRegression(unittest.TestCase):
    def exercise(self, module, fixture_type, method, verify):
        original_factory = tempfile.TemporaryDirectory
        with original_factory() as directory:
            base = Path(directory).resolve()
            physical = base / 'physical'
            physical.mkdir()
            linked = base / 'alias'
            try:
                linked.symlink_to(physical, target_is_directory=True)
            except OSError as error:
                import errno
                if error.errno in {errno.EPERM, errno.EACCES, errno.ENOSYS, errno.ENOTSUP} or getattr(error, 'winerror', None) == 1314:
                    self.skipTest('Symlink creation unavailable: ' + str(error))
                raise
            raw_paths = []
            def linked_factory(*args, **kwargs):
                temp = original_factory(*args, dir=str(linked), **kwargs)
                raw_paths.append(Path(temp.name))
                return temp
            fixture = fixture_type(methodName=method)
            try:
                with patch.object(module.tempfile, 'TemporaryDirectory', side_effect=linked_factory):
                    fixture.setUp()
                self.assertEqual(len(raw_paths), 1)
                self.assertIn(linked, raw_paths[0].parents)
                self.assertNotEqual(raw_paths[0], raw_paths[0].resolve())
                self.assertEqual(fixture.root, raw_paths[0].resolve())
                self.assertTrue(fixture.root.is_relative_to(physical))
                verify(fixture)
            finally:
                fixture.doCleanups()

    def test_adapter_fixture_resolves_linked_parent_before_admission(self):
        def verify(fixture):
            result = adapter_fixtures.rea.make_plan('inventory', str(fixture.target), advertised_commands={'inspect-artifact'})
            self.assertEqual(result['readiness'], 'REQUIRES_HOST_REVIEW')
        self.exercise(adapter_fixtures, adapter_fixtures.ReaAdapterTests,
                      'test_plan_never_claims_execution', verify)

    def test_runtime_fixture_resolves_linked_parent_before_verification(self):
        def verify(fixture):
            digest = fixture.write_manifest()
            # The actual verifier must accept the canonical fixture tree.
            qualified_fixtures.qualified.verify_tree(fixture.runtime, fixture.manifest, digest)
        self.exercise(qualified_fixtures, qualified_fixtures.QualifiedRuntimeTests,
                      'test_exact_fixture_matches', verify)

if __name__ == '__main__':
    unittest.main()
