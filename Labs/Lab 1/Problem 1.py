'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for figuring out how to split a restaurant bill.
'''

def main():
    bill_amount = float(input("Please input your total amount of the bill ($): "))
    tip_percentage = float(input("Please input the percentage everyone is willing to tip (between 0 and 1): "))
    num_of_people = int(input("Please input the number of people your group: "))

    total_amount = bill_amount * (1 + tip_percentage)
    amount_for_user = total_amount / num_of_people
    print("The amount of money each person should pay is ($):", amount_for_user)
    
if __name__ == "__main__":
    main()