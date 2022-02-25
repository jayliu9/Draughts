'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code consists of functions to determine the greatest common divisor (GCD)
of non-zero positive integers.
'''


def get_gcd(num1, num2):
    '''
        Function -- get_gcd
            Computes the greatest common divisor (GCD) of two non-zero positive
            integers.
        Parameter:
            num1 -- A non-zero positive integer to compute
            num2 -- A non-zero positive integer to compute
        Returns:
            The greatest common divisor of two non-zero positive integers.
    '''
    if num2 == 0:
        return num1
    elif num1 == 0:
        return num2
    return get_gcd(num2, num1 % num2)


def get_n_gcd(numbers):
    '''
        Function -- get_n_gcd
            Computes the greatest common divisor (GCD) of n positive integers.
        Parameter:
            numbers -- A list of positive integers to compute
        Returns:
            The greatest common divisor of n positive integers.
    '''
    if len(numbers) == 1:
        return numbers[0]
    return get_gcd(numbers[0], get_n_gcd(numbers[1:]))
