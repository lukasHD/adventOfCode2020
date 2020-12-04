import day04 as day
from helper import loadingUtils

INPUTFOLDER = day.get_path()

def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 2


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 254


def test_validate():
    valid_passports   = loadingUtils.import_multiline(INPUTFOLDER+"/test_valid")
    invalid_passports = loadingUtils.import_multiline(INPUTFOLDER+"/test_invalid")
    for valid in valid_passports:
        print(valid)
        validity = day.validate_passport(valid)
        assert validity == True
    for invalid in invalid_passports:
        print(invalid)
        validity = day.validate_passport(invalid)
        assert validity == False

def test_part_2():
    result = day.run_part_2(INPUTFOLDER+"/test1")
    assert result == 2


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input1")
    assert result == 184
