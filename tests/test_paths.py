from pathlib import Path
from moonpy.util import force_string


def test_force_string_str():
    assert isinstance(force_string("foobar"), str)


def test_force_string_int():
    assert isinstance(force_string(32), str)


def test_force_string_float():
    assert isinstance(force_string(32 / 3), str)


def test_force_string_path():
    assert isinstance(force_string(Path(__file__)), str)
