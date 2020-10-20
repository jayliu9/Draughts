'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is a function that takes a string and checks if it is a secure
password.
'''


def secure_password(user_in):
    '''
        Function -- secure_password
            Checks whether or not the supplied string is a secure password
        Parameter:
            user_in -- A string to consider.
        Returns:
            True if the supplied string is a secure password, False otherwise
    '''
    MINIMUM_LENGTH = 9
    MAXIMUM_LENGTH = 12
    LOWERCASE_LETTER = "abcdefghijklmnopqrstuvwxyz"
    UPPERCASE_LETTER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    DIGIT = "0123456789"
    SPECIAL_CHARACTER = "$#@!"
    MINIMUM_VALID_BOOL_SUM = 1

    is_valid_length = (len(user_in) >= MINIMUM_LENGTH and
                       len(user_in) <= MAXIMUM_LENGTH)
    if not is_valid_length:
        return False
    lowercase_bool_sum = 0
    uppercase_bool_sum = 0
    digit_bool_sum = 0
    special_character_bool_sum = 0
    requirements_bool_sum = 0
    for character in user_in:
        if character not in (LOWERCASE_LETTER + UPPERCASE_LETTER + DIGIT +
                             SPECIAL_CHARACTER):
            return False
        lowercase_bool_sum += character in LOWERCASE_LETTER
        uppercase_bool_sum += character in UPPERCASE_LETTER
        digit_bool_sum += character in DIGIT
        special_character_bool_sum += character in SPECIAL_CHARACTER
    requirement_bool_sum = ((lowercase_bool_sum >= MINIMUM_VALID_BOOL_SUM) +
                            (uppercase_bool_sum >= MINIMUM_VALID_BOOL_SUM) +
                            (digit_bool_sum >= MINIMUM_VALID_BOOL_SUM) +
                            (special_character_bool_sum >=
                             MINIMUM_VALID_BOOL_SUM))
    meet_requirements = requirement_bool_sum >= 3
    if meet_requirements:
        return True
    return False
