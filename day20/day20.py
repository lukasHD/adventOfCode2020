import sys
import inspect
from copy import deepcopy
from more_itertools import locate
import numpy as np
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 20
def get_path():
    return "day{:02d}".format(DAY)


class Tile():
    def __init__(self, _id, _content):
        #print("INIT")
        self.id = _id
        self.map = deepcopy(_content)
        self.is_edge = False
        self.is_side = False
        self.gen_edges()
        self.neighbours = []
        self.unique_sides = []

    def print(self):
        print("Tile ID: {}".format(self.id))
        for line in self.map:
            print("".join(line))

    def flip(self):
        self.map = np.flipud(self.map)

    def rot90(self):
        self.map = np.rot90(self.map)

    def rotflip(self):
        #print("rot90")
        yield self.rot90()
        #print("rot90")
        yield self.rot90()
        #print("rot90")
        yield self.rot90()
        #print("rot90")
        yield self.rot90()
        #print("flip")
        yield self.flip()
        #print("rot90")
        yield self.rot90()
        #print("rot90")
        yield self.rot90()
        #print("rot90")
        yield self.rot90()
        #print("rot90")
        yield self.rot90()
        raise ValueError("Rotated too much")

    def gen_edges(self):
        self.edges = []
        self.edges.append("".join(self.map[0]))
        self.edges.append("".join([row[-1] for row in self.map]))
        self.edges.append("".join(self.map[-1]))
        self.edges.append("".join([row[0] for row in self.map]))
        # self.flip()
        # self.edges.append("".join(self.map[0]))
        # self.edges.append("".join(self.map[-1]))
        # self.edges.append("".join([row[0] for row in self.map]))
        # self.edges.append("".join([row[-1] for row in self.map]))
        # self.flip()
    
    def upper(self):
        return "".join(self.map[0])

    def right(self):
        return "".join([row[-1] for row in self.map])

    def lower(self):
        return "".join(self.map[-1])

    def left(self):
        return "".join([row[0] for row in self.map])

    def get_inner(self):
        return [x[1:-1] for x in self.map[1:-1]] 


def reverse(inp: str) -> str:
    return inp[::-1]

def find_edges(tiles):
    all_edges = []
    for tile in tiles:
        for edge in tile.edges:
            all_edges.append(edge)
    print(all_edges)
    for i, tile in enumerate(tiles):
        print("~~~~~ {} ~~~~~ {} ~~~~~".format(tile.id, i))
        cnt_unique = 0
        poss_neighbours = []
        for edge in tile.edges:
            edge_ids = list(locate(all_edges, lambda x: x == edge or x == reverse(edge)))
            overlap = [x//4 for x in edge_ids]
            #print("{} --> {} --> {}".format(edge_ids, overlap, len(edge_ids)))
            if len(edge_ids) == 1:
                cnt_unique += 1
                tile.unique_sides.append(edge)
                tile.unique_sides.append(reverse(edge))
            for _id in overlap:
                if _id != i:
                    poss_neighbours.append(_id)
        print("Has {} uniqe edges.".format(cnt_unique))
        if cnt_unique == 1:
            tile.is_side = True
        if cnt_unique == 2:
            tile.is_edge = True
        print("Possible Neighbours: {}".format(poss_neighbours))
        tile.neighbours = poss_neighbours.copy()


def get_max(pos):
    max_x = 0
    max_y = 0
    for x,y in pos.keys():
        max_x = max(max_x, x)
        max_y = max(max_y, y)
    return max_x, max_y



def assemble_image(tiles):
    stack = list(range(len(tiles)))
    fixed = []
    pos = {} # array of positions 
    x = 0 
    y = 0
    print(stack)
    # get a starting Point (i.e. a edge)
    start = -1
    for i, tile in enumerate(tiles):
        if tile.is_edge:
            start = i
            break
    print("pick id = {} as start".format(start))
    stack.remove(start)
    fixed.append(start)
    pos[(x,y)] = start
    # rotate start so that left and up are unique
    start_tile = tiles[start]
    start_tile.flip() # so we can compare to the example
    _i = 0
    while not (start_tile.upper() in start_tile.unique_sides and start_tile.left() in start_tile.unique_sides):
        print("rot90")
        start_tile.rot90()
        _i += 1
        if _i % 5 == 0:
            print("flip")
            start_tile.flip()
        print("{} {} =?= {}".format(start_tile.upper(), start_tile.left(), start_tile.unique_sides))
    start_tile.print()
    # find right neighbours until we reach the edge
    current_tile_id = start
    current_tile    = start_tile
    while True:
        print(stack)
        print(pos)
        for next_id in current_tile.neighbours:
            if next_id in fixed:
                # skip neighbours that are already placed
                continue
            print("Try to place neighbour {}".format(next_id))
            next_tile = tiles[next_id]
            generator = next_tile.rotflip()
            while True:
                generator.__next__()
                if next_tile.left() == current_tile.right():
                    print("Found right neighbour")
                    pos[(x+1,y)] = next_id
                    stack.remove(next_id)
                    fixed.append(next_id)
                    break
                if next_tile.upper() == current_tile.lower():
                    print("Found lower neighbour")
                    pos[(x,y+1)] = next_id
                    stack.remove(next_id)
                    fixed.append(next_id)
                    break
        x = x + 1
        if current_tile.right() in current_tile.unique_sides:
            y += 1
            x = 0
            if current_tile.lower() in current_tile.unique_sides:
                assert len(stack) == 0
                break
        current_tile_id = pos[(x,y)]
        current_tile = tiles[current_tile_id]
    print(stack)
    print(pos)
    max_x, max_y = get_max(pos)
    print(max_x, max_y)
    print()
    a = []
    for y in range(max_y+1):
        line_a = []
        for x in range(max_x+1):
            print("{}".format(tiles[pos[(x,y)]].id), end=' ')
            line_a.append(tiles[pos[(x,y)]].get_inner())
        line = np.concatenate(line_a, axis=1)
        a.append(line)
        print()
        #pretty.print2DMap(line)
    full_map = np.concatenate(a, axis=0)
    pretty.print2DMap(full_map)
    return deepcopy(full_map)


def rot(t):
    for i in range(4):
        yield np.rot90(t, i)

def fliprot(t):
    yield from rot(t)
    yield from rot(np.flip(t,1))


def remove_monsters(image):
    monster_str = ""
    monster_str += "                  # \n"
    monster_str += "#    ##    ##    ###\n"
    monster_str += " #  #  #  #  #  #   "
    print(monster_str)
    monster_arr = [list(x) for x in monster_str.split("\n")]
    pretty.print2DArray(monster_arr)
    monster2 = []
    for x, l in enumerate(monster_arr):
        for y, v in enumerate(l):
            if v == "#":
                monster2.append((x,y))
    print(monster2)
    monster = []
    for idx, v in np.ndenumerate(monster_arr):
        if v == "#":
            monster.append(idx)
    print(monster)
    # for all rotations and flips
    for image in fliprot(image):
        print("Flip rot")
        pretty.print2DMap(image)
        monster_cnt = 0
        for idx, value in np.ndenumerate(image):
            #print(idx, value)
            matches_monster = True
            for m_idx in monster:
                try:
                    if image[tuple(np.add(idx,m_idx))] != "#":
                        matches_monster = False
                        break
                except IndexError:
                    matches_monster = False
                    break
            if matches_monster:
                print("found a monster starting at {}!".format(idx))
                monster_cnt += 1
                # replace # with O
                for m_idx in monster:
                    image[tuple(np.add(idx,m_idx))] = "O"
        print("Found {:2} monsters in this flip-rot".format(monster_cnt))
        if monster_cnt > 0:
            pretty.print2DMap(image)
            result = 0
            for idx, value in np.ndenumerate(image):
                if value == "#":
                    result += 1
            return result


@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    in_text = loadingUtils.importToArray(in_file)
    tile_id = 0
    tile_content = []
    tile_counter = 0
    tiles = []
    for line in in_text:
        if line == "":
            tiles.append(Tile(tile_id, tile_content))
            tile_id = 0
            tile_content = []
            continue
        if "Tile" in line:
            tile_id = int(line.split(" ")[1][:-1])
            tile_counter += 1
        else:
            tile_content.append(list(line))
    tiles.append(Tile(tile_id, tile_content))
    print("We have {} Tiles".format(tile_counter))
    print(len(tiles))
    assert len(tiles) == tile_counter
    for tile in tiles:
        print()
        tile.print()
        print(tile.edges)
    find_edges(tiles)
    result = 1
    for tile in tiles:
        if tile.is_edge:
            result = result * tile.id
    # code here
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    in_text = loadingUtils.importToArray(in_file)
    tile_id = 0
    tile_content = []
    tile_counter = 0
    tiles = []
    for line in in_text:
        if line == "":
            tiles.append(Tile(tile_id, tile_content))
            tile_id = 0
            tile_content = []
            continue
        if "Tile" in line:
            tile_id = int(line.split(" ")[1][:-1])
            tile_counter += 1
        else:
            tile_content.append(list(line))
    tiles.append(Tile(tile_id, tile_content))
    print("We have {} Tiles".format(tile_counter))
    print(len(tiles))
    assert len(tiles) == tile_counter
    for tile in tiles:
        print()
        tile.print()
        print(tile.edges)
    find_edges(tiles)
    print("Start Assembling Image")
    image = assemble_image(tiles)
    # now remove all monsters
    result = remove_monsters(image)
    # code here
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
