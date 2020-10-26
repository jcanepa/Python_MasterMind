'''
    Master Mind game.
    Version 1.0
    October 19, 2020
    Julian Canepa
'''

from classes.GameMaster import GameMaster
from classes.CodeMaker import CodeMaker
from classes.CodeBreaker import CodeBreaker

# game variables
colors = ["blue", "green", "red", "yellow"]
code_length = 4
rounds = 10
cheat_mode = True


def get_game():
    # enter the GameMaster
    return GameMaster(code_length, colors)


def get_new_code():
    # ask the CodeMaker for a new code
    return CodeMaker(code_length, colors).get_code()


def crack_code():
    # let CodeBreaker get to work
    return CodeBreaker().get_code_break_attempt(code_length, colors)


def main():

    # set up the game
    code = get_new_code()
    game_master = get_game()
    current_round = 1

    # cheat mode
    if(cheat_mode):
        print("The code is:", str(code))
        print()

    # start the game
    while current_round <= rounds:
        game_master.announce_round(current_round, rounds)

        # Round phase one: CodeBreaker attempts to crack the code
        code_breaker_attempt = crack_code()

        # Round phase two: CodeBreaker's code is tested
        code_cracked = game_master.compare_codes(
            code.copy(),
            code_breaker_attempt)

        # Output results of round
        if code_cracked:
            game_master.announce_victory(current_round)
            quit()
        else:
            print("Code break unsuccessful.")

        current_round += 1

    # CodeBreaker is out of rounds
    game_master.announce_defeat()
    quit()

main()
