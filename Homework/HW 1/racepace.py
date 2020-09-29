'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code can be used to calculate statistics about a race time by runners.

Test cases：
12 km, 0 hours, 48 minutes => 7.45 miles, 6:26 pace, 9.32 MPH
21 km, 2 hours, 5 minutes => 13.04 miles, 9:35 pace, 6.26 MPH
25 km, 2 hours, 42 minutes => 15.53 miles, 10:26 pace, 5.75 MPH
'''

def main():
    distance_kilometers = float(input("How many kilometers did you run? "))
    hours = int(input("What was your finish time? Enter hours: "))
    minutes = int(input("Enter minutes: "))

    distance_miles = distance_kilometers / 1.61
    rounded_distance_miles = round(distance_kilometers / 1.61, 2)
    minutes_of_average_pace = int(((60 * hours) + minutes) // distance_miles)
    seconds_of_average_pace = round(((60 * hours) + minutes) % distance_miles / distance_miles * 60)
    average_pace = str(minutes_of_average_pace) + ":" + str(seconds_of_average_pace).zfill(2)
    rounded_speed = round(distance_miles / (hours + minutes / 60), 2)
    print(str(rounded_distance_miles) + " miles, " + average_pace + " pace, " + str(rounded_speed) + " MPH")

if __name__ == "__main__":
    main()