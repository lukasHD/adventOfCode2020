import day09 as day

INPUTFOLDER = day.get_path()

def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1", 5)
    assert result == 127


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 507622668


def test_part_2():
    weak = day.run_part_1(INPUTFOLDER+"/test1", 5)
    result = day.run_part_2(INPUTFOLDER+"/test1", weak)
    assert result == 62


def test_part_2_real():
    weak = day.run_part_1(INPUTFOLDER+"/input1", 25)
    result = day.run_part_2(INPUTFOLDER+"/input1", weak)
    assert result == 76688505
