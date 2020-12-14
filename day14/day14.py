import sys
import inspect
from codetiming import Timer
import copy
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 14
def get_path():
    return "day{:02d}".format(DAY)


def process_instructions(instructions):
    mask = []
    mem = {}
    for line in instructions:
        op, _val = line.split(" = ")
        if op == "mask":
            print(op + "   " + _val)
            mask = []
            for i, char in enumerate(list(_val)):
                if char == "X":
                    continue
                mask.append((i, int(char)))
            print(mask)
            continue
        val = "{:036b}".format(int(_val))
        print(op, val)
        new_val = list(val)
        for pos, override in mask:
            new_val[pos] = str(override)
        val = "".join(new_val)
        dest = int(op.split("[")[1].split("]")[0])
        print("{}      {}".format(dest, val))
        mem[dest] = int(val,2)
    return mem


def process_instructions2(instructions):
    mask = []
    mem = {}
    for line in instructions:
        op, _val = line.split(" = ")
        if op == "mask":
            #print(op + "   " + _val)
            mask = []
            for i, char in enumerate(list(_val)):
                if char == "0":
                    continue
                mask.append((i, char))
            #print(mask)
            continue
        addr = int(op.split("[")[1].split("]")[0])
        b_addr = "{:036b}".format(int(addr))
        #print("addr   {}".format(b_addr))
        new_addr = list(b_addr)
        for pos, override in mask:
            if override == "1":
                new_addr[pos] = override
        #print("addr1: "+"".join(new_addr))
        adresses = [new_addr]
        for pos, override in mask:
            if override == "X":
                new_addresses = []
                for address in adresses:
                    #print(address)
                    tmp1 = copy.deepcopy(address)
                    tmp2 = copy.deepcopy(address)
                    tmp1[pos] = "1"
                    tmp2[pos] = "0"
                    new_addresses.append(tmp1)
                    new_addresses.append(tmp2)
                adresses = copy.deepcopy(new_addresses)
        i_addresses = []
        for address in adresses:
            b_dest = "".join(address) 
            #print(b_dest)
            dest = int(b_dest)
            i_addresses.append(dest)
            mem[dest] = int(_val)
    return mem


def sum_memory(memory):
    _sum = 0
    for val in memory.values():
        _sum += val
    return _sum


@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    instructions = loadingUtils.importToArray(in_file)
    memory = process_instructions(instructions)
    result = sum_memory(memory)
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    instructions = loadingUtils.importToArray(in_file)
    memory = process_instructions2(instructions)
    result = sum_memory(memory)
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test2", True)
    run_part_2(get_path() + "/input1")
