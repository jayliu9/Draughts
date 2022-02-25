'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for calculating the logarithem of a number to any base.
'''


def calculate_log(num, base):
    '''
        Function - calculate_log
            Calculates the logarithm of a number to any base
        Parameters:
            num -- The number to calculate. Assumes the number is a positive
            integer which is a power of the input of base
            base -- The base used to calculate the logarithm of a number
        Returns:
            The result of the logarithm of the number to any base
    '''
    LOOP_END = 1

    times = 0
    while num != LOOP_END:
        num /= base
        times += 1
    return times


def main():
    base = int(input("Enter a base: "))
    number = int(input("Enter a positive power of %d: " % base))
    result_of_log = calculate_log(number, base)
    print("log base %d of %d is %d" % (base, number, result_of_log))


if __name__ == "__main__":
    main()
