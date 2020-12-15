import sys
import inspect
from collections import defaultdict
from codetiming import Timer
from more_itertools import locate
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 15
def get_path():
    return "day{:02d}".format(DAY)


def get_2020_number(in_list, stop = 2020):
    # 2020, 2019, or 2021 (0 or 1 as first index?)
    for i in range(stop-len(in_list)):
    #for i in range(10):
        last_number = in_list[-1]
        index_pos_list = list(locate(in_list, lambda a: a == last_number))
        if len(index_pos_list) < 2:
            in_list.append(0)
        else:
            in_list.append(index_pos_list[-1] - index_pos_list[-2])
        #print(in_list)
    print(in_list[-5:])
    return in_list[-1]


def get_number(in_list, stop = 2020):
    my_dict = defaultdict(list)
    for i, n in enumerate(in_list):
        my_dict[n].append(i)
    last_number = in_list[-1]
    for step in range(len(in_list), stop):
        if len(my_dict[last_number]) < 2:
            age = 0
            my_dict[age].append(step)
        else:
            age = my_dict[last_number][-1] -my_dict[last_number][-2]
            my_dict[age].append(step)
            del my_dict[age][:-2]
        last_number = age
    return last_number

@Timer()
def run_part_1(in_file, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = get_2020_number(in_file)
    # code here
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    #result = get_number(in_file, 2020)
    result = get_number(in_file, 30000000)
    # code here
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1([0,3,6], True)
    run_part_1([0,14,1,3,7,9])
    run_part_2([0,3,6], True)
    run_part_2([0,14,1,3,7,9])
