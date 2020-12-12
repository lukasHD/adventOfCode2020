import sys
import inspect
import math
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 12
def get_path():
    return "day{:02d}".format(DAY)


def parse_nav_line(_navline):
    direction = _navline[0]
    distance  = int(_navline[1:])
    return (direction, distance)


#
# x is positive in E 
# y is positive in N
#
def get_next(_pos, _hdg, direction, distance):
    x,y = _pos
    hdg = _hdg
    if   direction == "F":
        # override direction wihh heading to contune in the direction we are facing
        direction = _hdg
    
    if   direction == "N":
        y += distance
    elif direction == "E":
        x += distance
    elif direction == "S":
        y -= distance
    elif direction == "W":
        x -= distance
    elif direction == "L":
        # turn left
        facing = ["N", "W", "S", "E"]
        steps = distance//90
        start_idx = facing.index(_hdg)
        next_idx = (start_idx+steps)%4
        hdg = facing[next_idx]
    elif direction == "R":
        # turn right
        facing = ["N", "E", "S", "W"]
        steps = distance//90
        start_idx = facing.index(_hdg)
        next_idx = (start_idx+steps)%4
        hdg = facing[next_idx]
    else:
        raise ValueError("Unexpected direction")
    return (x,y), hdg


def get_next_real(_pos, _nav, direction, distance):
    x,y = _pos
    nav_x, nav_y = _nav
    if   direction == "F":
        # move ship towards nav point
        x += distance*nav_x
        y += distance*nav_y
    elif direction == "N":
        nav_y += distance
    elif direction == "E":
        nav_x += distance
    elif direction == "S":
        nav_y -= distance
    elif direction == "W":
        nav_x -= distance
    elif direction == "L":
        # turn left
        ang = math.atan2(nav_y, nav_x)
        length = math.sqrt(nav_x**2 + nav_y**2)
        ang += math.radians(distance)
        nav_x = int(round(math.cos(ang) * length))
        nav_y = int(round(math.sin(ang) * length))
    elif direction == "R":
        # turn right
        #print("{}  {}".format(nav_x, nav_y))
        ang = math.atan2(nav_y, nav_x)
        length = math.sqrt(nav_x**2 + nav_y**2)
        ang -= math.radians(distance)
        nav_x = int(round(math.cos(ang) * length))
        nav_y = int(round(math.sin(ang) * length))
        #print("{}  {}".format(nav_x, nav_y))
    else:
        raise ValueError("Unexpected direction")
    return (x,y), (nav_x, nav_y)


def get_end_point(nav_lines):
    # we start at (0,0) facing East = 0 degree
    pos = (0,0)
    hdg = "E"
    for nav_str in nav_lines:
        direction, distance = parse_nav_line(nav_str)
        print("{} for {:4} steps".format(direction, distance), end=" ")
        pos, hdg = get_next(pos, hdg, direction, distance)
        print(" --> ({:3},{:3}) facing {}".format(pos[0], pos[1], hdg))
    return pos


def get_end_point_real(nav_lines):
    # we start at (0,0) facing East = 0 degree
    pos = (0,0)
    hdg = (10,1)
    for nav_str in nav_lines:
        direction, distance = parse_nav_line(nav_str)
        if direction == "F":
            print("Move ship to nav  for {:4} steps".format( distance), end=" ")
        else:
            print("Move nav_target {} for {:4} steps".format(direction, distance), end=" ")
        pos, hdg = get_next_real(pos, hdg, direction, distance)
        print(" --> ({:3},{:3}) relative nav_point {}".format(pos[0], pos[1], hdg))
    return pos



@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    nav_lines = loadingUtils.importToArray(in_file)
    print(nav_lines)
    goal = get_end_point(nav_lines)
    print("Endpoint {}".format(goal))
    result = abs(goal[0])+abs(goal[1])
    # code here
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    nav_instr = loadingUtils.importToArray(in_file)
    print(nav_instr)
    goal = get_end_point_real(nav_instr)
    print("Endpoint {}".format(goal))
    result = abs(goal[0])+abs(goal[1])
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/test2", True)
    run_part_2(get_path() + "/input1")
