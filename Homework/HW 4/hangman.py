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


def letter_guess(letter, word):
    index = 0
    word_length = len(word)
    while index < word_length:
        if letter == word[index]:
            word = word[:index] + letter + word[index+1:]
    return word


def word_guess(guess, word):
    if guess == word:
        
