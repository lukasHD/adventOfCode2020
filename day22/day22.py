import sys
import inspect
from codetiming import Timer
sys.path.insert(0, 'D:\\projects\\aoc2020\\')
from helper import loadingUtils, pretty

DAY = 22
def get_path():
    return "day{:02d}".format(DAY)


def parse(in_arr):
    p1 = []
    p2 = []
    player1 = True
    for line in in_arr[1:]:
        if line == "":
            continue
        if "Player" in line:
            player1 = False
            continue
        try:
            a = int(line)
            if player1:
                p1.append(a)
            else:
                p2.append(a)
        except ValueError:
            raise ValueError("smthg went wrong")
    return p1, p2


def play(p1,p2, debug):
    step = 1
    while len(p1) > 0 and len(p2) > 0:
        if debug: print("Round {:3}".format(step))
        v1 = p1.pop(0)
        v2 = p2.pop(0)
        if v1 > v2: 
            if debug: print("Player 1 wins this round!")
            p1.append(v1)
            p1.append(v2)
        else:
            if debug: print("Player 2 wins this round!")
            p2.append(v2)
            p2.append(v1)
        step += 1
    if len(p1) == 0:
        return p2
    else:
        return p1


def play_advanced(_p1, _p2, debug):
    p1 = _p1.copy()
    p2 = _p2.copy()
    previous_rounds = []
    step = 1
    while len(p1) > 0 and len(p2) > 0:
        if debug: print("Round {:3}".format(step))
        #if debug: print(previous_rounds)
        """
        Before either player deals a card, if there was a previous round in this game that
        had exactly the same cards in the same order in the same players' decks, the game
        instantly ends in a win for player 1. Previous rounds from other games are not
        considered. (This prevents infinite games of Recursive Combat, which everyone agrees
        is a bad idea.)
        """
        hashed = str(p1) + ";" + str(p2)
        if hashed in previous_rounds:
            # declare P1 the winner
            if debug: print("Player 1 is declared the winner! Stop infinity!")
            return 1, p1 
        else:
            previous_rounds.append(hashed)
        """
        the players begin the round by each drawing the top card of their deck as normal.
        """
        v1 = p1.pop(0)
        v2 = p2.pop(0)
        """
        If both players have at least as many cards remaining in their deck as the value
        of the card they just drew, the winner of the round is determined by playing a new
        game of Recursive Combat (see below).
        Otherwise the winner of the round is the player with the higher-value card.
        """
        if len(p1) >= v1 and len(p2) >= v2:
            if debug: print("Recursive Combat")
            new_p1 = p1.copy()[:v1]
            new_p2 = p2.copy()[:v2]
            winner, _ = play_advanced(new_p1, new_p2, debug)
            #raise NotImplementedError
        else:
            if v1 > v2: 
                if debug: print("Player 1 wins this round!")
                winner = 1
            else:
                if debug: print("Player 2 wins this round!")
                winner = 2
        """
        As in regular Combat, the winner of the round (even if they won the round by winning
        a sub-game) takes the two cards dealt at the beginning of the round and places them on
        the bottom of their own deck (again so that the winner's card is above the other card).
        """
        if winner == 1:
            p1.append(v1)
            p1.append(v2)
        else:
            p2.append(v2)
            p2.append(v1)
    """
    If collecting cards by winning the round causes a player to have
    all of the cards, they win, and the game ends.
    """
    if len(p1) == 0:
        return 2, p2
    else:
        return 1, p1


@Timer()
def run_part_1(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 1, inspect.stack()[0].function, in_file)
    result = 0
    p1, p2 = parse(loadingUtils.importToArray(in_file))
    print(p1)
    print(p2)
    winner = play(p1,p2, debug)
    print(winner)
    winner.reverse()
    for i, v in enumerate(winner):
        result += (i+1) * v
    # code here
    print("Result = {}".format(result))
    return result

@Timer()
def run_part_2(in_file: str, debug: bool = False) -> int:
    pretty.printHeader(DAY, 2, inspect.stack()[0].function, in_file)
    result = 0
    p1, p2 = parse(loadingUtils.importToArray(in_file))
    _, winner = play_advanced(p1,p2, debug)
    print(winner)
    winner.reverse()
    for i, v in enumerate(winner):
        result += (i+1) * v
    # code here
    print("Result = {}".format(result))
    return result

if __name__ == "__main__":
    run_part_1(get_path() + "/test1", True)
    run_part_1(get_path() + "/input1")
    run_part_2(get_path() + "/test2", True)
    run_part_2(get_path() + "/test1", True)
    run_part_2(get_path() + "/input1")
