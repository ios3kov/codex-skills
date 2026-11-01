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
                self.save()
                self.assertEqual(check_license_inventory(self.root), [])
                self.data['packages'][0].pop('package_license')
