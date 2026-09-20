# CodeAlpha Task 1 — Hangman Game

A beginner-friendly text-based Hangman game built with Python for the CodeAlpha Python Programming Internship.

## Objective

Build a console game where the player guesses a randomly selected word one letter at a time, with a maximum of 6 incorrect guesses.

## Features

- Uses 5 predefined words
- Randomly selects a secret word
- Accepts one-letter guesses
- Tracks guessed letters
- Limits incorrect guesses to 6
- Validates invalid and repeated input
- Displays win and game-over messages

## Concepts Used

- `random`
- `while` loop
- `for` loop
- `if-elif-else`
- strings
- lists and sets
- functions
- console input/output

## Project Structure

```text
CodeAlpha_HangmanGame/
├── README.md
├── main.py
├── requirements.txt
```

## How to Run

1. Install Python 3.x.
2. Open a terminal in this project folder.
3. Run:

```bash
python main.py
```

No third-party packages are required.

## Example

```text
===== HANGMAN GAME =====
Guess the word one letter at a time.
You have 6 incorrect guesses.

Word: _ _ _ _ _ _
Wrong guesses: 0/6
Enter a letter: p
Correct guess!
```

## Learning Outcome

This project strengthens Python fundamentals by combining functions, loops, collections, random selection, and input validation into one small application.

## Future Improvements

- Add difficulty levels
- Add more words
- Display ASCII hangman stages
- Track score and wins/losses

## Author

Abdul Rehman

## Internship

CodeAlpha — Python Programming Internship
