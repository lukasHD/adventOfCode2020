import day02 as day

inputFolder = day.getPath()

def test_part1():
    result = day.runPart1(inputFolder+"/test1")
    assert result == 2


def test_part1_real():
    result = day.runPart1(inputFolder+"/input1")
    assert result == 591


def test_part2():
    result = day.runPart2(inputFolder+"/test1")
    assert result == 1


def test_part2_real():
    result = day.runPart2(inputFolder+"/input1")
    assert result == 335