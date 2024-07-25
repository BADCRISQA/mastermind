import random

class MastermindBoard:
    COLORS = ['R', 'G', 'B', 'Y', 'O', 'P']  # Red, Green, Blue, Yellow, Orange, Purple
    
    def __init__(self):
        self.code = self.generate_code()
        self.guesses = []
        self.feedbacks = []
        self.max_attempts = 10

    def generate_code(self):
        return [random.choice(self.COLORS) for _ in range(4)]

    def make_guess(self, guess):
        if len(guess) != 4 or not all(color in self.COLORS for color in guess):
            raise ValueError("Guess must be a list of 4 colors from: " + ", ".join(self.COLORS))
        
        self.guesses.append(guess)
        feedback = self.get_feedback(guess)
        self.feedbacks.append(feedback)
        
        return feedback
    
    def get_feedback(self, guess):
        black_pegs = 0
        white_pegs = 0
        code_copy = self.code[:]
        guess_copy = guess[:]

        # First pass: count black pegs and mark them
        for i in range(4):
            if guess[i] == code_copy[i]:
                black_pegs += 1
                code_copy[i] = guess_copy[i] = None
        
        # Second pass: count white pegs
        for i in range(4):
            if guess_copy[i] is not None and guess_copy[i] in code_copy:
                white_pegs += 1
                code_copy[code_copy.index(guess_copy[i])] = None
        
        return {'black': black_pegs, 'white': white_pegs}
    
    def is_solved(self):
        return any(feedback['black'] == 4 for feedback in self.feedbacks)

    def is_game_over(self):
        return self.is_solved() or len(self.guesses) >= self.max_attempts

    def print_board(self):
        for i, guess in enumerate(self.guesses):
            feedback = self.feedbacks[i]
            print(f"Guess {i+1}: {guess} -> Black Pegs: {feedback['black']}, White Pegs: {feedback['white']}")

    def reset_game(self):
        self.code = self.generate_code()
        self.guesses = []
        self.feedbacks = []

# Example usage:
if __name__ == "__main__":
    game = MastermindBoard()
    print("Secret code is set. Try to guess it!")

    while not game.is_game_over():
        guess = input("Enter your guess (e.g., RGYB): ").upper().strip()
        guess = list(guess)
        if len(guess) == 4 and all(c in MastermindBoard.COLORS for c in guess):
            feedback = game.make_guess(guess)
            game.print_board()
        else:
            print("Invalid guess. Please enter 4 colors from: R, G, B, Y, O, P")
        
        if game.is_solved():
            print("Congratulations! You've guessed the code!")
            break
    else:
        print("Game over! The correct code was:", game.code)
