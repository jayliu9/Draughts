'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is the first milestone of the final project
'''
import turtle
NUM_SQUARES = 8
SQUARE = 50
BOARD_SIZE = NUM_SQUARES * SQUARE
CORNER = -BOARD_SIZE / 2


def draw_square(a_turtle, size):
    '''
        Function -- draw_square
            Draw a square of a given size.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the length of each side of the square
        Returns:
            Nothing. Draws a square in the graphics window.
    '''
    RIGHT_ANGLE = 90
    a_turtle.begin_fill()
    a_turtle.pendown()
    for i in range(4):
        a_turtle.forward(size)
        a_turtle.left(RIGHT_ANGLE)
    a_turtle.end_fill()
    a_turtle.penup()


def click_handler(x, y):
    '''
        Function -- click_handler
            Called when a click occurs.
        Parameters:
            x -- X coordinate of the click. Automatically provided by Turtle.
            y -- Y coordinate of the click. Automatically provided by Turtle.
        Returns:
            Does not and should not return. Click handlers are a special type
            of function automatically called by Turtle. You will not have
            access to anything returned by this function.
    '''
    try:
        click_validator(x, y)
        print("Clicked at", x, y)
    except:
        print("Clicked out of range")


def click_validator(x, y):
    '''
        Function -- click_validation
            Checks that the click was in bounds of the board.
        Parameters:
            x -- X coordinate of the click. Automatically provided by Turtle.
            y -- Y coordinate of the click. Automatically provided by Turtle.
        Raises:
            ValueError -- If the click was out of bounds of the board.
        Returns:
            Nothing
    '''
    out_of_bounds = x < CORNER or x > -CORNER or y > -CORNER or y < CORNER
    if out_of_bounds:
        raise ValueError


def draw_circle(a_turtle, radius):
    '''
        Function -- draw_circle
            Draw a circle with a given radius.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the radius of the circle
        Returns:
            Nothing. Draws a circle in the graphics windo.
    '''
    a_turtle.pendown()
    a_turtle.begin_fill()
    a_turtle.circle(radius)
    a_turtle.end_fill()
    a_turtle.penup()


def black_pieces_starting_row(row):
    '''
        Function -- black_pieces_starting_row
            Checks if the row is the starting position of black pieces, which 
            is from the bottom row of the board to row 2 (the bottom row of the 
            board is counted row 0).
        Parameters:
            row -- the row number
        Returns:
            True if the row is one of the starting row of black pieces, False
            otherwise.
    '''
    LOWEREST_BLACK_STARTING_ROW = 0
    HIGHEST_BLACK_STARTING_ROW = 2
    return (row <= HIGHEST_BLACK_STARTING_ROW and
            row >= LOWEREST_BLACK_STARTING_ROW)


def red_pieces_starting_row(row):
    '''
        Function -- red_pieces_starting_row
            Checks if the row is the starting position of red pieces, which is
            from the top row of the board to row 5 (the bottom row of the board
            is counted row 0).
        Parameters:
            row -- the row number
        Returns:
            True if the row is one of the starting row of red pieces, False
            otherwise.
    '''
    LOWEREST_RED_STARTING_ROW = 5
    HIGHEST_RED_STARTING_ROW = 7
    return row >= LOWEREST_RED_STARTING_ROW and row <= HIGHEST_RED_STARTING_ROW


def main():
    CIRCLE_RADIUS = 0.5 * SQUARE
    SQUARE_COLORS = ("light gray", "white")
    PIECE_COLORS = ("black", "red")
    WINDOW_SIZE = BOARD_SIZE + SQUARE

    turtle.setup(WINDOW_SIZE, WINDOW_SIZE)
    turtle.screensize(BOARD_SIZE, BOARD_SIZE)
    turtle.bgcolor("white")
    turtle.tracer(0, 0)

    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()

    pen.color("black", "white")
    pen.setposition(CORNER, CORNER)
    draw_square(pen, BOARD_SIZE)

    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            if col % 2 != row % 2:
                pen.color("black", SQUARE_COLORS[0])
                pen.setposition(CORNER + SQUARE * col, CORNER + SQUARE * row)
                draw_square(pen, SQUARE)
                if (black_pieces_starting_row(row) or
                    red_pieces_starting_row(row)):
                    if black_pieces_starting_row(row):
                        pen.color(PIECE_COLORS[0], PIECE_COLORS[0])
                    else:
                        pen.color(PIECE_COLORS[1], PIECE_COLORS[1])
                    pen.setposition(CORNER + SQUARE * col + CIRCLE_RADIUS,
                                    CORNER + SQUARE * row)
                    draw_circle(pen, CIRCLE_RADIUS)

    screen = turtle.Screen()
    screen.onclick(click_handler)
    turtle.done()


if __name__ == "__main__":
    main()
