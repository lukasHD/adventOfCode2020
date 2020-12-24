import day21 as day

INPUTFOLDER = day.get_path()

def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 5


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 1679


def test_part_2():
    result = day.run_part_2(INPUTFOLDER+"/test1")
    assert result == "mxmxvkd,sqjhc,fvjkl"


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input1")
    assert result == "lmxt,rggkbpj,mxf,gpxmf,nmtzlj,dlkxsxg,fvqg,dxzq"
