'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is for running a table-making robot.

Test cases:
10 tops, 32 legs, 60 screws => 7 tables assembled. Leftover parts: 3 tops, 4 legs, 4 screws.
17 tops, 70 legs, 145 screws => 17 tables assembled. Leftover parts: 0 tops, 2 legs, 9 screws.
7 tops, 25 legs, 61 screws => 6 tables assembled. Leftover parts: 1 tops, 1 legs, 13 screws.
'''

def main():
    available_tops = int(input("Number of tops: "))
    available_legs = int(input("Number of legs: "))
    available_screws = int(input("Number of screws: "))

    tables_from_tops = available_tops 
    tables_from_legs = available_legs // 4
    tables_from_screws = available_screws // 8
    tables_assembled = min(tables_from_tops, tables_from_legs, tables_from_screws)
    remaining_tops = available_tops - tables_assembled
    remaining_legs = available_legs - tables_assembled * 4
    remaining_screws = available_screws - tables_assembled * 8
    print(str(tables_assembled) + " tables assembled. Leftover parts: " + str(remaining_tops) + " tops, " + str(remaining_legs) + " legs, " + str(remaining_screws) + " screws.")

if __name__ == "__main__":
    main()