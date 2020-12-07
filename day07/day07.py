import sys
import inspect
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 7
def get_path():
    return "day{:02d}".format(DAY)

class Color:
    qualifyer: str = ""
    name: str = ""

    # def __init__(self, _qual, _name):
    #     self.qualifyer = _qual
    #     self.name = _name

    def __init__(self, combined: str):
        (self.qualifyer, self.name) = combined.split(" ")

    def get_name(self):
        return self.name

    def get_qualifyer(self):
        return self.qualifyer

    def display(self):
        print("I'm a color: {} {}".format(self.qualifyer, self.name))

    def get_color(self):
        return self.qualifyer+" "+self.name

    def __str__(self):
        return "{} {}".format(self.qualifyer, self.name)



@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    rules = loadingUtils.importToArray(in_file)
    for rule_str in rules:
        (parent, children) = rule_str[:-1].split(" bags contain ")
        print("{}  ->  {}".format(parent, children))
        if children == "no other bags":
            print("Has no Children")
            continue
        for child in children.split(", "):
            (num, qual, col, null) = child.split(" ")
            c_col = Color(qual+" "+col)
            print("  ---- {}x {}".format(num, c_col))
    # code here
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    # code here
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    # run_part_1(get_path() + "/input1")
    # run_part_2(get_path() + "/test2", True)
    # run_part_2(get_path() + "/input2")
