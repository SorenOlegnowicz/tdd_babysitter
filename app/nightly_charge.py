from datetime import datetime


class NightlyCharge():
    def __init__(self, start_time='5:00', bed_time='8:00', end_time='4:00'):
        self.start_time = datetime.strptime(start_time, '%H:%M')
        self.bed_time = datetime.strptime(bed_time, '%H:%M')
        self.end_time = datetime.strptime(end_time, '%H:%M')

    def __str__(self):
        return "Start Time: {}\n  Bed Time: {}\n  End Time: {}".format(self.start_time, self.bed_time, self.end_time)


# Start Script
"""
try:
    start = datetime.strptime(input('Start Time: '), '%H:%M')
    bed = datetime.strptime(input('Bed Time: '), '%H:%M')
    end = datetime.strptime(input('End Time: '), '%H:%M')
except:
    print('Please give your time in this format: HH:MM')

night = NightlyCharge(start, bed, end)
print(night.charge)
"""
