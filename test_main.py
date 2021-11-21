import tempfile
from pathlib import Path

import pytest

from main import fmt
from main import fmtfile


@pytest.mark.parametrize(
    ["filename", "new_filename"],
    [
        ("helloworld.txt", "helloworld.txt"),
        ("hello world.txt", "hello_world.txt"),
        ("HelloWorld.txt", "helloworld.txt"),
    ],
)
def test_fmtfile(filename, new_filename):
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / filename
        with open(path, "w") as f:
            f.write("")
        expected = Path(tmp) / new_filename
        assert fmtfile(path) == expected


def test_fmt():
    with tempfile.TemporaryDirectory() as tmp:
        names = ["byeworld.txt", "hello world.txt", "HelloWorld.txt"]
        new_names = ["byeworld.txt", "hello_world.txt", "helloworld.txt"]
        files = [Path(tmp) / name for name in names]
        for file in files:
            with open(file, "w") as f:
                f.write("")
        expected = [Path(tmp) / name for name in new_names]
        assert sorted(fmt(Path(tmp))) == sorted(expected)
