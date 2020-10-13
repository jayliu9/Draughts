'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is for implementing a version of the game Hangman. In this version,
the user will play three rounds against the computer.
'''


def hide_word(word):
    HIDE_CHARACTER = "_"
    word_length = len(word)
    return "_" * word_length


def letter_guess(letter, secret_word, hidden_word):
    index = 0
    word_length = len(secret_word)
    while index < word_length:
        if letter == secret_word[index]:
            hidden_word = hidden_word[:index] + letter + hidden_word[index+1:]
    return hidden_word


def word_guess(guess, secret_word):
    if guess == secret_word:
        return True
    return False


def is_repetition(guess, guessed_letter):
    index = 0
    str_length = len(guessed_letter)
    while index < str_length:
        if guess == guessed_letter[index]:
            return True
        index += 1
    return False


def guessed_so_far(previous_guess, guess):
    current_guess = previous_guess + guess
    return current_guess


def main():
    SECRET_WORDS = ["APPLE", "OBVIOUS", "XYLOPHONE"]
    MAXIMUM_GUESS_NUMBER = 6

    current_guesses = ""
    count_round = 1
    while count_round <= 3:
        count_guess = 1
        while count_guess <= MAXIMUM_GUESS_NUMBER:
            current_secret_word = SECRET_WORDS[count_round-1]
            hidden_word = hide_word(current_secret_word)
            print(hidden_word)
            user_guess = input("Enter a letter or word: ")
            is_letter = len(user_guess) == 1
            if is_letter:
                if is_repetition(user_guess, current_guesses):
                    print("You have already guessed that letter!")
                else:
                    hidden_word = letter_guess(user_guess, SECRET_WORD_1,
                                            hidden_word)
                    guessed_so_far(current_guesses, user_guess)
                    print("Your guess so far:", guessed_so_far)
            else:
                if word_guess(user_guess, current_secret_word):
                    print("You win!")

