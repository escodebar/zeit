from zeit.reader import file_reader
import datetime
import pytest


@pytest.fixture
def december(tmp_path):
    _file = tmp_path / "2018-12"
    _file.write_text("\n".join(["", "", "08:00-12:00\t13:00-17:33"]))
    yield file_reader(_file)


@pytest.fixture
def saturday(december):
    saturday = next(december)
    assert 6 == saturday.date.isoweekday()
    yield saturday


@pytest.fixture
def sunday(december):
    _ = next(december)
    sunday = next(december)
    assert 7 == sunday.date.isoweekday()
    yield sunday


@pytest.fixture
def monday(december):
    for i in range(2):
        next(december)
    monday = next(december)
    assert 1 == monday.date.isoweekday()
    yield monday


def test_saturday_does_not_count_against_minus_hours(saturday):
    assert datetime.timedelta() == saturday.minus_hours


def test_sunday_does_not_count_against_minus_hours(sunday):
    assert datetime.timedelta() == sunday.minus_hours


@pytest.mark.xfail
def test_weekdays_have_working_hours(monday):
    assert datetime.timedelta(hours=8, minutes=33) == monday.working_hours
