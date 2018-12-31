from zeit.reader import file_reader
import datetime
import pytest


@pytest.fixture
def december(tmp_path):
    _file = tmp_path / "2018-12"
    _file.write_text("\n")
    yield file_reader(_file)


@pytest.fixture
def saturday(december):
    saturday = next(december)
    assert 6 == saturday.date.isoweekday()
    yield saturday


def test_saturday_does_not_count_against_minus_hours(saturday):
    assert datetime.timedelta() == saturday.minus_hours
