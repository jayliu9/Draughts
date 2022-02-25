'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for drawing a nested star with Turtle using recursion.
'''
import turtle


def draw_nested_star(turt, initial_len, increase, num_of_segment, color_index):
    '''
        Function -- draw_nested_star
            Draws a nested star
        Parameters:
            turt -- an instance of Turtle
            initial_len -- the initial length of the star
            increase -- the increased length each time
            num_of_segment -- the number of the segments to draw
            color_index -- the index of the color used to draw the segment
        Returns:
            Nothing. Draws a nested star in the graphics windo.
    '''
    RIGHT_ANGLE = 144
    COLORS = ("green", "blue", "orange", "red", "yellow")
    INITIAL_LENGTH = 50

    turt.pendown()
    turt.color(COLORS[color_index])
    if num_of_segment <= 1:
            turt.forward(initial_len)
            turt.penup()
    else:        
        turt.forward(initial_len)
        turt.right(RIGHT_ANGLE)
        turt.penup()
        draw_nested_star(turt, initial_len + increase, increase,
                         num_of_segment - 1, (color_index + 1) % len(COLORS))


def main():
    INITIAL_ANGLE = 72
    INITIAL_LENGTH = 50
    FIRST_COLOR_INDEX = 0
    LENGTH_INCREASE = 10

    turtle.setup(520, 520)
    turtle.screensize(500, 500)
    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.left(INITIAL_ANGLE)

    segments = 20
    draw_nested_star(pen, INITIAL_LENGTH, LENGTH_INCREASE, segments,
                     FIRST_COLOR_INDEX)

    turtle.done()


if __name__ == "__main__":
    main()
