import sys
import inspect
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 25
def get_path():
    return "day{:02d}".format(DAY)


def transform(subj_nr: int, loop_size: int) -> int:
    value = 1
    for i in range(loop_size):
        value = value * subj_nr
        value = value % 20201227
    return value


def crack_loopsize(pub_key: int, subj_nr: int = 7):
    MAX_TRIES = 50000
    for i in range(MAX_TRIES):
        if transform(subj_nr, i) == pub_key:
            return i
    raise RuntimeError("Could not crack the card ...")


def crack_loopsize_2(pub_key: int, subj_nr: int = 7):
    MAX_TRIES = 100000000
    value = 1
    for i in range(MAX_TRIES):
        value = value * subj_nr
        value = value % 20201227
        if value == pub_key:
            return i+1
    raise RuntimeError("Could not crack the card ...")


@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    pub_keys = loadingUtils.importToArray(in_file)
    door_pub = int(pub_keys[0])
    card_pub = int(pub_keys[1])
    print("Intercepted Public keys: door = {}; card = {}".format(door_pub, card_pub))
    door_secret = crack_loopsize_2(door_pub, 7)
    card_secret = crack_loopsize_2(card_pub, 7)
    print("Cracked secret loop number: door = {}; card = {}".format(door_secret, card_secret))
    door_encryption = transform(door_pub, card_secret)
    card_encryption = transform(card_pub, door_secret)
    print("Encyption Keys: door = {}; card = {}".format(door_encryption, card_encryption))
    assert door_encryption == card_encryption
    result = door_encryption
    # code here
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    # code here
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    #run_part_2(get_path() + "/test2", True)
    #run_part_2(get_path() + "/input2")
