'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for converting a binary number to its decimal equivalent.
'''

def convert_to_decimal(binary):
    '''
        Function - convert_to_decimal
            Converts a binary number to its decimal equivalent
        Parameters:
            binary -- A binary number
        Returns:
            The decimal equivalent of the binary number
    '''
    BASE = 2

    place = len(binary) - 1
    decimal_equivalent = 0
    for digit in binary:
        to_decimal = int(digit) * BASE ** place
        decimal_equivalent += to_decimal
        place -= 1
    return decimal_equivalent


def main():
    binary_num = input("Enter a binary number: ")
    decimal_num = convert_to_decimal(binary_num)
    print(binary_num, "base 2 is equal to", decimal_num, "base 10")


if __name__ == "__main__":
    main()
