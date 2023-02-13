"""
This is what the program does
"""

import random

MAX_INCORRECT_GUESSES = 5

# open words.txt and shuffle randomly
with open("words.txt", encoding="utf-8") as f:
    word_list = []
    word_list = f.read().splitlines()
    random.shuffle(word_list)


def get_random_word(index):
    """
    Pick a random word from the list of random words and return it
    Returns:
        string: A random word.
    """
    return word_list[index]


def print_blanked_word(word, guessed_letters):
    """
    Given a word, print it as underscores or blanks.
    If a letter has been guessed correctly, show it within the word.
    """

    blanked_word = ""

    for letter in word:
        if letter in guessed_letters:
            blanked_word += f" {letter}"
        else:
            blanked_word += " _"
    print(blanked_word)


def get_user_guess(guessed_letters):
    """
    Get a valid user guess
    Validations:
        Single letter
        Not already guessed

    Returns:
        string: a single letter
    """

    while True:
        user_guess = input("Guess a letter: ").strip().lower()

        if not user_guess.isalpha() or len(user_guess) > 1:
            print("Please enter a single letter.")
            continue

        if user_guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        break

    return user_guess


def print_list(mylist):
    """
    Takes a list and separates it with commas
    """
    separator = ", "
    print(separator.join(mylist).upper())


def double_line():
    """
    Prints a blank line
    """
    print("\n")


def letter_not_guessed(word, characters):
    """
    Defines number of characters not guessed and counts down to 0
    """
    count = 0
    for letter in word:
        if letter not in characters:
            count += 1
    return count


def run_game(word):
    """
    Runs the game
    """
    guessed_letters = []
    fail_count = 0

    print_blanked_word(word, guessed_letters)
    print(f"\nYou have {MAX_INCORRECT_GUESSES} guesses remaining")
    double_line()
    while (fail_count < MAX_INCORRECT_GUESSES) and (
        letter_not_guessed(word, guessed_letters) > 0
    ):

        user_guess = get_user_guess(guessed_letters)
        if user_guess not in word:
            fail_count += 1
            lives_remaining = MAX_INCORRECT_GUESSES - fail_count
            print(f"\n Incorrect Guess! Lives remaining = {lives_remaining}")

        guessed_letters.append(user_guess)
        double_line()
        print_list(guessed_letters)
        double_line()
        letter_not_guessed(word, guessed_letters)
        print_blanked_word(word, guessed_letters)
        double_line()

    if fail_count == MAX_INCORRECT_GUESSES:
        print(
            f"Game over, you ran out of guesses.\n \n The answer was {word} \n"
            )
    else:
        print(f"Victory, you guessed the word! \n \n The word was {word} \n")


def main():
    """
    Runs the game
    """
    print("Welcome to Hangman!")
    double_line()

    keep_playing = True
    current_index = 0
    while keep_playing:
        word = get_random_word(current_index).lower()
        run_game(word)
        play_again = (
            input(
                "Enter 'Y' to play again or anything else to exit:\n"
            ).strip().upper()
        )
        if play_again == "Y":
            current_index += 1
        else:
            keep_playing = False


if __name__ == "__main__":
    main()
