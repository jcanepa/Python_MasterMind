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

        # Winner winner chicken dinner
        if code == attempt:
            return True

        feedback = []

        # Check the attempt sequence for exact matches
        for index, peg in enumerate(attempt):

            if code[index] == peg:
                feedback.append("black")
                code[index] = ""

        # Then check remaining for any occurances
        for index, peg in enumerate(attempt):

            if peg in code:
                feedback.append("white")
                code[index] = ""

        # Output feedback
        print()
        print("Your code:")
        print(attempt)
        print()
        print("Results:")
        print(feedback)
        print()
        print("Remember, 'black' is a direct hit. 'white' indicates an occurance somewhere in the sequence.")
        print()

        # Return code_cracked
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
