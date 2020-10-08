'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for calculating the logarithem base 2 based on user's input.
'''


def log_base_2(num):
    '''
        Function - log_base_2
            Calculates the logarithm base 2 of a number
        Parameters:
            num -- The number to calculate. Assumes the number is a positive
            integer which is a power of 2 
        Returns:
            The result of the logarithm base 2 of the parameter
    '''
    BASE = 2
    LOOP_END = 1

    times = 0
    while num != LOOP_END:
        num /= BASE
        times += 1
    return times


def main():
    user_in = int(input("Enter a positive power of 2: "))
    result_of_log = log_base_2(user_in)
    print(result_of_log)
    

if __name__ == "__main__":
    main()
