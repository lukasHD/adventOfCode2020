import sys
import inspect
import functools
import re
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 4
def get_path():
    return "day{:02d}".format(DAY)

def string_to_dict(line: str): 
    out = {}
    for field in line.split(" "):
        k, v = field.split(":")
        out[k] = v
    return out

def complete_passport(passport: str):
    required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    optional_fields = ["cid"]
    valid = False
    # str to dict also removes duplicate fields
    pass_dict = string_to_dict(passport)
    # print(passport)
    # print(pass_dict)
    number_of_required = functools.reduce(lambda x,y: x + (1 if y in pass_dict else 0), required_fields, 0)
    # print(number_of_required)
    if number_of_required == len(required_fields): 
        valid = True
    else: 
        return False
    # check optional fields
    return valid


def is_year(in_str: str):
    return bool(re.search("^\\d{4}$", in_str))

def validate_passport(passport: str):
    """
    Allowed Values:
    byr (Birth Year) - four digits; at least 1920 and at most 2002.
    iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    hgt (Height) - a number followed by either cm or in:
        If cm, the number must be at least 150 and at most 193.
        If in, the number must be at least 59 and at most 76.
    hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    pid (Passport ID) - a nine-digit number, including leading zeroes.
    cid (Country ID) - ignored, missing or not.
    """
    if not complete_passport(passport): 
        print("passport not complete")
        return False
    pass_dict = string_to_dict(passport)
    # validate byr
    byr_s = pass_dict["byr"]
    if not is_year(byr_s): 
        print("byr is no valid year")
        return False
    byr = int(byr_s)
    #print("byr = {}".format(byr))
    if byr < 1920 or byr > 2002: 
        print("byr not in range")
        return False
    # validate iyr
    iyr_s = pass_dict["iyr"]
    if not is_year(iyr_s): 
        print("iyr is no valid year")
        return False
    iyr = int(iyr_s)
    #print("iyr = {}".format(iyr))
    if iyr < 2010 or iyr > 2020: 
        print("byr not in range")
        return False
    # validate eyr
    eyr_s = pass_dict["eyr"]
    if not is_year(eyr_s): 
        print("eyr is no valid year")
        return False
    eyr = int(eyr_s)
    #print("eyr = {}".format(eyr))
    if eyr < 2020 or eyr > 2030: 
        print("eyr not in range")
        return False
    # validate hgt
    hgt_s = pass_dict["hgt"]
    match = re.search("^(\d{2,3})(cm|in)$", hgt_s)
    if not bool(match): 
        print("hgt no valid format")
        return False
    size = int(match.group(1))
    unit = match.group(2)
    #print("hgt = {} {}".format(size, unit))
    if unit == "cm":
        if size < 150 or size > 193: 
            print("Size not in Range")
            return False
    if unit == "in":
        if size < 59 or size > 76: 
            print("Size not in Range")
            return False
    # validate hcl
    hcl_s = pass_dict["hcl"]
    #print("hcl = {}".format(hcl_s))
    if not bool(re.search("^#[0-9a-f]{6}$",hcl_s )): 
        print("hcl no valid format")
        return False
    # validate ecl
    ecl_s = pass_dict["ecl"]
    #print("ecl = {}".format(ecl_s))
    if ecl_s not in [ "amb", "blu", "brn", "gry", "grn", "hzl", "oth"] : 
        print("ecl no valid value")
        return False
    # validate pid
    pid_s = pass_dict["pid"]
    #print("pid = {}".format(pid_s))
    if not bool(re.search("^[0-9]{9}$", pid_s)): 
        print("pid no valid format")
        return False
    return True

@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    passports = loadingUtils.import_multiline(in_file)
    if debug: pretty.print2DMap(passports)
    count = 0
    for passport in passports:
        if complete_passport(passport):
            count += 1

    # code here
    result = count
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    passports = loadingUtils.import_multiline(in_file)
    if debug: pretty.print2DMap(passports)
    count = 0
    for passport in passports:
        if validate_passport(passport):
            count += 1

    # code here
    result = count
    # code here
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
