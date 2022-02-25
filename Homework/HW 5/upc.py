'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is a function that takes a string as input and tells whether or not
the supplied string is a valid UPC.
'''


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
    DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    FACTOR = 10

    sum = 0
    user_in_len = len(user_in)
    if len(user_in) == 0:
        return False
    for i in range(user_in_len - 1, -1, -1):
        if user_in[i] not in DIGITS:
            return False
        current_position = (user_in_len - 1) - i
        if current_position % 2 == 0:
            sum += int(user_in[i])
        else:
            sum += int(user_in[i]) * ODD_POSITION_COEFFCIENT
    is_valid = sum % FACTOR == 0
    return is_valid
