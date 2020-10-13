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
    '''
        Function - hide_word
            Hides the secret words behind the underscore characters
        Parameters:
            word -- The secret word to hide
        Returns:
            The secret word replaced with underscore characters.
    '''
    HIDE_CHARACTER = "_"

    word_length = len(word)
    return HIDE_CHARACTER * word_length


def letter_guess(letter, secret_word, hidden_word):
    '''
        Function - letter_guess
            Checks if the letter the user enters is in the secret word and
            reveals the letter of the secret word hidden behind the underscore
            characters if this letter is in the secret word.
        Parameters:
            letter -- The letter the user guesses
            secret_word -- The secret word
            hidden_word -- The hidden secret word to reveal
        Returns:
            The hidden secret word with the letters revealed if these letters
            are the same as the user guesses
    '''
    index = 0
    word_length = len(secret_word)
    while index < word_length:
        if letter == secret_word[index]:
            hidden_word = hidden_word[:index] + letter + hidden_word[index+1:]
        index += 1
    return hidden_word


def word_guess(guess, secret_word):
    '''
        Function - word_guess
            Checks if the word the user enters matches the serect word
            (case-insensitive)
        Parameters:
            guess -- The word the user enters
            secret_word -- The secret word
        Returns:
            The boolean value of whether the word the user enters matches the
            secret word.
    '''
    if guess == secret_word:
        return True
    return False


def is_repetition(guess, guessed_letter):
    '''
        Function - is_repetition
            Checks if the word user enters matches the serect word
            (case-insensitive)
        Parameters:
            guess -- The word the user enters
            secret_word -- The secret word
        Returns:
            The boolean value of whether the word the user enters matches the
            secret word.
    '''
    index = 0
    str_length = len(guessed_letter)
    while index < str_length:
        if guess == guessed_letter[index]:
            return True
        index += 1
    return False


def guessed_so_far(previous_guess, guess):
    '''
        Function - guessed_so_far
            Keeps track of each letter the user has guesses so far in
            chronological order
        Parameters:
            previous_guess -- all the previous letter guesses from the users in
            chronological order
            guess -- The letter the user guesses this time
        Returns:
            all letters in chronological order which the user has guessed up to
            now
    '''
    current_guess = previous_guess + guess
    return current_guess


def main():
    SECRET_WORDS = ["APPLE", "OBVIOUS", "XYLOPHONE"]
    MAXIMUM_GUESS_NUMBER = 6
    TOTAL_ROUND = 3
    GUESSES_SO_FAR_PROMPT = "Your guesses so far:"

    count_round = 1
    num_of_win = 0
    while count_round <= TOTAL_ROUND:
        current_guesses = ""
        current_secret_word = SECRET_WORDS[count_round-1]
        count_guess = 1
        hidden_word = hide_word(current_secret_word)
        print(hidden_word)
        while count_guess <= MAXIMUM_GUESS_NUMBER:
            user_guess = input("Enter a letter or word: ").upper()
            is_letter = len(user_guess) == 1
            if is_letter:
                if is_repetition(user_guess, current_guesses):
                    print("You've already guessed that letter!")
                else:
                    if count_guess == MAXIMUM_GUESS_NUMBER:
                        print("You lose! The word was", current_secret_word)
                        break
                    hidden_word = letter_guess(user_guess, current_secret_word,
                                               hidden_word)
                    current_guesses = guessed_so_far(current_guesses,
                                                     user_guess)
                    count_guess += 1
            elif word_guess(user_guess, current_secret_word):
                print("You win!")
                num_of_win += 1
                break
            print(hidden_word)
            print(GUESSES_SO_FAR_PROMPT, current_guesses)
        count_round += 1
    print("You won", num_of_win, "out of 3")


if __name__ == "__main__":
    main()
