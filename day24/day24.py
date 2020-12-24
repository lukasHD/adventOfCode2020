import sys
import inspect
from copy import deepcopy
from enum import Enum
from collections import defaultdict, Counter
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 24
def get_path():
    return "day{:02d}".format(DAY)


def parse(paths):
    out_path = []
    for path in paths:
        path_a = []
        #print(path)
        iterator = iter(path)
        done_looping = False
        while not done_looping:
            try:
                char = next(iterator)
                if char in "sn":
                    char += next(iterator)
                #print(char)
                path_a.append(char)
            except StopIteration:
                done_looping = True
        out_path.append(path_a)
        #print(path_a)
    return deepcopy(out_path)


def walk_path(path: list[str], debug: bool) -> tuple[int]:
    # x to the right 
    # y to the down
    x = 0
    y = 0
    if debug: print(" ".join(path))
    for step in path:
        if debug: print("({:2},{:2}) -> ".format(x,y), end="")
        if   step == "e":
            x += 1
        elif step == "w":
            x -= 1
        elif step == "ne":
            x += (0 if (y % 2 == 0) else 1)
            y -= 1
        elif step == "nw":
            x -= (1 if (y % 2 == 0) else 0)
            y -= 1
        elif step == "se":
            x += (0 if (y % 2 == 0) else 1)
            y += 1
        elif step == "sw":
            x -= (1 if (y % 2 == 0) else 0)
            y += 1
        else:
            raise ValueError("Unexpected direction for a hex-grid")
    if debug: print("({:2},{:2})".format(x,y))
    return (x,y)


class Color(Enum):
    WHITE = 0
    BLACK = 1

class Tile:
    def __init__(self) -> None:
        super().__init__()
        self.color = Color.WHITE

    def flip(self):
        if self.color == Color.WHITE:
            self.color = Color.BLACK
        elif self.color == Color.BLACK:
            self.color = Color.WHITE

    def __str__(self) -> str:
        return self.color.name

    def __repr__(self) -> str:
        return self.color.name

#    def __eq__(self, o: object) -> bool:
#        return super().__eq__(o)

    def print(self) -> str:
        return self.color.name

    def pr(self) -> str:
        if self.color == Color.WHITE:
            return "*"
        elif self.color == Color.BLACK:
            return "#"



def count_black(tiles: defaultdict(Tile)):
    return Counter([x.print() for x in tiles.values()])['BLACK']


def step(tiles):
    new_tiles = deepcopy(tiles)
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    for val in tiles.keys():
        x = val[0]
        y = val[1]
        x_min = min(x_min, x)
        x_max = max(x_max, x)
        y_min = min(y_min, y)
        y_max = max(y_max, y)
    #for idx in tiles:
    for _y in range(y_min-1, y_max+2):
        #print()
        for _x in range(x_min-1, x_max+2):
            idx = (_x, _y)
            value = tiles[idx].print()
            #print("{} is {}".format(idx, value), end="")
            cnt_black_neighbours = 0
            nl = []
            if idx[1] % 2 == 0:
                nl = [(1,0),(-1,0), (0,-1), (-1,-1), (0,1), (-1,1)]
            else:
                nl = [(1,0),(-1,0), (1,-1), (0,-1), (1,1), (0,1)]
            for d_idx in nl:
                x = idx[0] + d_idx[0]
                y = idx[1] + d_idx[1]
                #if (x,y) not in tiles:
                #    continue
                if tiles[(x,y)].print() == Color.BLACK.name:
                    cnt_black_neighbours += 1
            #print(" has {} black neighbours".format(cnt_black_neighbours), end='')
            if value == Color.BLACK.name and (cnt_black_neighbours == 0 or cnt_black_neighbours > 2):
                #print(" --> FLIP to WHITE")
                new_tiles[idx].flip()
            elif value == Color.WHITE.name and cnt_black_neighbours == 2:
                #print(" --> FLIP to BLACK")
                new_tiles[idx].flip()
            #else:
                #print()
    return new_tiles.copy()


def print_floor(tiles):
    x_min = 0
    x_max = 0
    y_min = 0
    y_max = 0
    for val in tiles.keys():
        x = val[0]
        y = val[1]
        x_min = min(x_min, x)
        y_min = min(y_min, y)
        x_max = max(x_max, x)
        y_max = max(y_max, y)
    for y in range(y_min-1, y_max+2):
        if y % 2 != 0: print(' ', end='')
        for x in range(x_min-1, x_max+2):
            if x == 0 and y == 0:
                print("O ", end='')
            else:
                print(tiles[(x,y)].pr(), end=" ")
        print()
    print()

@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    paths = parse(loadingUtils.importToArray(in_file))
    tiles = defaultdict(Tile)
    for path in paths:
        idx = walk_path(path, debug)
        if debug: print("gonna flip Tile {}: from {}".format(idx, tiles[idx]),end="")
        tiles[idx].flip()
        if debug: print(" to {}".format(tiles[idx]))
    print(tiles)
    result = Counter([x.print() for x in tiles.values()])['BLACK']
    print()
    # code here
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    paths = parse(loadingUtils.importToArray(in_file))
    tiles = defaultdict(Tile)
    for path in paths:
        idx = walk_path(path, False)
        if debug: print("gonna flip Tile {}: from {}".format(idx, tiles[idx]),end="")
        tiles[idx].flip()
        if debug: print(" to {}".format(tiles[idx]))
    print_floor(tiles)
    print(count_black(tiles))
    #tiles = step(tiles)
    #print_floor(tiles)
    #print(count_black(tiles))
    for i in range(1, 101):
    #for i in range(1, 5):
        tiles = step(tiles)
        #print_floor(tiles)
        print("Step {:3}: {}".format(i,count_black(tiles)))

    result = count_black(tiles)
    # code here
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    #walk_path(parse(["esenee"])[0], True)
    #walk_path(parse(["nwwswee"])[0], True)
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
