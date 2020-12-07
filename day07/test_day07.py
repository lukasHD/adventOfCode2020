import day07 as day

INPUTFOLDER = day.get_path()


def test_color_1():
    q = "qual"
    n = "name"
    a = day.Color(q+" "+n)
    assert a.get_name() == n
    assert a.get_qualifyer() == q
    assert a.get_color() == q+" "+n

def test_color_2():
    q = "qual"
    n = "name"
    q2 = "q2"
    n2 = "n2"
    a = day.Color(q+" "+n)
    b = day.Color(q+" "+n)
    c = day.Color(q2+" "+n)
    d = day.Color(q+" "+n2)
    e = day.Color(q2+" "+n2)
    assert a == b 
    assert a != c
    assert a != d
    assert a != e


def test_color_dict():
    mydict = {}
    q = "qual"
    n = "name"
    q2 = "q2"
    n2 = "n2"
    a = day.Color(q+" "+n)
    b = day.Color(q+" "+n)
    c = day.Color(q2+" "+n)
    d = day.Color(q+" "+n2)
    e = day.Color(q2+" "+n2)
    mydict[a] = c
    assert mydict[a] == c
    assert mydict[b] == c
    mydict[c] = d
    assert mydict[c] == d


def test_part_1():
    result = day.run_part_1(INPUTFOLDER+"/test1")
    assert result == 4


def test_part_1_real():
    result = day.run_part_1(INPUTFOLDER+"/input1")
    assert result == 226


def test_part_2_1():
    result = day.run_part_2(INPUTFOLDER+"/test1")
    assert result == 32


def test_part_2_2():
    result = day.run_part_2(INPUTFOLDER+"/test2")
    assert result == 126


def test_part_2_real():
    result = day.run_part_2(INPUTFOLDER+"/input1")
    assert result == 0
