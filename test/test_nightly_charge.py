import unittest
from datetime import datetime, timedelta
from app.nightly_charge import NightlyCharge


class BabysitterCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.nightly = NightlyCharge()
        self.midnightly = NightlyCharge('10:00', '1:00', '3:00')

    # Test One
    def test_timedelta_checker(self):
        self.assertIsInstance(self.nightly.first_timedelta(), timedelta)
        self.assertIsInstance(self.nightly.second_timedelta(), timedelta)
        self.assertIsInstance(self.nightly.third_timedelta(), timedelta)

    # Test Two
    def test_timedelta_positive(self):
        self.assertGreaterEqual(self.nightly.first_timedelta().total_seconds(), 0)
        self.assertGreaterEqual(self.nightly.second_timedelta().total_seconds(), 0)
        self.assertGreaterEqual(self.nightly.third_timedelta().total_seconds(), 0)

    # Test Three
    def test_delta_conversion(self):
        self.assertIsInstance(self.nightly.delta_conversion(self.nightly.first_time), float)
        self.assertIsInstance(self.nightly.delta_conversion(self.nightly.second_time), float)
        self.assertIsInstance(self.nightly.delta_conversion(self.nightly.third_time), float)

    # Test Four
    def test_charge(self):
        self.assertEqual(self.nightly.charge(self.nightly.first_time, self.nightly.first_pay), (self.nightly.delta_conversion(self.nightly.first_time) * 12))
        self.assertEqual(self.nightly.charge(self.nightly.second_time, self.nightly.second_pay), (self.nightly.delta_conversion(self.nightly.second_time) * 8))
        self.assertEqual(self.nightly.charge(self.nightly.third_time, self.nightly.third_pay), (self.nightly.delta_conversion(self.nightly.third_time) * 16))

    # Test Five
    def test_total_charge(self):
        self.assertEqual(self.nightly.total_charge(), (3 * 12) + (4 * 8) + (4 * 16))
