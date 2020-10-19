'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is a function that takes a string as input and determines whether or
not the supplied string is a valid UPC.
'''


def is_valid_upc(upc):
    ODD_POSITION_COEFFCIENT = 3
    DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    FACTOR = 10

    sum = 0
    len_of_upc = len(upc)
    if len(upc) == 0:
        return False
    for i in range(len_of_upc - 1, -1, -1):
        if upc[i] not in DIGITS:
            return False
        current_position = (len_of_upc - 1) - i
        if current_position % 2 == 0:
            sum += int(upc[i])
        else:
            sum += int(upc[i]) * ODD_POSITION_COEFFCIENT
    is_valid = sum % FACTOR == 0
    return is_valid
