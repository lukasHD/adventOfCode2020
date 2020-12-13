import day13 as day

INPUTFOLDER = day.get_path()

def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 295


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 3035


def test_part_2():
    result = day.run_part_2(INPUTFOLDER+"/test1")
    assert result == 1068781


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input1")
    assert result == 725169163285238
