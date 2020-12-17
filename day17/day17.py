import sys
import inspect
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 17
def get_path():
    return "day{:02d}".format(DAY)


def run1(start_map, steps):
    current_map = {}
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    min_z = 0
    max_z = 0

    def print_stack():
        for z in range(min_z, max_z+1):
            print("z = {}".format(z))
            for y in range(min_y, max_y+1):
                for x in range(min_x, max_y+1):
                    try:
                        a = current_map[(x,y,z)]
                    except KeyError:
                        a = "x"
                    print(a, end="")
                print()
            print()

    def get_value(x,y,z):
        try:
            value = current_map[(x,y,z)]
        except KeyError:
            value = "."
        return value

    for y, line in enumerate(start_map):
        for x, element in enumerate(line):
            current_map[(x,y,0)] = element
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    print_stack()
    for step in range(1, steps + 1):
        new_map = {}
        print("Run step {:2}".format(step))
        print("z = [{:3},{:3}]; y = [{:3},{:3}]; x = [{:3},{:3}]".format(
            min_z, max_z, min_y, max_y, min_x, max_x))
        for z in range(min_z-1, max_z+2):
            for y in range(min_y-1, max_y+2):
                for x in range(min_x-1, max_x+2):
                    value = get_value(x,y,z)
                    num_neighbours = 0
                    for nz in [z-1, z, z+1]:
                        for ny in [y-1, y, y+1]:
                            for nx in [x-1, x, x+1]:
                                if nz == z and ny == y and nx == x:
                                    continue
                                if get_value(nx, ny, nz) == "#":
                                    num_neighbours += 1
                    if value == "." and num_neighbours == 3:
                        new_map[(x,y,z)] = "#"
                    elif value == "#" and not (num_neighbours == 3 or num_neighbours == 2):
                        new_map[(x,y,z)] = "."
                    else:
                        new_map[(x,y,z)] = value
        min_x -= 1
        min_y -= 1
        min_z -= 1
        max_x += 1
        max_y += 1
        max_z += 1
        current_map = new_map.copy()
        print_stack()
    return current_map


def run2(start_map, steps):
    current_map = {}
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    min_z = 0
    max_z = 0
    min_w = 0
    max_w = 0

    def print_stack():
        for w in range(min_w, max_w+1):
            for z in range(min_z, max_z+1):
                print("z = {}, w = {}".format(z, w))
                for y in range(min_y, max_y+1):
                    for x in range(min_x, max_y+1):
                        try:
                            a = current_map[(x,y,z,w)]
                        except KeyError:
                            a = "x"
                        print(a, end="")
                    print()
                print()
            print()

    def get_value(x,y,z,w):
        try:
            value = current_map[(x,y,z,w)]
        except KeyError:
            value = "."
        return value

    for y, line in enumerate(start_map):
        for x, element in enumerate(line):
            current_map[(x,y,0,0)] = element
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)
    print_stack()
    for step in range(1, steps + 1):
    #for step in range(1,3):
        new_map = {}
        print("Run step {:2}".format(step))
        print("w = [{:3},{:3}]; z = [{:3},{:3}]; y = [{:3},{:3}]; x = [{:3},{:3}]".format(
            min_w, max_w, min_z, max_z, min_y, max_y, min_x, max_x))
        for w in range(min_w-1, max_w+2):
            for z in range(min_z-1, max_z+2):
                for y in range(min_y-1, max_y+2):
                    for x in range(min_x-1, max_x+2):
                        value = get_value(x,y,z,w)
                        #count = 0
                        num_neighbours = 0
                        for nw in [w-1, w, w+1]:
                            for nz in [z-1, z, z+1]:
                                for ny in [y-1, y, y+1]:
                                    for nx in [x-1, x, x+1]:
                                        if nz == z and ny == y and nx == x and nw == w:
                                            continue
                                        #count += 1
                                        if get_value(nx, ny, nz, nw) == "#":
                                            num_neighbours += 1
                        #print(count)
                        if value == "." and num_neighbours == 3:
                            new_map[(x,y,z,w)] = "#"
                        elif value == "#" and not (num_neighbours == 3 or num_neighbours == 2):
                            new_map[(x,y,z,w)] = "."
                        else:
                            new_map[(x,y,z,w)] = value
        min_x -= 1
        min_y -= 1
        min_z -= 1
        min_w -= 1
        max_x += 1
        max_y += 1
        max_z += 1
        max_w += 1
        current_map = new_map.copy()
        print_stack()
    return current_map


def count_map(final_map):
    count = 0
    for key, value in final_map.items():
        if value == "#":
            count += 1
    return count


@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    start_map = loadingUtils.importTo2DArray(in_file)
    final_map = run1(start_map, 6)
    result = count_map(final_map)
    # code here
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    start_map = loadingUtils.importTo2DArray(in_file)
    final_map = run2(start_map, 6)
    result = count_map(final_map)
    # code here
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
