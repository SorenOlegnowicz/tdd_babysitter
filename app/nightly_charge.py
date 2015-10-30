from datetime import datetime, timedelta


class NightlyCharge():

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

# Start Script
"""
while True:
    try:
        start = datetime.strptime(input('Start Time: '), '%H:%M')
        bed = datetime.strptime(input('Bed Time: '), '%H:%M')
        end = datetime.strptime(input('End Time: '), '%H:%M')
        break
    except:
        print('Please give your time in this format: HH:MM')

night = NightlyCharge(start, bed, end)
print(night.charge)
"""

# Debug
night = NightlyCharge()
print(type(night.second_time))
print(night.delta_conversion(night.first_time))
night.delta_conversion
print('Delta: {}'.format(night.delta_conversion(night.third_time)))
