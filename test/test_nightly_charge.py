import unittest
from datetime import datetime, timedelta
from app.nightly_charge import NightlyCharge


class BabysitterCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.nightly = NightlyCharge()

    def test_timedelta_checker(self):
        self.assertIsInstance(self.nightly.first_time(), timedelta)
        self.assertIsInstance(self.nightly.second_time(), timedelta)
        self.assertIsInstance(self.nightly.third_time(), timedelta)

    def test_timedelta_positive(self):
        self.assertGreaterEqual(self.nightly.first_time().total_seconds(), 0)
        self.assertGreaterEqual(self.nightly.second_time().total_seconds(), 0)
        self.assertGreaterEqual(self.nightly.third_time().total_seconds(), 0)
