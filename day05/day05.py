import sys
import inspect
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 5
def get_path():
    return "day{:02d}".format(DAY)


def calc_row_column(in_str: str):
    separator = 7
    row = in_str[:separator]
    column = in_str[separator:]
    row_b = row.replace("F","0")
    row_b = row_b.replace("B","1")
    column_b = column.replace("R","1")
    column_b = column_b.replace("L","0")
    row_i = int(row_b, 2)
    col_i = int(column_b, 2)
    seatID = row_i * 8 + col_i
    #print("row {} column {} ==> row {} column {} ==> row {} seat {} seatID {}".format(row, column, row_b, column_b, row_i, col_i, seatID))
    return (row_i, col_i, seatID)

@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    boardingpasses = loadingUtils.importToArray(in_file)
    seatIDs = []
    for boardingpass in boardingpasses:
        (row_i, col_i, seatID) = calc_row_column(boardingpass)
        seatIDs.append(seatID)
    result = max(seatIDs)
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    boardingpasses = loadingUtils.importToArray(in_file)
    seatIDs = []
    for boardingpass in boardingpasses:
        (row_i, col_i, seatID) = calc_row_column(boardingpass)
        seatIDs.append(seatID)
    seatIDs.sort()
    print(seatIDs)
    minSeat = min(seatIDs)
    maxSeat = max(seatIDs)
    results = []
    for seat in range(minSeat, maxSeat):
        if seat in seatIDs: continue
        if seat+1 not in seatIDs: continue
        if seat-1 not in seatIDs: continue
        print(seat)
        results.append(seat)
    assert len(results) == 1
    result = results[0]
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    #run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    #run_part_2(get_path() + "/test2", True)
    run_part_2(get_path() + "/input1")
