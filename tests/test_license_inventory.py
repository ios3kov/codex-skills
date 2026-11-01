"""License accounting integrity; not legal clearance."""
import json
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from check_library import check_license_inventory, UNRESOLVED, MIT_PACKAGE, RESTRICTED_PACKAGE

class LicenseInventory(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name).resolve()
        (self.root / 'skills/demo').mkdir(parents=True)
        (self.root / 'plugins').mkdir()
        (self.root / 'skills/demo/NOTICE').write_text('notice')
        self.data = {'packages': [{'package': 'skills/demo', 'status': UNRESOLVED,
                                  'notice_files': ['skills/demo/NOTICE']}], 'skills': []}
        (self.root / 'NOTICE').write_text(f'| `skills/demo` | {UNRESOLVED} | None |\n')
        self.save()

    def save(self):
        (self.root / 'license-inventory.json').write_text(json.dumps(self.data))

    def test_valid_inventory(self):
        self.assertEqual(check_license_inventory(self.root), [])

    def test_new_package_is_detected(self):
        (self.root / 'plugins/new').mkdir()
        self.assertTrue(any('package mismatch' in e for e in check_license_inventory(self.root)))

    def test_extra_and_duplicate_packages(self):
        for name in ('skills/absent', 'skills/demo'):
            with self.subTest(name=name):
                self.data['packages'].append({'package': name, 'status': UNRESOLVED, 'notice_files': []})
                self.save()
                self.assertTrue(check_license_inventory(self.root))
                self.data['packages'].pop()

    def test_invalid_status(self):
        self.data['packages'][0]['status'] = 'approved'
        self.save()
        self.assertTrue(any('Invalid license status' in e for e in check_license_inventory(self.root)))

    def test_missing_and_escaping_notices(self):
        for name in ('missing', '../outside', str(self.root / 'skills/demo/NOTICE')):
            with self.subTest(name=name):
                self.data['packages'][0]['notice_files'] = [name]
                self.save()
                self.assertTrue(any('unsafe license notice' in e for e in check_license_inventory(self.root)))

    def test_notice_cannot_swap_unresolved_identity(self):
        (self.root / 'NOTICE').write_text(f'| `skills/other` | {UNRESOLVED} | None |\n')
        self.assertTrue(any('NOTICE package/status' in e for e in check_license_inventory(self.root)))

    def test_nested_skill_notices_are_checked(self):
        self.data['skills'] = [{'package': 'plugins/demo/skills/child', 'status': UNRESOLVED,
                                'notice_files': ['absent']}]
        self.save()
        self.assertTrue(any('unsafe license notice' in e for e in check_license_inventory(self.root)))

    def test_package_grants_require_retained_license(self):
        for status in (MIT_PACKAGE, RESTRICTED_PACKAGE):
            with self.subTest(status=status):
                self.data['packages'][0]['status'] = status
                self.save()
                (self.root / 'NOTICE').write_text(f'| `skills/demo` | {status} | None |\n')
                self.assertTrue(any('Package license missing' in e for e in check_license_inventory(self.root)))
                self.data['packages'][0]['package_license'] = 'skills/demo/NOTICE'
                if status == MIT_PACKAGE:
                    (self.root / 'skills/demo/NOTICE').write_text((Path(__file__).resolve().parents[1] / 'scripts/license-texts/MIT.txt').read_text())
                self.save()
                self.assertEqual(check_license_inventory(self.root), [])
                self.data['packages'][0].pop('package_license')

    def test_skill_inventory_missing_extra_and_duplicate(self):
        (self.root / 'skills/demo/SKILL.md').write_text('demo')
        self.assertTrue(any('skill mismatch' in e for e in check_license_inventory(self.root)))
        row = dict(self.data['packages'][0])
        self.data['skills'] = [row]
        self.save()
        self.assertEqual(check_license_inventory(self.root), [])
        for other in (row, dict(row, package='plugins/absent/skills/child')):
            with self.subTest(package=other['package']):
                self.data['skills'].append(other)
                self.save()
                self.assertTrue(any('skill mismatch' in e or 'Duplicate license inventory skill' in e for e in check_license_inventory(self.root)))
                self.data['skills'].pop()

    def test_new_nested_plugin_skill_is_detected(self):
        nested = self.root / 'plugins/demo/skills/new/SKILL.md'
        nested.parent.mkdir(parents=True)
        nested.write_text('new skill')
        self.assertTrue(any('skill mismatch: plugins/demo/skills/new' in e for e in check_license_inventory(self.root)))

    def add_source(self, **fields):
        import hashlib
        source = {'license_file': 'NOTICE', 'sha256': hashlib.sha256(b'notice').hexdigest()}
        source.update(fields)
        self.data['packages'][0]['license_review'] = {'sources': [source]}
        self.save()

    def test_source_license_hash_detects_changed_bytes(self):
        self.add_source()
        self.assertEqual(check_license_inventory(self.root), [])
        (self.root / 'skills/demo/NOTICE').write_text('changed')
        self.assertTrue(any('SHA-256 mismatch' in e for e in check_license_inventory(self.root)))

    def test_missing_or_invalid_source_hash_fails(self):
        for digest in (None, 'bad'):
            with self.subTest(digest=digest):
                self.add_source(sha256=digest)
                self.assertTrue(any('source license hash' in e for e in check_license_inventory(self.root)))

    def test_source_license_path_cannot_escape_package(self):
        for name in ('../demo/NOTICE', str(self.root / 'skills/demo/NOTICE')):
            with self.subTest(path=name):
                self.add_source(license_file=name)
                self.assertTrue(any('unsafe source license' in e for e in check_license_inventory(self.root)))

    def test_mit_grant_rejects_arbitrary_notice_and_modified_terms(self):
        row = self.data['packages'][0]
        row.update(status=MIT_PACKAGE, package_license='skills/demo/NOTICE')
        (self.root / 'NOTICE').write_text(f'| `skills/demo` | {MIT_PACKAGE} | MIT |\n')
        canonical = (Path(__file__).resolve().parents[1] / 'scripts/license-texts/MIT.txt').read_text()
        for text in ('notice', canonical + 'No commercial use.\n', canonical.replace('sublicense, and/or sell', 'use')):
            with self.subTest(text=text[:30]):
                (self.root / 'skills/demo/NOTICE').write_text(text)
                self.save()
                self.assertTrue(any('MIT text mismatch' in e for e in check_license_inventory(self.root)))

    def test_mit_accepts_multiple_copyrights_and_wrapping(self):
        from check_library import is_mit_text
        canonical = (Path(__file__).resolve().parents[1] / 'scripts/license-texts/MIT.txt').read_text()
        canonical = canonical.replace('Copyright (c) 2026 ios3kov', 'Copyright (c) 2025 Original Author\nCopyright (c) 2026 Adaptation Author')
        self.assertTrue(is_mit_text(canonical))
        self.assertTrue(is_mit_text(canonical.replace('to deal\nin', 'to deal in')))

    def test_skill_level_source_hash_is_checked(self):
        (self.root / 'skills/demo/SKILL.md').write_text('demo')
        row = dict(self.data['packages'][0])
        row['license_review'] = {'sources': [{'license_file': 'NOTICE', 'sha256': '0' * 64}]}
        self.data['skills'] = [row]
        self.save()
        self.assertTrue(any('Source license SHA-256 mismatch' in e for e in check_license_inventory(self.root)))
