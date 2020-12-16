import sys
import inspect
from copy import deepcopy
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 16
def get_path():
    return "day{:02d}".format(DAY)


def parser(notes):
    mode = "rules"
    rules = []
    skip = False
    my_ticket = []
    nearby = []
    for line in notes:
        if   line == '' and mode == "rules":
            mode = "myTicket"
            skip = True
            continue
        elif line == '' and mode == "myTicket":
            mode = "nearby"
            skip = True
            continue
        elif skip:
            skip = False
            continue

        if mode == "rules":
            rule_list = [list(map(int, x.split("-"))) for x in line.split(": ")[1].split(" or ")]
            rules.append(rule_list)
            #print(rule_list)
        elif mode == "myTicket":
            my_ticket = list(map(int, line.split(",")))
            #print(my_ticket)
        elif mode == "nearby":
            ticket = list(map(int, line.split(",")))
            nearby.append(ticket)
            #print(ticket)
    return rules, my_ticket, nearby


def sum_wrong(rules, nearby):
    result = 0
    for ticket in nearby:
        for value in ticket:
            if not is_valid_any(rules, value):
                print("Invalid Ticket {}".format(ticket))
                result += value
    return result


def is_valid_any(rules, value):
    valid = False
    for rule in rules:
        for subrule in rule:
            if value in range(subrule[0], subrule[1]+1):
                valid = True
    return valid


def cleanup(rules, nearby):
    clean = []
    for ticket in nearby:
        add = True
        for value in ticket:
            if not is_valid_any(rules, value):
                add = False
        if add:
            clean.append(deepcopy(ticket))
    return clean

@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    notes = loadingUtils.importToArray(in_file)
    rules, my_ticket, nearby = parser(notes)
    result = sum_wrong(rules, nearby)
    # code here
    print("Result = {}".format(result))
    return result


def matches_rule(column, rule):
    all_match = True
    for value in column:
        if value not in range(rule[0][0], rule[0][1]+1) and value not in range(rule[1][0], rule[1][1]+1):
            all_match = False
    return all_match


def match_columns(rules, clean_nearby):
    matches = []
    for id, column in enumerate(list(zip(*clean_nearby))):
        print("Column {:2} matches Rules:".format(id))
        match = []
        for rule_id, rule in enumerate(rules):
            if matches_rule(column, rule):
                print("  -- Rule {:2}".format(rule_id))
                match.append("1")
            else:
                match.append("0")
        matches.append(deepcopy(match))
    pretty.print2DMap(matches)
    pretty.print2DMap(zip(*matches))



def print_rules(rules):
    for i in range(1000):
        print("{:4}: ".format(i), end="")
        for rule in rules:
            if i in range(rule[0][0], rule[0][1]+1) or i in range(rule[1][0], rule[1][1]+1):
                print("|", end="")
            else:
                print(" ", end="")
        print()


@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    notes = loadingUtils.importToArray(in_file)
    rules, my_ticket, nearby = parser(notes)
    #print_rules(rules)
    clean_nearby = cleanup(rules, nearby)
    print("before cleanup = {}; after cleanup {}".format(len(nearby), len(clean_nearby)))
    match_columns(rules, clean_nearby)
    # code here
    result = 97*163*101*73*53*131
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
