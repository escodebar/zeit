from zeit.models import Day


def file_reader(file_path):
    with open(file_path, 'r') as data_file:
        data_lines = data_file.readlines()

    yield from [Day(day_line.strip()) for day_line in data_lines]
