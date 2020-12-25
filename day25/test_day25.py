import day25 as day

INPUTFOLDER = day.get_path()


def test_transform_1():
    assert 5764801 == day.transform(7,8)


def test_transform_2():
    assert 17807724 == day.transform(7,11)

def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 14897079


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 1478097


def test_part_2():
    result = day.run_part_2(INPUTFOLDER+"/test2")
    assert result == 0


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input2")
    assert result == 0
