'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is a recursive function that checks if every string in a given list of
strings contains a vowel.
'''
VOWELS = ("a", "e", "i", "o", "u")


def vowelsearch(lst):
    '''
        Function -- vowelsearch
            Checks if every string in a given list of strings contain a vowel.
        Parameter:
            lst -- A list of strings
        Returns:
            True if every string in the list of strings contains a vowel, False
            otherwise.
    '''
    if len(lst) == 0:
        return False
    elif len(lst) == 1:
        return vowel_in_string(lst[0]) 
    return vowel_in_string(lst[0]) and vowel_in_string(lst[1:]) 


def vowel_in_string(word):
    '''
        Function -- vowel_in_string
            Checks if a string contains a vowel.
        Parameter:
            word -- A string to check
        Returns:
            True if the string contains a vowel, False otherwise.
    '''
    if len(word) == 0:
        return False
    return word[0] in VOWELS or vowel_in_string(word[1:])
