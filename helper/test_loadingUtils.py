#from helper import *
from helper import loadingUtils
import pytest

def test_return42():
    assert loadingUtils.return42() == 42


def test_printShit(capsys):
    loadingUtils.printShit()
    captured = capsys.readouterr()
    assert captured.out == "This is shit from the helper library\n"


def test_importToArrayRaises():
    with pytest.raises(FileNotFoundError):
        loadingUtils.importToArray("non_exisiting_filename")


def test_importToArray():
    out = loadingUtils.importToArray("helper/test_input_importToArray")
    assert out == ['2','4','6','8','99','-42']


def test_importToIntArray():
    out = loadingUtils.importToIntArray("helper/test_input_importToArray")
    assert out == [2,4,6,8,99,-42]


def test_import_multiline():
    out = loadingUtils.import_multiline("helper/test_multiline")
    assert out == ["Line 1 Line 2 Line 3", "Line 4 Line 5"]


def test_import_multiline2():
    out = loadingUtils.import_multiline("helper/test_multiline_2")
    assert out == ["Line 1 Line 2 Line 3", "Line 4 Line 5"]
