'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code consists of functions refactored from previous labs which replace
iteration with recursion.
'''
num_of_division = 0


def logarithm(num):
    '''
        Function -- logarithm
            Calculates the logarithm base 2.
        Parameter:
            num -- The number to calculate. Assumes the number is a positive
            integer which is a power of 2
        Returns:
            The result of the log base 2 of the parameter
    '''
    LOG_BASE = 2

    if num // LOG_BASE == 0:
        return num_of_division
    num_of_division += 1
    return logarithm(num / LOG_BASE)


def binary_to_decimal(binary):
    '''
        Function - binary_to_decimal
            Converts a binary string to its decimal equivalent
        Parameters:
            binary -- A binary string
        Returns:
            The decimal equivalent of the binary string
    '''
    BASE = 2

    if len(binary) == 1:
        return int(binary)
    return BASE * binary_to_decimal(binary[:-1]) + int(binary[-1])
