import day22 as day

INPUTFOLDER = day.get_path()

def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 306


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 34255


def test_part_2_1():
    result = day.run_part_2(INPUTFOLDER+"/test1")
    assert result == 291


def test_part_2_2():
    result = day.run_part_2(INPUTFOLDER+"/test2")
    assert result == 105


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input1")
    assert result == 33369
