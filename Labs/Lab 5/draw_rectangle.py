'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for drawing a rectangle in command line.
'''


def rows_top_bottom(width, character):
    '''
        Function - rows_top_bottom
            Draws the top or the bottom of a rectangle.
        Parameters:
            character - The character to use to draw the rectangle.
        Returns:
            A top or a bottom of a rectangle consisting of the parameter.
    '''
    top_and_bottom = width * character
    return top_and_bottom


def rows_inside(width, character):
    '''
        Function - rows_inside
            Draws a middle row of a rectangle.
        Parameters:
            character - The character to use to draw the either end.
        Returns:
            A middle row of the rectangle consisting of the spaces and the
            parameter.
    '''
    SPACE = " "

    middle_rows = character + SPACE * (width - 2) + character
    return middle_rows


def main():
    NUM_OF_TOP_BOTTOM_ROWS = 2
    width = int(input("Enter a desired width in columns: "))
    height = int(input("Enter a desired height in rows: "))
    character = input("Enter a character you will use to draw a rectangle: ")

    if height != 0 and width != 0:
        print(rows_top_bottom(width, character))
        for i in range(height - NUM_OF_TOP_BOTTOM_ROWS):
            print(rows_inside(width, character))
        print(rows_top_bottom(width, character))


if __name__ == "__main__":
    main()
