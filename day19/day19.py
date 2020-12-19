import sys
import inspect
import re
from copy import deepcopy
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 19
def get_path():
    return "day{:02d}".format(DAY)


def split(lines):
    is_rule = True
    rules = {}
    messages = []
    for line in lines:
        if line == "":
            is_rule = False
            continue
        if is_rule:
            num, rule = line.split(": ")
            rules[num] = rule
        else:
            messages.append(line)
    return rules, messages


def convert(subrule, rules):
    new = ""
    for el in subrule.split(" "):
        if el == "|":
            new = new + "|"
            continue
        #print(rules[el])
        rule = rules[el]
        if rule[0] == "\"" and rule[2] == "\"":
            new = new + rule[1]
        else:
            new = new + "(?:" + convert(rules[el], rules) + ")"
    return deepcopy(new)


def generate_regex(rules):
    # start with rule 0 and go down
    #print(rules["0"].split(" "))
    regex = "^{}$".format(convert(rules["0"], rules))
    #regex = "^a((aa|bb)(ab|ba)|(ab|ba)(aa|bb))b$"
    return deepcopy(regex)


def transform(rules):
    new_rules = rules.copy()
    new_rules["8"]  = "42 | 42 8"
    new_rules["11"] = "42 31 | 42 11 31"
    rule_42 = convert("42", rules)
    rule_31 = convert("31", rules)
    print(rule_42)
    print(rule_31)
    return new_rules


def count_matches(regex, lines, debug):
    p = re.compile(regex)
    cnt = 0
    for line in lines:
        if p.match(line):
            if debug: print(line)
            cnt += 1
    return cnt


def gen_regex2(rules):
    rule_42 = convert("42", rules)
    rule_31 = convert("31", rules)
    print(rule_42)
    print(rule_31)
    regexp = "^(?:"
    max_recursion = 10
    for m in range(1,max_recursion+1):
        # (^(?:a){3,10}(?:b){1,2}$
        regexp += "(?:"
        # regexp = regexp + "a" + r"{" + str(m+1) + "," + str(max_recursion+1) + r"}"
        # regexp = regexp + "b" + r"{1," + str(m) + r"})|"
        regexp = regexp + rule_42 + r"{" + str(m+1) + "," + str(max_recursion+1) + r"}"
        regexp = regexp + rule_31 + r"{1," + str(m) + r"})|"
    regexp = regexp[:-1] + ")$"
    print(regexp)
    return regexp

@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    lines = loadingUtils.importToArray(in_file)
    rules, messages = split(lines)
    #print(rules)
    regexp = generate_regex(rules)
    print(regexp)
    #print(messages)
    result = count_matches(regexp, messages, debug)
    # code here
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    lines = loadingUtils.importToArray(in_file)
    rules, messages = split(lines)
    print(rules["8"])
    print(rules["11"])
    new_rules = transform(rules)
    print(new_rules["8"])
    print(new_rules["11"])
    max_len = 0
    for message in messages:
        max_len = max(max_len, len(message))
    print(max_len)
    regexp = gen_regex2(rules)
    #print(regexp)
    result = count_matches(regexp, messages, debug)
    # code here
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/test2")
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test2", True)
    run_part_2(get_path() + "/input1")
