import unittest
from datetime import datetime
from app.nightly_charge import NightlyCharge


class BabysitterCalculatorTest(unittest.TestCase):
    def setUp(self):
        self.nightly = NightlyCharge()

    def test_time_checker(self):
        self.assertTrue(datetime.strptime(self.nightly.start_time, '%H:%M'))
        self.assertTrue(datetime.strptime(self.nightly.bed_time, '%H:%M'))
        self.assertTrue(datetime.strptime(self.nightly.end_time, '%H:%M'))
