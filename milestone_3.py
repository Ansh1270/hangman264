import random

def check_guess(guess, word):
    """Check if the guessed letter is in the word and provide feedback."""
    if guess in word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

def ask_for_input(word):
    """Continuously ask for a valid single letter and check if it's in the word."""
    while True:
        guess = input("Please enter a single letter: ").lower()
        if len(guess) == 1 and guess.isalpha():
            check_guess(guess, word)
            break  # Exiting the loop after processing the guess
        else:
            print("Invalid letter. Please enter a single alphabetical character.")

# Choose a secret word from the list
word_list = ['apple', 'banana', 'cherry', 'date', 'fig']
secret_word = random.choice(word_list)

# Call the function to start the game
ask_for_input(secret_word)
