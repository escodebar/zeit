import datetime


class Day:
    def __init__(self, *, year, month, day, data):
        self.date = datetime.date(year, month, day)
        self.data = data

    @property
    def minus_hours(self):
        if self.date.isoweekday() in [6, 7]:
            return datetime.timedelta()
