import random

# List of 5 predefined words
words = ["python", "computer", "science", "program", "coding"]

# Randomly select one word
secret_word = random.choice(words)

# Store letters guessed by the player
guessed_letters = []

# Maximum incorrect guesses
max_wrong_guesses = 6
wrong_guesses = 0

print("===== HANGMAN GAME =====")
print("Guess the word one letter at a time!")
print("You can make only 6 incorrect guesses.\n")

# Game loop
while wrong_guesses < max_wrong_guesses:

    # Display the word with underscores
    displayed_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "

    print("Word:", displayed_word)
    print("Wrong guesses:", wrong_guesses, "/", max_wrong_guesses)
    print("Guessed letters:", guessed_letters)

    # Check if the player has guessed the complete word
    if all(letter in guessed_letters for letter in secret_word):
        print("\nCongratulations! You guessed the word:", secret_word)
        break

    # Ask the player for a guess
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    # Check whether the letter was already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    # Add the guess to the list
    guessed_letters.append(guess)

    # Check the guess
    if guess in secret_word:
        print("Correct guess!\n")
    else:
        wrong_guesses += 1
        print("Incorrect guess!\n")

# Game over
if wrong_guesses == max_wrong_guesses:
    print("Game Over!")
    print("The correct word was:", secret_word)
    
