'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is for calculating the area of a shape.
'''


def main():
    shape = input("Select a shape (triangle, square, or rectangle): ").lower()

    is_valid = shape == "triangle" or shape == "square" or shape == "rectangle"
    if not is_valid:
        print("Unknown shape")
    else:
        width = float(input("Enter the width: "))
        if width <= 0:
            print("Invalid width")
        elif shape == "square":
            area = width * width
            print("The area of the square is %.2f" % area)
        else:
            height = float(input("Enter the height: "))
            if height <= 0:
                print("Invalid height")
            elif shape == "rectangle":
                area = width * height
                print("The area of the rectangle is %.2f" % area)
            else:
                area = width * height / 2
                print("The area of the triangle is %.2f" % area)


if __name__ == "__main__":
    main()
