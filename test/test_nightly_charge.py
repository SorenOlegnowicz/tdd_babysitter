import unittest
from datetime import datetime, timedelta
from app.nightly_charge import NightlyCharge


class BabysitterCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.nightly = NightlyCharge()

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
    def test_first_charge(self):
        """Cost: $12 per hour"""
        self. assertEqual(self.nightly.charge(self.nightly.first_time), (self.nightly.first_time*12))
