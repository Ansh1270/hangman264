import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word = random.choice(word_list)
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = []
    
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = guess
            self.num_letters = len(set(self.word) - set(self.word_guessed))
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        while self.num_lives > 0 and self.num_letters > 0:
            print(' '.join(self.word_guessed))
            guess = input("Guess a letter: ").lower()
            if not guess.isalpha() or len(guess) != 1:
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)
        if self.num_lives <= 0:
            print("You lost the game.")
        else:
            print(f"Congratulations! You guessed the word: {self.word}")

# Example usage
word_list = ['apple', 'banana', 'cherry', 'date', 'fig']
game = Hangman(word_list)
game.ask_for_input()
