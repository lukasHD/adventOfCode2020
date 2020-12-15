import day15 as day

INPUTFOLDER = day.get_path()


def test_part_1():
    result = day.run_part_1([0,3,6])
    assert result == 436


def test_part_1_real():
    result = day.run_part_1([0,14,1,3,7,9])
    assert result == 763


def test_01_a():
    in_list = [0,3,6]
    result = day.get_number(in_list, 2020)
    assert result == 436


def test_02_a():
    inp = [1,3,2]
    result = day.get_number(inp)
    assert result == 1


def test_03_a():
    inp = [2,1,3]
    result = day.get_number(inp)
    assert result == 10


def test_04_a():
    inp = [1,2,3]
    result = day.get_number(inp)
    assert result == 27


def test_05_a():
    inp = [2,3,1]
    result = day.get_number(inp)
    assert result == 78


def test_06_a():
    inp = [3,2,1]
    result = day.get_number(inp)
    assert result == 438


def test_07_a():
    inp = [3,1,2]
    result = day.get_number(inp)
    assert result == 1836



def test_01_b():
    in_list = [0,3,6]
    result = day.get_number(in_list, 30000000)
    assert result == 175594


def test_02_b():
    inp = [1,3,2]
    result = day.get_number(inp, 30000000)
    assert result == 2578


def test_03_b():
    inp = [2,1,3]
    result = day.get_number(inp, 30000000)
    assert result == 3544142


def test_04_b():
    inp = [1,2,3]
    result = day.get_number(inp, 30000000)
    assert result == 261214


def test_05_b():
    inp = [2,3,1]
    result = day.get_number(inp, 30000000)
    assert result == 6895259


def test_06_b():
    inp = [3,2,1]
    result = day.get_number(inp, 30000000)
    assert result == 18


def test_07_b():
    inp = [3,1,2]
    result = day.get_number(inp, 30000000)
    assert result == 362


# def test_part_2():
#     result = day.run_part_2(INPUTFOLDER+"/test2")
#     assert result == 0


# def test_part_2_real():
#     result = day.run_part_2([0,14,1,3,7,9])
#     assert result == 1876406
