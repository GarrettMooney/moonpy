import pytest


@pytest.fixture(scope="module")
def data():
    return {
        "data": {"a": 1, "c": 3, "b": 2},
        "file_contents": '{\n    "hello": "world"\n}',
        "invalid_file_contents": '{\n    "hello": world\n}',
        "file_name": "tmp.json",
        "sorted_file_contents": '{"a":1,"b":2,"c":3}',
    }
