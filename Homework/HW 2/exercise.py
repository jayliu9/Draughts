'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is for making an exercise plan based on the day of the week and
weather.
'''


def main():
    day_of_week = input("What day is it? ").upper()
    holiday = input("Is it a holiday? ").upper()
    raining = input("Is it raining? ").upper()
    temp = float(input("What is the temperature? "))

    day_is_valid = (day_of_week == "M" or day_of_week == "TU" or
                    day_of_week == "W" or day_of_week == "TH" or
                    day_of_week == "F" or day_of_week == "SA" or
                    day_of_week == "SU")
    holiday_is_valid = holiday == "Y" or holiday == "N"
    raining_is_valid = raining == "Y" or raining == "N"

    is_holiday = holiday == "Y"
    is_raining = raining == "Y"
    running_days = ((day_of_week == "M" or day_of_week == "W" or
                    day_of_week == "F") and not is_holiday)
    hiking_days = day_of_week == "SA" or is_holiday
    duration = 45

    if not (day_is_valid and holiday_is_valid and raining_is_valid):
        print("Swim for 35 minutes")
    elif is_raining and (running_days or hiking_days):
        exercise = "Swim"
    elif hiking_days:
        exercise = "Hike"
    elif running_days:
        if temp > 75 or temp < 35:
            duration = 30
        exercise = "Run"
    else:
        print("Take a rest day")

    if (day_is_valid and holiday_is_valid and raining_is_valid and
       (running_days or hiking_days)):
        print(exercise, "for", duration, "minutes")


if __name__ == "__main__":
    main()
