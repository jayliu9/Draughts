'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for figuring out how long until a user can buy a house given important factors like the cost of the house and how much money they make.
'''


import math
def main():
    house_cost = float(input("How much is the house? $"))
    annual_salary = float(input("How much is your annual salary? $"))
    saving_percent = float(input("What percent of your monthly salary can you save (between 0 and 1)? "))

    down_payment = 0.25 * house_cost
    monthly_saving = annual_salary / 12 * saving_percent
    time_for_down_payment = down_payment / monthly_saving
    year = time_for_down_payment // 12
    month = math.ceil(time_for_down_payment % 12)
    print("If you save $%f per month, it will take %d year(s) and %d month(s) to save up enough for the down payment!" %(monthly_saving, year, month))

if __name__ == "__main__":
    main()