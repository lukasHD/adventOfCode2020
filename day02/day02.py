import sys
sys.path.insert(0, 'D:\\projects\\aoc2020\\')

import inspect
from codetiming import Timer

from helper import loadingUtils, pretty

day = 2
def getPath():
    return "day{:02d}".format(day)


def validate_password_rules(password: str, 
                            min_number: int, 
                            max_number: int, 
                            test_char: str) -> bool:
    """
    Old Password Rules

    The password policy indicates the lowest and highest number of times a given letter must
    appear for the password to be valid. For example, '1-3 a' means that the password must contain
    'a' at least 1 time and at most 3 times.
    """
    string_array = list(password)
    number_matching_chars = len(list(filter(lambda char: char == test_char, string_array)))
    return number_matching_chars >= min_number and number_matching_chars <= max_number


def validate_password_rules2(password: str, 
                             min_number: int, 
                             max_number: int, 
                             test_char: str) -> bool:
    """
    New Password Rules

    Each policy actually describes two positions in the password, where 1 means the first
    character, 2 means the second character, and so on. (Be careful; Toboggan Corporate Policies
    have no concept of "index zero"!) Exactly one of these positions must contain the given letter.
    Other occurrences of the letter are irrelevant for the purposes of policy enforcement.
    """
    string_array = list(password)
    val1 = string_array[min_number-1]
    val2 = string_array[max_number-1]
    return (val1 == test_char) ^ (val2 == test_char)


def parseInput(password_line: str) -> (str, int, int, str):
    """
    Typical Input Line:
    1-3 a: abcde
    """
    # set types of variables
    password: str   = ""
    min_number: int = -1
    max_number: int = -1
    test_char: str  = ""
    # parse the line
    (rule, password) = password_line.split(": ")
    (allowed_range, test_char) = rule.split(" ")
    (min_number, max_number) = list(map(int, allowed_range.split("-")))
    # Assert the results
    assert min_number >= 0
    assert max_number >= 0
    assert max_number >= min_number
    assert len(test_char) == 1
    assert len(password) >= 0
    # print("{}-{} times {} required in password {}"
    #     .format(min_number, max_number, test_char, password))
    return (password, min_number, max_number, test_char)


@Timer()
def runPart1(inFile: str, debug: bool = False) -> int:
    pretty.printHeader(day, 1, inspect.stack()[0].function, inFile)
    result = 0
    passwords_list = loadingUtils.importToArray(inFile)
    results = []
    for password_line in passwords_list:
        (password, min_number, max_number, test_char) = parseInput(password_line)
        if validate_password_rules(password, min_number, max_number, test_char):
            results.append(password)
    result = len(results)
    print("We have found {} valid passwords.".format(result))
    return result

@Timer()
def runPart2(inFile: str, debug: bool = False) -> int:
    pretty.printHeader(day, 2, inspect.stack()[0].function, inFile)
    result = 0
    passwords_list = loadingUtils.importToArray(inFile)
    results = []
    for password_line in passwords_list:
        (password, min_number, max_number, test_char) = parseInput(password_line)
        if validate_password_rules2(password, min_number, max_number, test_char):
            results.append(password)
    result = len(results)
    print("We have found {} valid passwords.".format(result))
    return result

if __name__ == "__main__":
    runPart1(getPath() + "/test1", True)
    runPart1(getPath() + "/input1")
    runPart2(getPath() + "/test1", True)
    runPart2(getPath() + "/input1")