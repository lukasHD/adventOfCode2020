import sys
import inspect
from codetiming import Timer
from tqdm import tqdm
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 23
def get_path():
    return "day{:02d}".format(DAY)


# Copy from Reddit
class CrabCups():
    def __init__(self, cups):
        self.current = cups[0]
        self.next_cup = {}
        for i, c in enumerate(cups, 1):
            try:
                self.next_cup[c] = cups[i]
            except IndexError:
                self.next_cup[c] = cups[0]

    def __iter__(self):
        return self

    def __next__(self):
        remove = []
        to_move = self.current
        for i in range(3):
            remove.append(self.next_cup[to_move])
            to_move = self.next_cup[to_move]
        self.next_cup[self.current] = self.next_cup[remove[2]]
        destination = self.current - 1
        while destination <= 0 or destination in remove:
            if destination == 0:
                destination = len(self.next_cup)
            if destination in remove:
                destination -= 1
        self.next_cup[destination], self.next_cup[remove[2]] = (
            remove[0],
            self.next_cup[destination],
        )
        self.current = self.next_cup[self.current]
    
    @property
    def final(self):
        current = 1
        output = []
        for _ in range(len(self.next_cup) - 1):
            output.append(self.next_cup[current])
            current = self.next_cup[current]
        output = [str(n) for n in output]
        return "".join(output)


def run_a(cups):
    cc = CrabCups(cups)
    for _ in range(100):
        next(cc)
    return cc.final


def run_b(cups):
    cups.extend(range(10, 1000001))
    cc = CrabCups(cups)
    for i in tqdm(range(10000000)):
        next(cc)
    a = cc.next_cup[1]
    b = cc.next_cup[a]
    return a * b


@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    cups = list(map(int, list(loadingUtils.importToArray(in_file)[0])))
    print(cups)
    result = run_a(cups)
    # code here
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    cups = list(map(int, list(loadingUtils.importToArray(in_file)[0])))
    print(cups)
    result = run_b(cups)
    # code here
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
