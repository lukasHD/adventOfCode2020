def printShit():
    print("This is shit from the helper library")

def return42():
    return 42

def importToArray(inFile):
    out = []
    with open(inFile) as lines:
        for line in lines:
            out.append(line.strip('\n'))
    return out

def importToIntArray(inFile):
    out = []
    with open(inFile) as lines:
        for line in lines:
            out.append(int(line.strip('\n')))
    return out


def importTo2DArray(in_file):
    out = []
    with open(in_file) as lines:
        for line in lines:
            out.append(list(line.strip("\n")))
    return out
