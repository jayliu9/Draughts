'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for figuring out how to split a restaurant bill and this code has
been refactored to follow the "one job per function" rule.
'''


def calculate_tip(bill_amount, tip_percentage):
    '''
        Function -- calculate_tip
            Calculates the amount of tip.
        Parameter:
            bill_amount - The amount of the bill.
            tip_percentage - The percentage everyone is willing to tip.
        Returns:
            The amount of tip.
    '''
    return bill_amount * tip_percentage


def total(bill_amount, tip_percentage):
    '''
        Function -- total
            Calculates the total amount of money that should be paid.
        Parameter:
            bill_amount -- The amount of the bill.
            tip_percentage - The percentage everyone is willing to tip.
        Returns:
            The total amount of the money that should be paid.
    '''
    tip_amount = calculate_tip(bill_amount, tip_percentage)
    return bill_amount + tip_amount


def split(total_amount, people_num):
    '''
        Function -- split
            Calculates the amount of money each person should pay.
        Parameter:
            total_amount -- The total amount of the money that should be paid.
            people_num -- The number of people in the group.
        Returns:
            The amount of money each person should pay.
    '''
    return total_amount / people_num


def main():
    bill_amount = float(input("How much was the bill? "))
    tip_percentage = float(input("Input the percentage " + "everyone " +
                                 "is willing to tip (between 0 and 1): "))
    num_of_people = int(input("Input the number of people your group: "))

    total_amount = total(bill_amount, tip_percentage)
    amount_for_user = split(total_amount, num_of_people)
    print("The amount each person should pay is ($):", amount_for_user)


if __name__ == "__main__":
    main()
