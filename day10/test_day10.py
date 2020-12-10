import day10 as day

INPUTFOLDER = day.get_path()

def test_part_1_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 35


def test_part_1_2():
    result = day.run_part_1(INPUTFOLDER+"/test2")
    assert result == 220


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 2376


def test_part_2_1():
    result = day.run_part_2(INPUTFOLDER+"/test1")
    assert result == 8


def test_part_2_2():
    result = day.run_part_2(INPUTFOLDER+"/test2")
    assert result == 19208


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input1")
    assert result == 129586085429248
