import day05 as day

INPUTFOLDER = day.get_path()


def test_conversion():
    (row, column, seatID) = day.calc_row_column("FBFBBFFRLR")
    assert row == 44
    assert column == 5
    assert seatID == 357


def test_conversion2():
    (row, column, seatID) = day.calc_row_column("BFFFBBFRRR")
    assert row == 70
    assert column == 7
    assert seatID == 567


def test_conversion3():
    (row, column, seatID) = day.calc_row_column("FFFBBBFRRR")
    assert row == 14
    assert column == 7
    assert seatID == 119


def test_conversion4():
    (row, column, seatID) = day.calc_row_column("BBFFBBFRLL")
    assert row == 102
    assert column == 4
    assert seatID == 820


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 806


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input1")
    assert result == 562
