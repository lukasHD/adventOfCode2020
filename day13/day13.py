import sys
import inspect
from codetiming import Timer
from sympy.ntheory.modular import solve_congruence
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 13
def get_path():
    return "day{:02d}".format(DAY)

def get_valid_busses(inlist):
    busses = inlist.split(",")
    out = []
    for bus in busses:
        if bus == "x":
            continue
        out.append(int(bus))
    return out


def next_to_airport(starttime, busses):
    initial_start = starttime
    while True:
        print(starttime, end=", ")
        for bus in busses:
            if starttime % bus == 0:
                print()
                return bus * (starttime - initial_start)
        starttime += 1


def find_congurence():
    """
    https://de.wikipedia.org/wiki/Chinesischer_Restsatz
    Eine simultane Kongruenz ganzer Zahlen ist ein System von linearen Kongruenzen
    x ≡ a1 ( mod m1 ) 
    x ≡ a2 ( mod m2 ) 
    ⋮ 
    x ≡ an ( mod mn ) 
    für die alle x bestimmt werden sollen, die sämtliche Kongruenzen gleichzeitig lösen. 
    Wenn eine Lösung x0 existiert, dann sind mit M := kgV ( m1, m2, m3, … , mn ) die Zahlen x0 + k*M ( k ∈ Z ) genau alle Lösungen. 
    Es kann aber auch sein, dass es gar keine Lösung gibt. 

    die mn-Werte sind hier die Perioden der Busse
    die Rest=Werte an sind die offsets am congurenz-punkt
    """
    return 0


@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    _starttime, _busses = loadingUtils.importToArray(in_file)
    starttime = int(_starttime)
    print(starttime)
    busses = get_valid_busses(_busses)
    print(busses)
    result = next_to_airport(starttime, busses)
    # code here
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    _starttime, _busses = loadingUtils.importToArray(in_file)
    starttime = int(_starttime)
    print(starttime)
    busses = []
    for i, bus in enumerate(_busses.split(",")):
        print(i, bus)
        if bus == "x":
            continue
        busses.append(((int(bus) - i)%int(bus), int(bus)))
    print(busses)
    solution = solve_congruence(*busses)
    print(solution)
    # code here
    result = solution[0]
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
