from datetime import datetime, timedelta


class NightlyCharge():
    first_pay = 12
    second_pay = 8
    third_pay = 16

    def __init__(self, start_time='5:00', bed_time='8:00', end_time='4:00'):
        self.start_time = datetime.strptime(start_time, '%H:%M')
        self.bed_time = datetime.strptime(bed_time, '%H:%M')
        self.midnight = datetime.strptime('12:00', '%H:%M')
        self.end_time = datetime.strptime(end_time, '%H:%M')
        self.first_time = self.first_timedelta()
        self.second_time = self.second_timedelta()
        self.third_time = self.third_timedelta()

    def __str__(self):
        return "Start Time: {}\n  Bed Time: {}\n  End Time: {}".format(self.start_time, self.bed_time, self.end_time)

    def first_timedelta(self):
        return self.bed_time - self.start_time

    def second_timedelta(self):
        return self.midnight - self.bed_time

    def third_timedelta(self):
        return self.end_time - self.midnight + timedelta(hours=12)

    def delta_conversion(self, time):
        return (time.total_seconds()) / 3600

    def charge(self, time, pay):
        return self.delta_conversion(time) * pay

    def total_charge(self):
        return self.charge(self.first_time, self.first_pay) + self.charge(self.second_time, self.second_pay) + self.charge(self.third_time, self.third_pay)

# Start Script
"""
try:
    start = input('Start Time: ')
    bed = input('Bed Time: ')
    end = input('End Time: ')
except:
    print('None')

night = NightlyCharge(start, bed, end)
"""
