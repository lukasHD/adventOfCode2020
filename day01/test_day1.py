#from day01.py import *
import day01

def test_answer():
    assert day01.inc(4) == 5

def test_part1():
    result = day01.run("day01/test1")
    assert result == 514579
