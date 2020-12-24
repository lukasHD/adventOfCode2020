import day20 as day

INPUTFOLDER = day.get_path()

def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 20899048083289


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 45443966642567


def test_part_2():
    result = day.run_part_2(INPUTFOLDER+"/test1")
    assert result == 273


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input1")
    assert result == 1607
