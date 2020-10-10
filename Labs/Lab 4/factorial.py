'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for calculating the product of n and all the non-negative,
non-negative, non-zero integers below it.
'''


def calculate_factorial(num):
    '''
        Function - calculate_factorial
            Calculates the product of a number and all the non-negative,
            non-negative, non-zero integers below it.
        Parameters:
            num -- The number to calculate. Assumes the number is a positive
            integer
        Returns:
            The result of the product of the parameter and all the
            non-negative, non-negative, non-zero integers below it.
    '''
    END_OF_FACTORIAL = 1

    product = 1
    while num > END_OF_FACTORIAL:
        product *= num
        num -= 1
    return product


def main():
    user_in = int(input("Enter a positive integer: "))
    result_of_factorial = calculate_factorial(user_in)
    print("%d! = %d" % (user_in, result_of_factorial))


if __name__ == "__main__":
    main()
