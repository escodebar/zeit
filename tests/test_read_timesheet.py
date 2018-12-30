from zeit.models import Day
from zeit.reader import file_reader


def test_file_reader_generates_day_objects():
    test_data_reader = file_reader('tests/data/2018-12')
    day = next(test_data_reader)
    assert isinstance(day, Day)
