import random


def choose_word():
    words = ["python", "computer", "science", "program", "coding"]
    return random.choice(words)


def display_word(secret_word, guessed_letters):
    return " ".join(
        letter if letter in guessed_letters else "_"
        for letter in secret_word
    )


def play_game():
    secret_word = choose_word()
    guessed_letters = set()
    max_wrong_guesses = 6
    wrong_guesses = 0

    print("===== HANGMAN GAME =====")
    print("Guess the word one letter at a time.")
    print(f"You have {max_wrong_guesses} incorrect guesses.\n")

    while wrong_guesses < max_wrong_guesses:
        print("Word:", display_word(secret_word, guessed_letters))
        print(f"Wrong guesses: {wrong_guesses}/{max_wrong_guesses}")

        if all(letter in guessed_letters for letter in secret_word):
            print(f"\nCongratulations! You guessed the word: {secret_word}")
            return

        guess = input("Enter a letter: ").strip().lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one alphabetic letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Correct guess!\n")
        else:
            wrong_guesses += 1
            print("Incorrect guess!\n")

    print("Game Over!")
    print(f"The correct word was: {secret_word}")


if __name__ == "__main__":
    play_game()
