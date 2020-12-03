from functools import reduce

def printHeader(day: int, part: int, fctname: str, fname:  str):
    lines = []
    lines.append("Day {} Part {}".format(day, part))
    lines.append("Function: {}".format(fctname))
    lines.append("Input Filename: {}".format(fname))
    # add decorator
    longestText = max(list(map(len, lines)))
    lines = [line + " "*(longestText - len(line)) for line in lines]
    decorator = "+"
    assert len(decorator) == 1
    buffer = 4
    lenDecorator = 2*len(decorator) + 2*buffer + longestText
    def printWrapedString(instr: str, buffer:int = 2):
        print(decorator + " "*buffer + instr + " "*buffer + decorator)
    def printLine(deco: str, length: int):
        print(deco*length)
    # Output finally
    print()
    printLine(decorator, lenDecorator)
    for line in lines:
        printWrapedString(line, buffer)
    printLine(decorator, lenDecorator)


def print2DArray(map_in):
    for line in map_in:
        print(line)


def print2DMap(map_in):
    print()
    for line in map_in:
        print("".join(line))
    print()
