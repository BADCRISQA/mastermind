import random

class Mastermind:
    def __init__(self, colors=["R", "G", "B", "Y", "O", "P"], code_length=4):
        self.colors = colors
        self.code_length = code_length
        self.code = self.generate_code
        self.guesses = []
        self.feedback = []

    def generate_code(self):
        return [random.choice(self.colors) for _ in range(self.code_length)]

    def make_guess(self, guess):
        if len(guess) != self.code_length:
            raise ValueError("Guess must be the same length as the code.")
        self.guesses.append(guess)
        self.feedback.append(self.generate_feedback(guess))
        return self.feedback[-1]
