'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is for drawing a nested star with Turtle using recursion.
'''
import turtle


def draw_nested_star(turt, initial_len, increase, num_of_segment):
    RIGHT_ANGLE = 144
    COLORS = ("green", "blue", "orange", "red", "yellow")
    INITIAL_LENGTH = 50

    color_index = 0
    turt.pendown()
    turt.color(COLORS[color_index])
    if num_of_segment <= 1:
            turt.forward(initial_len)
            turt.penup()
    else:
