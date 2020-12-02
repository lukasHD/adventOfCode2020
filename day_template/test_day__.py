import day__ as day

inputFolder = day.getPath()

def test_part1():
    result = day.runPart1(inputFolder+"/test1")
    assert result == 0


def test_part2():
    result = day.runPart2(inputFolder+"/test2")
    assert result == 0