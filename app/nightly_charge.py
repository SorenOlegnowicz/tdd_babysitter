class NightlyCharge():

    def __init__(self, start_time='5:00', bed_time='8:00', end_time='4:00'):
        self.start_time = start_time
        self.bed_time = bed_time
        self.end_time = end_time

    def __str__(self):
        return "Start Time: {}\n  Bed Time: {}\n  End Time: {}".format(self.start_time, self.bed_time, self.end_time)
