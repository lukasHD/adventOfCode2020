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

def import_multiline(in_file: str, separator: str = "empty Line", joinString: bool = True):
    out = []
    block = []
    if separator != "empty Line":
        raise ValueError('Not Implemented')
    with open(in_file) as lines:
        for line in lines:
            # print("Line")
            # print(list(line))
            if line == "\n":
                # print("########### Finished Block")
                # print(block)
                # print("###########")
                if joinString:
                    out.append(" ".join(block))
                else:
                    out.append(block)
                block = []
            else: 
                block.append(line.strip())
            # print(block)
        # append last block aswell
        # print(block)
        if joinString:
            out.append(" ".join(block))
        else:
            out.append(block)
    return out
