'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is for calculating business trip driving expenses.
'''


def calculate_mileage(start, end):
    '''
        Function -- calculate_mileage
            Calculates miles driven using the start and end odometer values.
        Parameters:
            start -- The odometer reading at the start of the trip. Expecting a
            number greater than 0
            end -- The odometer reading at the end of the trip. Expecting a
            number greater than 0 and greater than the start value.
        Returns:
            The miles driven, a number. If either parameter is invalid (e.g.
            either parameter is negative or end is less than start), returns 0.
    '''
    is_start_valid = start > 0
    is_end_valid = end > 0 and end > start

    if is_start_valid and is_end_valid:
        return end - start
    else:
        return 0


def get_reimbursement_amount(mileage):
    '''
        Function -- get_reimbursement_amount
            Calculates the amount in dollars that the employee should be
            reimbursed based on their mileage and the standard rate per mile.
            The standard rate for 2020 is 57.5 cents per mile.
        Parameters:
            mileage -- The number of miles driven.
        Returns:
            The amount the employee should be reimbursed in dollars, a float
            rounded to 2 decimal places.
    '''
    STANDARD_RATE = 57.5
    CENTS_TO_DOLLARS = 0.01

    amount_of_reimbursement = mileage * STANDARD_RATE * CENTS_TO_DOLLARS
    return round(amount_of_reimbursement, 2)


def get_actual_mileage_rate(mpg, fuel_price):
    '''
        Function -- get_actual_mileage_rate
            Calculates the actual trip cost per mile in dollars based on the
            car's MPG and the fuel price.
        Parameters:
            mpg -- The car's miles per gallon (MPG), an integer greater than 0.
            fuel_price -- The fuel cost in dollars per gallon, a non-negative
            float.
        Returns:
            The actual cost per mile in dollars, a float rounded to 4 decimal
            places. If supplied arguments are invalid, returns 0.0
    '''
    is_mpg_valid = isinstance(mpg, int) and mpg > 0
    is_fuel_price_valid = isinstance(fuel_price, float) and fuel_price >= 0

    if is_mpg_valid and is_fuel_price_valid:
        dollars_per_mile = fuel_price / mpg
        return round(dollars_per_mile, 4)
    else:
        return 0.0


def get_actual_trip_cost(start, end, mpg, fuel_price):
    '''
        Function -- get_actual_trip_cost
            Calculates the cost of a trip in dollars based on the miles driven,
            the MPG of the car, and the fuel price per gallon.
        Parameters:
            start -- The odometer reading at the start of the trip. Expecting a
            number greater than 0.
            end -- The odometer reading at the end of the trip. Expecting a
            number greater than 0 and greater than the start value.
            mpg -- The car's miles per gallon (MPG), an integer greater than 0.
            fuel_price -- The fuel price per gallon, a non-negative float.
        Returns:
            The cost of the drive in dollars, a float rounded to 2 decimal
            places. If any of the supplied arguments are invalid, returns 0.0
    '''
    mileage = calculate_mileage(start, end)
    actual_mileage_rate = get_actual_mileage_rate(mpg, fuel_price)
    actual_trip_cost = mileage * actual_mileage_rate
    return round(actual_trip_cost, 2)


def main():
    CHOICE1 = "1"
    CHOICE2 = "2"
    CHOICE3 = "3"

    print("MILEAGE REIMBURSEMENT CALCULATOR")
    print("Options:")
    print("1 - Calculate reimbursement amount from odometer readings")
    print("2 - Calculate reimbursement amount from miles traveled")
    print("3 - Calculate the actual cost of your trip")

    user_choice = input("Enter your choice (1, 2, or 3): ")

    if user_choice == CHOICE1:
        start_reading = float(input("Enter your starting odometer reading: "))
        end_reading = float(input("Enter your ending odometer reading: "))
        miles = calculate_mileage(start_reading, end_reading)
        reimbursement = get_reimbursement_amount(miles)
        print("You will be reimbursed $%.2f" % reimbursement)
    elif user_choice == CHOICE2:
        miles = float(input("Enter the number of miles traveled: "))
        reimbursement = get_reimbursement_amount(miles)
        print("You will be reimbursed $%.2f" % reimbursement)
    elif user_choice == CHOICE3:
        start_reading = float(input("Enter your starting odometer reading: "))
        end_reading = float(input("Enter your ending odometer reading: "))
        car_mpg = int(input("Enter your car's MPG: "))
        fuel_price = float(input("Enter the fuel price per gallon: "))
        trip_cost = get_actual_trip_cost(start_reading, end_reading, car_mpg,
                                         fuel_price)
        print("Your trip cost $%.2f" % trip_cost)
    else:
        print("Not a valid choice")


if __name__ == "__main__":
    main()
