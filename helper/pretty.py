def sayDayandPart(day: int, part: int, fctname: str, fname:  str):
    lines = []
    greeting1 = "Day {} Part {}".format(day, part)
    greeting2 = "Function: {}".format(fctname)
    greeting3 = "Input Filename: {}".format(fname)
    l1 = len(greeting1)
    l2 = len(greeting2)
    l3 = len(greeting3)
    longestText = max(l1, l2, l3)
    greeting1 += " "*(longestText - l1)
    greeting2 += " "*(longestText - l2)
    greeting3 += " "*(longestText - l3)
    lenDecorator = 6 + longestText
    decorator = "#"
    def wrapString(instr: str) -> str:
        return(decorator + "  " + instr + "  " + decorator)
    print()
    print(decorator*lenDecorator)
    print(wrapString(greeting1))
    print(wrapString(greeting2))
    print(wrapString(greeting3))
    print(decorator*lenDecorator)