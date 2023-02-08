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


def main():
    """
    Runs the game
    """
    print("Welcome to Hangman!")

    word = get_random_word()
    guessed_letters = []

    print_blanked_word(word)


main()
