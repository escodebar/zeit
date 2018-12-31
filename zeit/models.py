import datetime


class Day:
    def __init__(self, *, year, month, day, data):
        self.date = datetime.date(year, month, day)
        self.data = data
