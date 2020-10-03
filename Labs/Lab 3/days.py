'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for figuring out how many days there are until Friday.
'''
NUM_OF_FRIDAY = 5
DAYS_OF_WEEK = 7

def num_of_current_day(day):
    '''
        Function -- num_of_current_day
            Numbers the current day of the week.
        Parameter:
            day -- The current day of the week.
        Returns:
            The number of the current day of the week.
    '''
    if day == "M":
        current = 1
    elif day == "TU":
        current = 2
    elif day == "W":
        current = 3
    elif day == "TH":
        current = 4
    elif day == "F":
        current = 5
    elif day == "SA":
        current = 6
    else:
        current = 7
    return current


def before_or_on_friday(day):
    '''
        Function -- before_or_on_friday
            The number of days until Friday when the current day is before or
            on Friday.
        Parameter:
            day -- The current day of the week.
        Returns:
            The number of days until Friday.
    '''
    days_until_friday = NUM_OF_FRIDAY - num_of_current_day(day)
    return days_until_friday


def after_friday(day):
    '''
        Function -- after_friday
            The number of days until Friday when the current day is after
            Friday.
        Parameter:
            day -- The current day of the week.
        Returns:
            The number of days until Friday.
    '''
    days_until_friday = NUM_OF_FRIDAY - num_of_current_day(day) + DAYS_OF_WEEK
    return days_until_friday


def main():
    name = input("Please enter your name: ")
    print("Hello,", name)
    current_day = input("Please enter the current day " +
                        "(M, Tu, W, Th, F, Sa, Su): ").upper()
    if num_of_current_day(current_day) > NUM_OF_FRIDAY:
        days_until_friday = after_friday(current_day)
    else:
        days_until_friday = before_or_on_friday(current_day)
    print("The number of days until Friday is", days_until_friday)


if __name__ == "__main__":
    main()
