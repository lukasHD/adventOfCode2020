import day11 as day
from helper import loadingUtils

INPUTFOLDER = day.get_path()

def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 37


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 2178


def test_view_2():
    seatmap = loadingUtils.importTo2DArray(INPUTFOLDER+"/test2")
    print(seatmap[4][3])
    cnt = day.count_occupied_neighbours_in_sight(seatmap, 4, 3 )
    assert cnt == 8


def test_view_3():
    seatmap = loadingUtils.importTo2DArray(INPUTFOLDER+"/test3")
    print("aaaaaaaaa + " + str(seatmap[1][1]))
    cnt = day.count_occupied_neighbours_in_sight(seatmap, 1, 1 )
    assert cnt == 0


def test_view_4():
    seatmap = loadingUtils.importTo2DArray(INPUTFOLDER+"/test4")
    print("aaaaaaaaa + " + str(seatmap[3][3]))
    cnt = day.count_occupied_neighbours_in_sight(seatmap, 3, 3 )
    assert cnt == 0

def test_part_2():
    result = day.run_part_2(INPUTFOLDER+"/test1")
    assert result == 26


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input1")
    assert result == 1978
