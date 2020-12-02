import day02 as day

INPUTFOLDER = day.get_path()

def test_part1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 2


def test_part1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 591


def test_part2():
    result = day.run_part_2(INPUTFOLDER+"/test1")
    assert result == 1


def test_part2_real():
    result = day.run_part_2(INPUTFOLDER+"/input1")
    assert result == 335
