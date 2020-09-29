'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is the prototype of a program that can help students at a small
college register for classes.
'''


def main():
    course_num = input("Enter a course number: ").upper().replace(" ", "")

    is_valid = (course_num == "X101" or course_num == "X102" or
                course_num == "B500" or course_num == "B525" or
                course_num == "B701")
    if not is_valid:
        print("Invalid course number")
    elif course_num == "X101" or course_num == "X102":
        print("You have successfully registered for", course_num)
    else:
        grade_X101 = input("What grade did you get for X101? ").upper()
        grade_X102 = input("What grade did you get for X102? ").upper()
        meet_prerequisites = ((grade_X101 == "A" or grade_X101 == "B") and
                              (grade_X102 == "A" or grade_X102 == "B" or
                              grade_X102 == "C"))
        if meet_prerequisites:
            print("You meet all the prerequisites",
                  "and have successfully registered for", course_num)
        else:
            print("You do not meet the prerequisites for", course_num)


if __name__ == "__main__":
    main()
