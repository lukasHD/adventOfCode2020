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

    def __hash__(self):
        return hash((self.qualifyer, self.name))

    def __eq__(self, other):
        return (self.qualifyer, self.name) == (other.qualifyer, other.name)

    def __ne__(self, other):
        # Not strictly necessary, but to avoid having both x==y and x!=y
        # True at the same time
        return not(self == other)


def rule_to_dict(rule_str: str):
    (parent_str, children) = rule_str[:-1].split(" bags contain ")
    parent = Color(parent_str)
    #print("{}  ->  {}".format(parent, children))
    if children == "no other bags":
        #print("Has no Children")
        return [parent, []]
    child_list = []
    for child in children.split(", "):
        (num, qual, col, null) = child.split(" ")
        c_col = Color(qual+" "+col)
        child_list.append((num, c_col))
        #print("  |___ {}x {}".format(num, c_col))
    return [parent, child_list]


def find_valid_bags(mydict, goal):
    def _contains_goal_bag(mydict, key):
        if goal in mydict[key]:
            return True
        for value in mydict[key]:
            if _contains_goal_bag(mydict, value):
                return True
        return False
    
    valid_keys = set()
    for key in mydict.keys():
        print(key)
        if key == goal:
            continue
        if _contains_goal_bag(mydict, key):
            valid_keys.add(key)
    return valid_keys

@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    rules = loadingUtils.importToArray(in_file)
    rule_dict = {}
    for rule_str in rules:
        parent, child_list = rule_to_dict(rule_str)
        if child_list == []:
            if debug: print("no children")
            rule_dict[str(parent)] = []    
            continue
        if debug: print("{} --> {}".format(parent, ", ".join(map(str,list(zip(*child_list))[1]))))
        rule_dict[str(parent)] = list(map(str,list(zip(*child_list))[1]))
    if debug: print(rule_dict)
    valid_bags = find_valid_bags(rule_dict, "shiny gold")
    print(valid_bags)
    result = len(valid_bags)
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
    run_part_1(get_path() + "/input1")
    # run_part_2(get_path() + "/test2", True)
    # run_part_2(get_path() + "/input2")
