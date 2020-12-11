import sys
import inspect
import copy
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 11
def get_path():
    return "day{:02d}".format(DAY)


def count_occupied_neighbours(seatmap, i, j ):
    neigh = [-1, 0, 1]
    count = 0
    for di in neigh:
        for dj in neigh:
            if di == 0 and dj == 0:
                continue
            if i+di < 0 or j+dj < 0:
                continue
            try:
                if seatmap[i+di][j+dj] == "#":
                    count += 1
            except IndexError:
                continue
    return count


def count_occupied_neighbours_in_sight(seatmap, i, j ):
    neigh = [-1, 0, 1]
    count = 0
    for di in neigh:
        for dj in neigh:
            if di == 0 and dj == 0:
                continue
            for multipl in range(1,50):
                row = i+(multipl*di)
                col = j+(multipl*dj)
                #check out of bounds
                if row < 0 or row > len(seatmap)-1:
                    break
                if col < 0 or col > len(seatmap[0])-1:
                    break
                # get seat
                seat = seatmap[row][col]
                #print("[{}][{}] = {}".format(row,col,seat))
                if seat == "#":
                    # found occupied seat
                    count += 1
                    break
                if seat== "L":
                    # found empty seat
                    break
    return count


def step(seatmap):
    new_map = copy.deepcopy(seatmap)
    for i,row in enumerate(seatmap):
        for j, seat in enumerate(row):
            #print("[{}][{}] = {}".format(i,j,seat))
            if seat == ".":
                continue
            occupied_neighbours = count_occupied_neighbours(seatmap,i,j)
            #print(occupied_neighbours)
            if seat == "L" and occupied_neighbours == 0:
                new_map[i][j] = "#"
                continue
            if seat == "#" and occupied_neighbours >= 4:
                new_map[i][j] = "L"
                continue
    return new_map


def step2(seatmap):
    new_map = copy.deepcopy(seatmap)
    for i,row in enumerate(seatmap):
        for j, seat in enumerate(row):
            #print("[{}][{}] = {}".format(i,j,seat))
            if seat == ".":
                continue
            occupied_neighbours = count_occupied_neighbours_in_sight(seatmap,i,j)
            #print(occupied_neighbours)
            if seat == "L" and occupied_neighbours == 0:
                new_map[i][j] = "#"
                continue
            if seat == "#" and occupied_neighbours >= 5:
                new_map[i][j] = "L"
                continue
    return new_map


def run_until_stable(_seatmap, max_iter = 100):
    seatmap = copy.deepcopy(_seatmap)

    for i in range(max_iter):
        print(i)
        old_seats = copy.deepcopy(seatmap)
        seatmap = copy.deepcopy(step(seatmap))
        #pretty.print2DMap(seatmap)
        #input()
        if old_seats == seatmap:
            pretty.print2DMap(seatmap)
            return sum(x.count("#") for x in seatmap)
    print("Did not converge")
    return 0


def run_until_stable2(_seatmap, max_iter = 100):
    seatmap = copy.deepcopy(_seatmap)

    for i in range(max_iter):
        print(i)
        old_seats = copy.deepcopy(seatmap)
        seatmap = copy.deepcopy(step2(seatmap))
        if old_seats == seatmap:
            pretty.print2DMap(seatmap)
            return sum(x.count("#") for x in seatmap)
    print("Did not converge")
    return 0


@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    seats = loadingUtils.importTo2DArray(in_file)
    result = run_until_stable(seats)
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    seats = loadingUtils.importTo2DArray(in_file)
    result = run_until_stable2(seats)
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
