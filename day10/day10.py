import sys
import inspect
from codetiming import Timer
from functools import lru_cache
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 10
def get_path():
    return "day{:02d}".format(DAY)


def validate_chain(_list):
    a = _list[:]
    num1 = 0
    num3 = 0
    last = 0
    for i in a:
        diff = i - last
        # print("i: {:3} diff: {:3}".format(i, diff))
        if diff == 1:
            num1 += 1
        elif diff == 2:
            pass
        elif diff == 3:
            num3 += 1
        else:
            raise ValueError("Invalid Chain")
        last = i
    num3 += 1
    print("Number of 1 diff: {}   Number of 3 diff: {}".format(num1, num3))
    return num1*num3


@lru_cache()
def get_number_of_chains(adapters):
    num = 0
    try:
        n0,n1,n2,n3 = adapters[0:4]
    except ValueError:
        if len(adapters) == 3:
            n0,n1,n2 = adapters[0:3]
            n3 = -1
        if len(adapters) == 2:
            n0,n1 = adapters[0:2]
            n2 = -1
            n3 = -1
        if len(adapters) == 1:
            n0 = adapters[0:1]
            n1 = -1
            n2 = -1
            n3 = -1
            return 1   
    if n1-n0 in [1,2,3]:
        num += get_number_of_chains(tuple(adapters[1:]))
    if n2-n0 in [1,2,3]:
        num += get_number_of_chains(tuple(adapters[2:]))
    if n3-n0 in [1,2,3]:
        num += get_number_of_chains(tuple(adapters[3:]))
    return num


def get_number_of_chains_no_cache(adapters):
    num = 0
    try:
        n0,n1,n2,n3 = adapters[0:4]
    except ValueError:
        if len(adapters) == 3:
            n0,n1,n2 = adapters[0:3]
            n3 = -1
        if len(adapters) == 2:
            n0,n1 = adapters[0:2]
            n2 = -1
            n3 = -1
        if len(adapters) == 1:
            n0 = adapters[0:1]
            n1 = -1
            n2 = -1
            n3 = -1
            return 1   
    if n1-n0 in [1,2,3]:
        num += get_number_of_chains_no_cache(tuple(adapters[1:]))
    if n2-n0 in [1,2,3]:
        num += get_number_of_chains_no_cache(tuple(adapters[2:]))
    if n3-n0 in [1,2,3]:
        num += get_number_of_chains_no_cache(tuple(adapters[3:]))
    return num


@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    adapters = loadingUtils.importToIntArray(in_file)
    adapters.sort()
    print(adapters)
    result = validate_chain(adapters)
    # code here
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    _adapters = loadingUtils.importToIntArray(in_file)
    _adapters.append(0)
    _adapters.sort()
    adapters = tuple(_adapters)
    print(adapters)
    result = get_number_of_chains(adapters)
    # code here
    print("Result = {}".format(result))
    return result


@Timer()
def run_part_2_no_cache(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    _adapters = loadingUtils.importToIntArray(in_file)
    _adapters.append(0)
    _adapters.sort()
    adapters = tuple(_adapters)
    print(adapters)
    result = get_number_of_chains_no_cache(adapters)
    # code here
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/test2", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2_no_cache(get_path() + "/test1")
    run_part_2(get_path() + "/test2", True)
    run_part_2_no_cache(get_path() + "/test2")
    run_part_2(get_path() + "/input1")
