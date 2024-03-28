import random

class Hangman:
    """
    A class to represent a Hangman game.
    """
    
    def __init__(self, word_list, num_lives=5):
        """
        Initializes a new game instance.
        
        Parameters:
            word_list (list of str): The list of possible words.
            num_lives (int): The number of lives the player starts with.
        """
        self.word = random.choice(word_list).lower()
        self._initialize_word_guessed()
        self.num_unique_letters = len(set(self.word))
        self.num_lives = num_lives
        self.guesses = []

    def _initialize_word_guessed(self):
        """Initializes the word guessed list with underscores."""
        self.word_guessed = ['_' for _ in self.word]

    def play(self):
        """Starts the game and handles the main game loop."""
        while self.num_lives > 0 and self.num_unique_letters > 0:
            print(' '.join(self.word_guessed))
            self._ask_for_input()
        
        print("Congratulations, you won!" if self.num_unique_letters == 0 else f"You lost! The word was '{self.word}'.")

    def _ask_for_input(self):
        """Asks the player to guess a letter and processes the guess."""
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetical character.")
        elif guess in self.guesses:
            print("You've already guessed that letter.")
        else:
            self._process_guess(guess)

    def _process_guess(self, guess):
        """Processes the player's guess."""
        self.guesses.append(guess)
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            self._update_word_guessed(guess)
        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word. {self.num_lives} lives left.")

    def _update_word_guessed(self, guess):
        """Updates the word guessed list with the correctly guessed letter."""
        for index, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[index] = letter
        self.num_unique_letters -= 1

# Usage example:
words = ['apple', 'banana', 'cherry']
game = Hangman(words)
game.play()
