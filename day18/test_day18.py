import day18 as day

INPUTFOLDER = day.get_path()

def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 26457


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 11004703763391


def test_part_2():
    result = day.run_part_2(INPUTFOLDER+"/test1")
    assert result == 694173


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input1")
    assert result == 290726428573651
