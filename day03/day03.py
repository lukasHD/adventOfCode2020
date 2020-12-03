import sys
import inspect
import functools
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 3
def get_path():
    return "day{:02d}".format(DAY)


def get_path_traverse_diagonal(treemap, delta: (int, int) = (1,1), start_pos: (int, int) = (0,0)):
    within_bounds = True
    out_list = []
    x,y    = start_pos
    dx, dy = delta
    size_x = len(treemap)
    size_y = len(treemap[0])
    while within_bounds:
        try:
            # add current Position --- assumes we start within the bounds
            out_list.append(treemap[x][y])
            # do the next step
            x += dx
            y += dy
            # wrap around in y direction
            y = y%size_y
        except IndexError:
            #we are out of bounds
            within_bounds = False
    return out_list

@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    treemap = loadingUtils.importTo2DArray(in_file)
    if debug: pretty.print2DMap(treemap)
    path = get_path_traverse_diagonal(treemap, (1,3))
    result = len(list(filter(lambda x: x == "#", path)))
    print("I hit {} trees!".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    treemap = loadingUtils.importTo2DArray(in_file)
    if debug: pretty.print2DMap(treemap)
    list_of_directions = [(1,1),(1,3),(1,5),(1,7),(2,1)]
    number_of_trees_per_run = []
    for direction in list_of_directions:
        number_of_trees_per_run.append(len(list(filter(lambda x: x == "#",
                                                 get_path_traverse_diagonal(treemap, direction)))))
    print(number_of_trees_per_run)
    result = functools.reduce(lambda x,y: x*y, number_of_trees_per_run)
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
