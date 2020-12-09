import sys
import inspect
import queue
from itertools import combinations
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 9
def get_path():
    return "day{:02d}".format(DAY)


def find_wrong_number(numbers, preamble, debug = False):
    window = queue.Queue()
    for k, num in enumerate(numbers):
        if k < preamble:
            print("Fill Queue with {:5}".format(num))
            window.put(num)
            continue
        allowed_numbers = list(map(lambda pair: pair[0]+pair[1],
                                   combinations(list(window.queue), 2)))
        if debug:
            print("num {} in allowed? {}".format(num, allowed_numbers))
        if num in allowed_numbers:
            window.get()
            window.put(num)
        else:
            print("{} NOT in the List".format(num))
            return num
    return 0


def find_weaknes(numbers, _weakness):
    for window_length in range(2,50):
        print("~~~~~ window length = {:3}".format(window_length))
        window = queue.Queue()
        for k, num in enumerate(numbers):
            if k < window_length:
                window.put(num)
                continue
            current_numbers = list(window.queue)
            if _weakness == sum(current_numbers):
                print("Found weakness with list {}".format(current_numbers))
                min_n = min(current_numbers)
                max_n = max(current_numbers)
                print("min: {}     max: {}".format(min_n, max_n))
                return min_n + max_n
            window.get()
            window.put(num)
    return 0


@Timer()
def run_part_1(in_file: str, preamble = 25, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    numbers = loadingUtils.importToIntArray(in_file)
    result = find_wrong_number(numbers, preamble, debug)
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, _weakness, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    numbers = loadingUtils.importToIntArray(in_file)
    result = find_weaknes(numbers, _weakness)
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    weakness_test = run_part_1(get_path() + "/test1", 5, True)
    weakness = run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", weakness_test, True)
    run_part_2(get_path() + "/input1", weakness)
