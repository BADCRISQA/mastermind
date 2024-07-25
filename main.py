import random

class Mastermind:
    def __init__(self, colors=["R", "G", "B", "Y", "O", "P"], code_length=4):
        self.colors = colors
        self.code_length = code_length
        self.code = self.generate_code()
        self.guesses = []
        self.feedback = []

    def generate_code(self):
        return [random.choice(self.colors) for _ in range(self.code_length)]

    def generate_feedback(self, guess):
        feedback = []
        code_copy = self.code[:]
        guess_copy = guess[:]

        for i in range(self.code_length):
            if guess_copy[i] == code_copy[i]:
                feedback.append("B")
                code_copy[i] = guess_copy[i] = None

        for i in range(self.code_length):
            if guess_copy[i] is not None and guess_copy[i] in code_copy:
                feedback.append("W")
                code_copy[code_copy.index(guess_copy[i])] = None

        feedback.sort(reverse=True)
        return feedback

    def make_guess(self, guess):
        if len(guess) != self.code_length:
            raise ValueError("Guess must be the same length as the code.")
        self.guesses.append(guess)
        self.feedback.append(self.generate_feedback(guess))
        return self.feedback[-1]
