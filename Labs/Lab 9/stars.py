'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for drawing a nested star with Turtle.
'''
import turtle
LINES_OF_STAR = 5

def draw_star(turt, initial_len, increase):
    '''
        Function -- draw_star
            Draw a single star with the length of each of its lines increasing.
        Parameters:
            turt -- an instance of Turtle
            initial_len -- the initial length of the star
            increase -- the increased length each time
        Returns:
            Nothing. Draws a star in the graphics windo.
    '''
    RIGHT_ANGLE = 144
    COLORS = ("green", "blue", "orange", "red", "yellow")

    turt.pendown()
    line_len = initial_len
    count = 0
    while count < LINES_OF_STAR:
        turt.color(COLORS[count])
        turt.forward(line_len)
        line_len += increase
        turt.right(RIGHT_ANGLE)
        count += 1
    turt.penup()


def main():
    INITIAL_ANGLE = 72
    ROUND = 4
    INITIAL_LENGTH = 50
    LENGTH_INCREASE = 10

    turtle.setup(520, 520)
    turtle.screensize(500, 500)

    pen = turtle.Turtle()
    pen.speed(0)
    pen.hideturtle()
    pen.left(INITIAL_ANGLE)
    count = 0
    length = INITIAL_LENGTH
    while count < ROUND:
        draw_star(pen, length, LENGTH_INCREASE)
        count += 1
        length += LENGTH_INCREASE * LINES_OF_STAR
    
    turtle.done()


if __name__ == "__main__":
    main()
