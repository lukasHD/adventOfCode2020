import sys
import inspect
import itertools
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 6
def get_path():
    return "day{:02d}".format(DAY)

@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    answer_groups = loadingUtils.import_multiline(in_file, separator="empty Line", joinString=False)
    for answers in answer_groups:
        answers = set(itertools.chain.from_iterable(map(list, answers)))
        result += len(answers)
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    answer_groups = loadingUtils.import_multiline(in_file, separator="empty Line", joinString=False)
    for answers in answer_groups:
        answers = list(map(set, answers))
        intersections = set.intersection(*answers)
        result += len(intersections)
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
