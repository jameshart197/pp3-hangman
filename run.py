"""
When user arrives, pick random word and show in blanks (underscores; _ _ _ _)
Ask user to guess a letter
    Validate that user has entered one single letter
If the letter is in the word, show the letter in blanked word.
If the letter is not in the word, flag a 'Fail'
    User has a maximum number of 'Fails'
Inform the user:
    Maximum 'Fails'
    'Fails' remaining
    Letters guessed
    State of word (eg. A P P _ E)
Game is over when either:
    The user has guessed all the letters in the word
    OR the user has reached the maximum number of 'FAILS'
"""


def get_random_word():
    """
    Pick a random word from the list of random words and return it
    Returns:
        string: A random word.
    """

    return "Cherry"


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


def main():
    """
    Runs the game
    """
    print("Welcome to Hangman!")

    word = get_random_word()
    guessed_letters = []
    num_incorrect_guesses = 0
    MAX_INCORRECT_GUESSES = 3

    print_blanked_word(word, guessed_letters)

    while (num_incorrect_guesses < MAX_INCORRECT_GUESSES):

        user_guess = get_user_guess(guessed_letters)
        if (user_guess not in word):
            num_incorrect_guesses += 1

        guessed_letters.append(user_guess)

        print(guessed_letters)
        print_blanked_word(word, guessed_letters)


main()
