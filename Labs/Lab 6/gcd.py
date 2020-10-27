'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is a function to determine the greatest common divisor (GCD) of two
non-zero positive integers.
'''


def get_gcd(num1, num2):
    '''
        Function -- get_gcd
            Computes the greatest common divisor (GCD) of two non-zero positive
            integers.
        Parameter:
            num1 -- A number to compute
            num2 -- A number to compute
        Returns:
            The greatest common divisor of two non-zero positive integers.
    '''
    if num2 == 0:
        return num1
    elif num1 == 0:
        return num2
    return get_gcd(num2, num1 % num2)
