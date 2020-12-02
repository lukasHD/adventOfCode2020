import sys
sys.path.insert(0, 'D:\\projects\\aoc2020\\')

import inspect
from codetiming import Timer

from helper import loadingUtils, pretty

day = 2

import os
import sys

def getPath():
    return "day{:02d}".format(day)

@Timer()
def runPart1(inFile: str, debug: bool = False) -> int:
    pretty.printHeader(day, 1, inspect.stack()[0].function, inFile)
    result = 0
    # code here
    return result

@Timer()
def runPart2(inFile: str, debug: bool = False) -> int:
    pretty.printHeader(day, 2, inspect.stack()[0].function, inFile)
    result = 0
    # code here
    return result

if __name__ == "__main__":
    runPart1(getPath + "/test1", True)
    runPart1(getPath + "/input")
    runPart2(getPath + "/test1", True)
    runPart2(getPath + "/input")

