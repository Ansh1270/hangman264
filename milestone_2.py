import random

def main():
    # Create a list of 5 favorite fruits
    word_list = ['apple', 'banana', 'cherry', 'date', 'fig']
    print("List of words:", word_list)

    # Select a random word from the list
    word = random.choice(word_list)
    print("Random word from the list:", word)

    # Continuously prompt for a letter until a valid guess is made
    while True:
        # Ask the user for a single letter
        guess = input("Please enter a single letter: ")

        # Validate the input
        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            break  # Exit the loop if the guess is valid
        else:
            print("Oops! That is not a valid input. Try again.")

if __name__ == "__main__":
    main()
