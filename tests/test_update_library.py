"""Observable bookkeeping behavior; refresh never invents executed evidence."""
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import update_library as updater

class RefreshLibrary(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        self.root = Path(temp.name).resolve()
        (self.root / 'skills/demo/references').mkdir(parents=True)
        (self.root / 'plugins').mkdir()
        self.skill = self.root / 'skills/demo/SKILL.md'
        self.skill.write_text('---\nname: demo\ndescription: demo\n---\nInstructions\n')
        (self.root / 'skills/demo/references/original.txt').write_text('original')
        files = updater.records(self.root)
        self.write('manifest.json', {'files': files, 'skills': [{'id':'demo','kind':'standalone','entrypoint':'skills/demo/SKILL.md'}], 'standalone_count':1, 'owned_plugin_skill_count':0})
        self.write('snapshot-baseline.json', {'snapshot_payload_commit':'a'*40,'files':files})
        self.write('verification.json', {'original_installed_snapshot':{'snapshot_payload_commit':'a'*40,'payload_files':2},
            'current_repository':{'payload_files':2,'additional_payload_files_since_snapshot':[],
                'modified_existing_payload_files_since_snapshot':0,'local_installed_parity':'PASS: old run','cloud_parity':'PASS: old run'},
            'history':{'tests':'PASS: recorded run','unperformed':'NOT RUN','note':'user-authored note'}})
        (self.root/'README.md').write_text('| Current payload manifest | **2 entries** |\n| Package maintenance | **0 added files** |\n')
        updater.refresh(self.root, write=True)

    def write(self, name, value):
        (self.root/name).write_text(json.dumps(value, indent=2)+'\n')

    def read(self, name):
        return json.loads((self.root/name).read_text())

    def outputs(self):
        return {name:(self.root/name).read_bytes() for name in ('manifest.json','verification.json','README.md')}

    def test_check_mode_detects_drift_without_writes(self):
        self.skill.write_text(self.skill.read_text().replace('description: demo','description: changed'))
        before = self.outputs()
        result = updater.refresh(self.root)
        self.assertEqual(result['status'], 'STALE')
        self.assertEqual(result['updated'], [])
        self.assertEqual(self.outputs(), before)

    def test_write_handles_changes_additions_and_deletions(self):
        self.skill.write_text(self.skill.read_text()+'More\n')
        (self.root/'skills/demo/references/original.txt').unlink()
        (self.root/'skills/demo/references/new.txt').write_text('new')
        result = updater.refresh(self.root, write=True)
        self.assertEqual(result['status'], 'UPDATED')
        manifest = self.read('manifest.json')
        self.assertEqual(manifest['files'], updater.records(self.root))
        current = self.read('verification.json')['current_repository']
        self.assertEqual(current['payload_files'], 2)
        self.assertEqual(current['modified_existing_payload_files_since_snapshot'], 1)
        self.assertEqual(current['additional_payload_files_since_snapshot'], ['skills/demo/references/new.txt'])
        self.assertEqual(current['removed_payload_files_since_snapshot'], ['skills/demo/references/original.txt'])
        self.assertIn('**1 added files**', (self.root/'README.md').read_text())

    def test_history_is_preserved_and_current_parity_invalidated(self):
        original = self.read('verification.json')
        self.skill.write_text('---\nname: demo\ndescription: different frontmatter\n---\nInstructions\n')
        updater.refresh(self.root, write=True)
        actual = self.read('verification.json')
        self.assertEqual(actual['history'], original['history'])
        self.assertEqual(actual['original_installed_snapshot'], original['original_installed_snapshot'])
        for field in ('local_installed_parity','cloud_parity'):
            self.assertTrue(actual['current_repository'][field].startswith('NOT VERIFIED'))

    def test_second_write_is_idempotent_and_preserves_file_mode(self):
        (self.root/'verification.json').chmod(0o640)
        before = self.outputs()
        self.assertEqual(updater.refresh(self.root, write=True)['status'], 'CURRENT')
        self.assertEqual(self.outputs(), before)
        self.assertEqual((self.root/'verification.json').stat().st_mode & 0o777, 0o640)

    def test_unregistered_skill_is_not_silently_invented(self):
        (self.root/'skills/new').mkdir()
        (self.root/'skills/new/SKILL.md').write_text('new')
        before = self.outputs()
        with self.assertRaisesRegex(ValueError, 'Curate manifest skill identities'):
            updater.refresh(self.root, write=True)
        self.assertEqual(self.outputs(), before)

    def test_symlink_payload_is_rejected_before_update(self):
        (self.root/'skills/demo/link.txt').symlink_to(self.root/'README.md')
        before = self.outputs()
        with self.assertRaisesRegex(ValueError, 'Refusing symlink'):
            updater.refresh(self.root, write=True)
        self.assertEqual(self.outputs(), before)

    def test_readme_parse_error_prevents_all_writes(self):
        (self.root/'README.md').write_text('missing count table')
        self.skill.write_text('changed')
        before = self.outputs()
        with self.assertRaisesRegex(ValueError, 'README'):
            updater.refresh(self.root, write=True)
        self.assertEqual(self.outputs(), before)

    def test_partial_write_reports_completed_paths_and_invalidates_first(self):
        self.skill.write_text('changed')
        before = self.outputs()
        replace = updater.os.replace
        def fail_manifest(source, target):
            if target.name == 'manifest.json':
                raise OSError('simulated write failure')
            return replace(source,target)
        with patch.object(updater.os, 'replace', side_effect=fail_manifest):
            with self.assertRaises(updater.UpdateError) as caught:
                updater.refresh(self.root, write=True)
        self.assertEqual(caught.exception.updated, ['verification.json'])
        self.assertEqual((self.root/'manifest.json').read_bytes(), before['manifest.json'])
        self.assertTrue(self.read('verification.json')['current_repository']['cloud_parity'].startswith('NOT VERIFIED'))
        self.assertFalse(list(self.root.glob('.library-refresh-*')))
        updater.refresh(self.root, write=True)
        self.assertEqual(updater.refresh(self.root)['status'], 'CURRENT')

    def test_executable_flag_is_refreshed(self):
        self.skill.chmod(0o755)
        updater.refresh(self.root, write=True)
        self.assertTrue(self.read('manifest.json')['files']['skills/demo/SKILL.md']['executable'])
