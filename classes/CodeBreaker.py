class CodeBreaker:
    def get_guess(self):
        return input("Color? ")

    def get_code_break_attempt(self, code_length, colors):

        i = 1
        attempt = []

        while i <= code_length:
            print()
            print("Position", str(i), "of", str(code_length))
            guess = self.get_guess()

            while guess not in colors:
                print("That's not one of the options, try again.")
                guess = self.get_guess()

            attempt.append(guess)
            i += 1

        return attempt
