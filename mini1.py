import random

# Word list
WORDS = [
    "python", "hangman", "programming", "computer", "keyboard",
    "developer", "function", "variable", "algorithm", "database",
    "internet", "software", "hardware", "network", "terminal"
]

# Hangman stages (0 = no body, 6 = full hangman)
STAGES = [
    # Stage 0
    """
  -----
  |   |
      |
      |
      |
      |
=========
""",
    # Stage 1
    """
  -----
  |   |
  O   |
      |
      |
      |
=========
""",
    # Stage 2
    """
  -----
  |   |
  O   |
  |   |
      |
      |
=========
""",
    # Stage 3
    """
  -----
  |   |
  O   |
 /|   |
      |
      |
=========
""",
    # Stage 4
    """
  -----
  |   |
  O   |
 /|\\  |
      |
      |
=========
""",
    # Stage 5
    """
  -----
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
""",
    # Stage 6
    """
  -----
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
"""
]


def get_random_word():
    return random.choice(WORDS)


def display_word(word, guessed_letters):
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def hangman():
    print("\n" + "="*40)
    print("       Welcome to HANGMAN!")
    print("="*40)

    word = get_random_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = 6

    print(f"\nThe word has {len(word)} letters. Good luck!\n")

    while wrong_guesses < max_wrong:
        # Display current hangman stage
        print(STAGES[wrong_guesses])

        # Display current word state
        current_display = display_word(word, guessed_letters)
        print(f"Word: {current_display}")

        # Check if player has won
        if "_" not in current_display:
            print("\n🎉 Congratulations! You guessed the word:", word.upper())
            print("You WIN!\n")
            break

        # Show guessed letters if any
        if guessed_letters:
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

        print(f"Attempts left: {max_wrong - wrong_guesses}")

        # Get player input
        guess = input("\nEnter a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️  Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"⚠️  You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.")
        else:
            wrong_guesses += 1
            remaining = max_wrong - wrong_guesses
            print(f"❌ Wrong guess! '{guess}' is not in the word. Attempts left: {remaining}")

    else:
        # Player lost
        print(STAGES[max_wrong])
        print(f"\n💀 Game Over! You ran out of attempts.")
        print(f"The word was: {word.upper()}\n")

    # Ask to play again
    play_again = input("Play again? (yes/no): ").lower().strip()
    if play_again in ("yes", "y"):
        hangman()
    else:
        print("\nThanks for playing Hangman! Goodbye! 👋\n")


if __name__ == "__main__":
    hangman()