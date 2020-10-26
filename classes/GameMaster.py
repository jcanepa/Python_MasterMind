class GameMaster:
    def __init__(self, code_length, colors):

        self.welcome(code_length, colors)

    def print_separator(self):

        print()
        print("*" * 30)
        print()

    def welcome(self, code_length, colors):

        print("Welcome to Master Mind")
        print("Can you crack the code maker's code?")
        print()

        print("Instructions:")
        print("Each round, select", code_length,
              "pegs, each a color of your choosing.")
        print("Available color options are:", colors)
        print()

        print("Results:")
        print("'black' is a direct hit.")
        print("'white' indicates an occurance somewhere in the sequence.")

    def compare_codes(self, code, attempt):

        if code == attempt:
            return True  # winner winner chicken dinner

        feedback = []

        # check the sequence for exact matches
        for index, peg in enumerate(attempt.copy()):

            if code[index] == peg:
                feedback.append("black")
                code[index] = ""

        # then check remaining for any occurances
        for index, peg in enumerate(attempt.copy()):

            if peg in code:
                feedback.append("white")
                code[index] = ""

        # output feedback
        print()
        print("Your code:")
        print(attempt)
        print()
        print("Results:")
        print(feedback)
        print(
            "...remember, 'black' is a direct hit. 'white' just indicates an occurance of your color somewhere in the sequence."
        )
        print()

        # code crack attempt unsuccessful
        return False

    def announce_round(self, current_round, rounds):

        self.print_separator()

        print("-" * 20)
        print("   Round", str(current_round), "of", rounds)
        print("-" * 20)

    def announce_victory(self, current_round):

        print()
        print("-" * 45)
        print()
        print("Code cracked. Nice work, master mind.")
        print("You achieved victory in", str(current_round), "rounds.")
        print()
        print("-" * 45)
        print()

    def announce_defeat(self):

        print()
        print("-" * 45)
        print()
        print("Too many failed attempts. You set off the silent alarm.")
        print("The police are en route!")
        print()
        print("-" * 45)
        print()
