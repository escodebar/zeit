import datetime
import time


class Day:
    def __init__(self, *, year, month, day, data):
        self.date = datetime.date(year, month, day)
        self.data = data

    @staticmethod
    def parse_shift(data):
        try:
            start, end = map(lambda x: time.strptime(x, "%H:%M"), data.split("-"))
            return datetime.timedelta(
                hours=end.tm_hour - start.tm_hour, minutes=end.tm_min - start.tm_min
            )

        except ValueError:
            return datetime.timedelta()

    @property
    def minus_hours(self):
        if self.date.isoweekday() in [6, 7]:
            return datetime.timedelta()

    @property
    def working_hours(self):
        shifts = [Day.parse_shift(shift) for shift in self.data.split("\t")]
        return sum(shifts, datetime.timedelta())
