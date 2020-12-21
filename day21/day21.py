import sys
import inspect
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 21
def get_path():
    return "day{:02d}".format(DAY)


def parse_input(foodlist):
    list_ingredients = []
    list_allergens = []
    d = {} # a dict mapping allergens to possible ingredients
    for food in foodlist:
        _tmp = food[:-1].split(" (contains ")
        ingredients = _tmp[0].split(" ")
        allergens = _tmp[1].split(", ")
        for allergen in allergens:
            if allergen in d:
                d[allergen].intersection_update(ingredients)
            else:
                d[allergen] = set(ingredients)
        list_ingredients.append(ingredients)
        list_allergens.append(allergens)

    print(list_ingredients)
    print(list_allergens)
    assert len(list_ingredients) == len(list_allergens)
    print(d)
    return list_ingredients, list_allergens, d

# inspired by a solution on reddit
def solve(mapping):
    solution = []
    while True:
        if len(mapping) == 0:
            break
        for key, values in mapping.items():
            if len(values) == 1:
                v = values.pop()
                solution.append((key, v))
                mapping.pop(key)
                for vs in mapping.values():
                    vs.discard(v) # remove this from all other lists, since it is fixed
                break # start over
    return solution




@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    foodlist = loadingUtils.importToArray(in_file)
    list_ingredients, allergens, mapping = parse_input(foodlist)
    # all values of the values of the dict
    exclude = set(v for vs in mapping.values() for v in vs)
    print(exclude)
    result = 0
    for ingredients in list_ingredients:
        for ingredient in ingredients:
            result += ingredient not in exclude
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    foodlist = loadingUtils.importToArray(in_file)
    list_ingredients, allergens, mapping = parse_input(foodlist)
    solution = solve(mapping)
    print(solution)
    solution.sort()
    print(solution)
    result = ",".join([x[1] for x in solution])
    # code here
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
