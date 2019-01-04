from zeit.reader import file_reader
import datetime
import pytest


@pytest.fixture
def december(tmp_path):
    _file = tmp_path / "2018-12"
    _file.write_text("\n".join(["", "08:00-12:00", "08:00-12:00\t13:00-17:33"]))
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


def test_weekend_days_have_working_hours(sunday):
    assert datetime.timedelta(hours=4) == sunday.working_hours


def test_weekdays_have_working_hours(monday):
    assert datetime.timedelta(hours=8, minutes=33) == monday.working_hours


def test_weekdays_contribute_minus_hours(monday, monkeypatch):
    monkeypatch.setenv("ZEIT_SHIFT_LENGTH", "9")
    assert datetime.timedelta(minutes=-27) == monday.minus_hours


def test_weekdays_contribute_no_negative_minus_hours(monday, monkeypatch):
    monkeypatch.setenv("ZEIT_SHIFT_LENGTH", "8")
    assert datetime.timedelta() == monday.minus_hours


def test_weekdays_overtime(monday, monkeypatch):
    monkeypatch.setenv("ZEIT_SHIFT_LENGTH", "8")
    assert datetime.timedelta(minutes=33) == monday.overtime


def test_weekends_overtime(sunday):
    assert datetime.timedelta(hours=4) == sunday.overtime


def test_minus_hours_is_not_negative_overtime(monday, monkeypatch):
    monkeypatch.setenv("ZEIT_SHIFT_LENGTH", "9")
    assert datetime.timedelta() == monday.overtime
