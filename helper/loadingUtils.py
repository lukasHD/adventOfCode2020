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