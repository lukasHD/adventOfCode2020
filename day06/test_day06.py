import day06 as day

INPUTFOLDER = day.get_path()

def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 11


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 6551


def test_part_2():
    result = day.run_part_2(INPUTFOLDER+"/test1")
    assert result == 6


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input1")
    assert result == 3358
