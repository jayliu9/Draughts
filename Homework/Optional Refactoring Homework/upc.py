'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is a function that takes a string as input and tells whether or not
the supplied string is a valid UPC.
'''


def contain_only_digits(user_in):
    '''
        Function -- contain_only_digits
            Checks whether or not the supplied string contains only digits.
        Parameter:
            user_in -- A string to consider.
        Returns:
            True if the supplied string contains only digits, False otherwise
    '''
    return user_in.isdigit()


def is_valid_upc(user_in):
    '''
        Function -- is_valid_upc
            Checks whether or not the supplied string is a valid UPC
        Parameter:
            user_in -- A string to consider.
        Returns:
            True if the supplied string is a valid UPC, False otherwise
    '''
    ODD_POSITION_COEFFCIENT = 3
    FACTOR = 10

    sum = 0
    user_in_len = len(user_in)
    if not contain_only_digits(user_in):
        return False
    for position in range(user_in_len):
        index = -position - 1
        if position % 2 == 0:
            sum += int(user_in[index])
        else:
            sum += int(user_in[index]) * ODD_POSITION_COEFFCIENT
    is_valid = sum % FACTOR == 0
    return is_valid
