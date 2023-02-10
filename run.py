import random

MAX_INCORRECT_GUESSES = 3

with open("words.txt") as f:
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
        user_guess = input("Guess a letter: ")

        if not user_guess.isalpha() or len(user_guess) > 1:
            print("Please enter a single letter.")
            continue

        if user_guess in guessed_letters:
            print("You have already guessed that letter.")
            continue

        break

    return user_guess


def characters_not_guessed(word, characters):
    """
    Defines number of characters not guessed and counts down to 0
    """
    count = 0
    for letter in word:
        if letter not in characters:
            count += 1
    return count


def run_game(word):
    guessed_letters = []
    num_incorrect_guesses = 0

    print_blanked_word(word, guessed_letters)

    while (num_incorrect_guesses < MAX_INCORRECT_GUESSES) and (characters_not_guessed(word, guessed_letters) > 0):

        user_guess = get_user_guess(guessed_letters)
        if user_guess not in word:
            num_incorrect_guesses += 1

        guessed_letters.append(user_guess)

        print(guessed_letters)
        characters_not_guessed(word, guessed_letters)
        print_blanked_word(word, guessed_letters)

    if num_incorrect_guesses == MAX_INCORRECT_GUESSES:
        print(f"Game over, you ran out of guesses.\n The answer was {word}")
    else:
        print(f"Victory, you guessed the word! The word was {word}")


def main():
    """
    Runs the game
    """
    print("Welcome to Hangman!")

    keep_playing = True
    current_index = 0
    while keep_playing:
        word = get_random_word(current_index)
        run_game(word)
        play_again = input("Enter 'Y' to play again or anything else to exit:\n").strip().upper()
        if play_again == "Y":
            current_index += 1
        else:
            keep_playing = False

main()
