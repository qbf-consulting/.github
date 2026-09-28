import unittest

from scripts.audit_licenses import classify


class ClassifyLicenseTests(unittest.TestCase):
    def test_apache_2(self):
        self.assertEqual(classify('Apache License\nVersion 2.0'), 'Apache-2.0')

    def test_mit(self):
        self.assertEqual(classify('MIT License\nPermission is hereby granted'), 'MIT')

    def test_cc_by(self):
        self.assertEqual(classify('Creative Commons Attribution 4.0 International'), 'CC-BY-4.0')

    def test_cc_by_sa(self):
        self.assertEqual(classify('Creative Commons Attribution-ShareAlike 4.0 International'), 'CC-BY-SA-4.0')

    def test_mixed_map(self):
        text = 'Licensing Map\nCreative Commons Attribution 4.0\nApache License, Version 2.0'
        self.assertEqual(classify(text), 'MIXED')

    def test_unrecognized(self):
        self.assertEqual(classify('All rights reserved'), 'UNRECOGNIZED')


if __name__ == '__main__':
    unittest.main()
