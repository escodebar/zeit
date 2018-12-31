from datetime import datetime
from zeit.models import Day
import os


def file_reader(file_path):

    date = datetime.strptime(os.path.basename(file_path), "%Y-%m")

    with open(file_path, 'r') as data_file:
        data_lines = data_file.readlines()

    yield from [
        Day(
            year=date.year,
            month=date.month,
            day=day_number,
            data=day_line.strip(),
        )
        for day_number, day_line in enumerate(data_lines, 1)
    ]
