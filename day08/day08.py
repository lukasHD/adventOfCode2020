import sys
import inspect
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

import computer.computer as cp

DAY = 8
def get_path():
    return "day{:02d}".format(DAY)

@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    prog_array = loadingUtils.importToArray(in_file)
    handheld = cp.Computer()
    handheld.hard_reset()
    handheld.debug = debug
    handheld.load_program(prog_array)
    result = handheld.run_day08_1()
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    prog_array = loadingUtils.importToArray(in_file)
    handheld = cp.Computer()
    handheld.hard_reset()
    handheld.debug = debug
    handheld.load_program(prog_array)
    result = handheld.run_day08_2()
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1", False)
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
