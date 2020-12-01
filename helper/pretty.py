def sayDayandPart(day: int, part: int, fctname: str, fname:  str):
    greeting1 = "Day {} Part {}".format(day, part)
    greeting2 = "Function: {}".format(fctname)
    greeting3 = "Input Filename: {}".format(fname)
    lenDecorator = max(len(greeting1), len(greeting2), len(greeting3))
    decorator = "#"
    print(decorator*lenDecorator)
    print(decorator + "  " + greeting1)
    print(decorator + "  " + greeting2)
    print(decorator + "  " + greeting3)
    print(decorator*lenDecorator)