"""
DAY 1
"""
import sys
sys.path.insert(0, 'D:\\projects\\aoc2020\\')

import inspect
from codetiming import Timer

import itertools
import functools

from helper import loadingUtils, pretty

DAY = 1
def getPath():
    return "day{:02d}".format(DAY)


@Timer()
def runPart1(inFile: str, debug: bool = False) -> int:
    pretty.printHeader(DAY,1, inspect.stack()[0].function, inFile)
    result = 0
    numbers = loadingUtils.importToIntArray(inFile)
    results = []
    for i in range(len(numbers)):
        a = numbers[i]
        for j in range(i,len(numbers)):
            b = numbers[j]
            if debug: print("{} {} : {} + {} = {}".format(i, j, a, b, a+b))
            if (a + b == 2020):
                results.append((a,b))
    print(results)
    print(len(results))
    assert len(results) != 0
    assert len(results[0]) == 2
    result = results[0][0] * results[0][1]
    print("Numbers {} and {} add to 2020 and have a product of {}"
            .format(results[0][0], results[0][1], result))
    return result


@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    """
    Runs part 2 of the day
    """
    pretty.printHeader(DAY,2,inspect.stack()[0].function, in_file)
    result = 0
    numbers = loadingUtils.importToIntArray(in_file)
    results = []
    # Code here
    ## itertools.product(numbers, repeat=3) gives many repetitions
    for tripel in itertools.combinations(numbers, 3):
        if debug: 
            print(tripel)
        if functools.reduce(lambda a,b : a+b, tripel) == 2020 :
            results.append(tripel)
    print(results)
    print(len(results))
    assert len(results) != 0
    assert len(results[0]) == 3
    winner_tripel = results[0]
    result = functools.reduce(lambda a,b: a*b, results[0])
    print("Numbers {} add to 2020 and have a product of {}".format(winner_tripel, result))
    return result

if __name__ == "__main__":
    runPart1(getPath() + "/test1", True)
    runPart1(getPath() + "/input")
    run_part_2(getPath() + "/test1", True)
    run_part_2(getPath() + "/input")
