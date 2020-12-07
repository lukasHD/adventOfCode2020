import day07 as day

INPUTFOLDER = day.get_path()


def test_color_1():
    q = "qual"
    n = "name"
    a = day.Color(q+" "+n)
    assert a.get_name() == n
    assert a.get_qualifyer() == q
    assert a.get_color() == q+" "+n

def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 4


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 0


def test_part_2():
    result = day.run_part_2(INPUTFOLDER+"/test2")
    assert result == 0


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input2")
    assert result == 0
