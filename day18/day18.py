import sys
import inspect
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 18
def get_path():
    return "day{:02d}".format(DAY)


# Copy from Barbara
def evaluate(in_str):
    left_el = 0
    right_el = 0
    brace_counter = 0
    op = None
    queue = []
    i = 0
    while i < len(in_str):
    #for i, char in enumerate(list(in_str)):
        char = in_str[i]
        # if char in ["(", ")"]:
        #     print("Brace", end="")
        # elif char in ["+", "*"]:
        #     print("Operator", end="")
        # elif char == " ":
        #     #print(char, end="")
        #     continue
        # else:
        #     val = int(char)
        #     print(val, end="")
        if char in "123456789":
            queue.append(int(char))
        if char in ["+", "*"]:
            op = char
        if char == "(":
            j = i + 1
            cnt = 1 # counts the braces
            while cnt:
                if in_str[j] == "(":
                    cnt += 1
                if in_str[j] == ")":
                    cnt -= 1
                if cnt == 0:
                    queue.append(evaluate(in_str[i+1: j]))
                    i=j
                    break
                j += 1
        if op is not None and (len(queue) == 2):
            a = queue.pop()
            b = queue.pop()
            if op == "+": queue.append(a+b)
            if op == "*": queue.append(a*b)
            op = None
        i += 1
    #print()
    assert len(queue) == 1
    return queue[0]


# Copy from Barbara
def transform(line):
    i = 0
    while i < len(line):
        if line[i] == "+":
            # enclose everything to the left in braces
            j = i - 1
            cnt = 0
            while j > 0:
                if line[j] == ")":
                    cnt += 1
                if line[j] == "(":
                    cnt -= 1
                if line[j] in "123456789(" and cnt == 0:
                    break
                j -= 1
            k = i + 1
            while k < len(line):
                #cnt == 0
                if line[k] == "(":
                    cnt += 1
                if line[k] == ")":
                    cnt -= 1
                if line[k] in "123456789)" and cnt == 0:
                    break
                k += 1
            line = line[:j] + "(" + line[j:k+1] + ")" + line[k+1:]
            i += 1
        i += 1
    return line


@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    eqns = loadingUtils.importToArray(in_file)
    for eqn in eqns:
        res = evaluate(eqn)
        print(res)
        result += res
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    eqns = loadingUtils.importToArray(in_file)
    for eqn in eqns:
        print(eqn)
        new_eqn = transform(eqn)
        print(new_eqn)
        res = evaluate(new_eqn)
        print(res)
        result += res
    # code here
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
