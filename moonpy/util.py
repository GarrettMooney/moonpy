import json
import os
import sys

from pathlib import Path
from typing import Union, Dict, Any, List, Tuple, Optional
from collections import OrderedDict

# fmt: off
FilePath = Union[str, Path]
# Superficial JSON input/output types
# https://github.com/python/typing/issues/182#issuecomment-186684288
JSONOutput = Union[str, int, float, bool, None, Dict[str, Any], List[Any]]
JSONOutputBin = Union[bytes, str, int, float, bool, None, Dict[str, Any], List[Any]]
# For input, we also accept tuples, ordered dicts etc.
JSONInput = Union[str, int, float, bool, None, Dict[str, Any], List[Any], Tuple[Any], OrderedDict]
JSONInputBin = Union[bytes, str, int, float, bool, None, Dict[str, Any], List[Any], Tuple[Any], OrderedDict]
YAMLInput = JSONInput
YAMLOutput = JSONOutput
# fmt: on

is_windows = sys.platform.startswith("win")
is_linux = sys.platform.startswith("linux")
is_osx = sys.platform == "darwin"


def path2str(path):
    return str(path)


def b_to_str(b_str):
    return str(b_str, encoding="utf-8")


def ensure_path(path):
    if isinstance(path, str):
        return Path(path)
    else:
        return path


#########
# symlink
#########
def symlink(orig, dest):
    """Create a symlink.

    :orig (unicode / Path): Origin path
    :dest (unicode / Path): Destination path of the symlink.
    """
    if is_windows:
        import subprocess

        subprocess.check_call(
            ["mklink", "/d", path2str(orig), path2str(dest)], shell=True
        )
    else:
        orig.symlink_to(dest)


def symlink_remove(link):
    """Remove a symlnk.

    :link (unicode / Path): The path to the symlink.
    """
    os.unlink(path2str(link))


######
# json
######
def force_path(location, require_exists=True):
    if not isinstance(location, Path):
        location = Path(location)
    if require_exists and not location.exists():
        raise ValueError(f"Can't read file: {location}")
    return location


def force_string(location):
    if isinstance(location, str):
        return location
    return str(location)


def json_dumps(
    data: JSONInput, indent: Optional[int] = 0, sort_keys: bool = False
) -> str:
    if sort_keys:
        indent = None if indent == 0 else indent
        result = json.dumps(
            data, indent=indent, separators=(",", ":"), sort_keys=sort_keys
        )
    else:
        result = json.dumps(data, indent=indent, escape_forward_slashes=False)
    return result


def read_json(location: FilePath) -> JSONOutput:
    if location == "-":
        data = sys.stdin.read()
        return json.loads(data)
    file_path = force_path(location)
    with file_path.open("r", encoding="utf8") as f:
        return json.load(f)


def write_json(location: FilePath, data: JSONInput, indent: int = 2) -> None:
    json_data = json_dumps(data, indent=indent)
    if location == "-":
        print(json_data)
    else:
        file_path = force_path(location, require_exists=False)
        with file_path.open("w", encoding="utf8") as f:
            f.write(json_data)
