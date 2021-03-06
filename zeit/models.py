import datetime
import os
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
    def expected_shift_length(self):
        return datetime.timedelta(hours=float(os.environ.get("ZEIT_SHIFT_LENGTH", 8.4)))

    @property
    def is_weekend(self):
        return self.date.isoweekday() in [6, 7]

    @property
    def minus_hours(self):
        if self.is_weekend:
            return datetime.timedelta()

        time_difference = self.working_hours - self.expected_shift_length

        if time_difference < datetime.timedelta():
            return time_difference

        return datetime.timedelta()

    @property
    def overtime(self):
        if self.is_weekend:
            return self.working_hours

        time_difference = self.working_hours - self.expected_shift_length

        if time_difference > datetime.timedelta():
            return self.working_hours - self.expected_shift_length

        return datetime.timedelta()

    @property
    def remark(self):
        data = self.data.split("\t")[-1]

        try:
            [time.strptime(_, "%H:%M") for _ in data.split("-")]
        except ValueError:
            return data

        return ""

    @property
    def working_hours(self):
        shifts = [Day.parse_shift(shift) for shift in self.data.split("\t")]
        return sum(shifts, datetime.timedelta())
