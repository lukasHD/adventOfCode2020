#from day01.py import *
import day01


def test_part1():
    result = day01.runPart1("day01/test1")
    assert result == 514579

def test_part1_real():
    result = day01.runPart1("day01/input")
    assert result == 864864


def test_part2():
    result = day01.runPart2("day01/test1")
    assert result == 241861950

def test_part2_real():
    result = day01.runPart2("day01/input")
    assert result == 281473080
