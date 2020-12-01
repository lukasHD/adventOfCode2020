import sys
sys.path.insert(0, 'D:\\projects\\aoc2020\\')

#from helper import importToIntArray
from helper import loadingUtils


def inc(x):
    return x + 1

def run(inFile):
    result = 0
    numbers = loadingUtils.importToIntArray(inFile)
    print(numbers)
    for (a, b) in numbers:
        print("{} + {} = {}".format(a, b, a+b))
    return result

if __name__ == "__main__":
    run("day01/test1")
    pass