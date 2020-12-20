def rotflip():
    yield "rot1"
    yield "rot2"
    yield "rot3"
    yield "rot4"
    yield "flip"
    yield "rot1"
    yield "rot2"
    yield "rot3"
    yield "rot4"
    raise ValueError("aaaaa")

i = 0
#for i,a in enumerate(rotflip()):
a_gen = rotflip()
while True:
    a = a_gen.__next__()
    print(a)
    i += 1
    if i == 6:
        break
