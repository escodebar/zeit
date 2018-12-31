from zeit.models import Day
from zeit.reader import file_reader
import pytest


@pytest.fixture
def data_file(tmp_path):
    _file = tmp_path / "2018-12"
    _file.write_text("\n")
    yield _file


def test_file_reader_generates_day_objects(data_file):
    test_data_reader = file_reader(data_file)
    day = next(test_data_reader)
    assert isinstance(day, Day)
