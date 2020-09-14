import pytest

from .util import make_tempdir
from moonpy.util import json_dumps, read_json


def test_json_dumps_sort_keys(data):
    result = json_dumps(data["data"], sort_keys=True)
    assert result == data["sorted_file_contents"]


def test_read_json_file(data):
    with make_tempdir({data["file_name"]: data["file_contents"]}) as temp_dir:
        file_path = temp_dir / data["file_name"]
        assert file_path.exists()
        data = read_json(file_path)
    assert len(data) == 1
    assert data["hello"] == "world"


def test_read_json_file_invalid(data):
    with make_tempdir({data["file_name"]: data["invalid_file_contents"]}) as temp_dir:
        file_path = temp_dir / data["file_name"]
        assert file_path.exists()
        with pytest.raises(ValueError):
            read_json(file_path)
