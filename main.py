'''
    Master Mind game.
    Version 1.0
    October 19, 2020
    Julian Canepa
'''

import random

from classes.game_master import GameMaster
from classes.code_maker import CodeMaker
from classes.code_breaker import CodeBreaker

# Create game variables
rounds = 10
code_length = 4
colors = ["blue", "green", "red", "yellow"]


def get_game():
    # Enter the GameMaster
    return GameMaster(code_length, colors)


def get_code():
    # Get the CodeMaker's code
    return CodeMaker(code_length, colors).get_code()


def crack_code():
    # Let the CodeBreaker get to work
    return CodeBreaker().get_code_break_attempt(code_length, colors)


def main():

    # Set up the game
    code = CodeMaker(code_length, colors).get_code()
    game_master = get_game()
    current_round = 1

    # Start the game
    while current_round <= rounds:

        # Round gameplay
        game_master.announce_round(current_round, rounds)
        code_breaker_attempt = crack_code()
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
