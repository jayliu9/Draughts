'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is the first milestone of the final project
'''
import turtle


def draw_circle(a_turtle, radius):
    '''
        Function -- draw_circle
            Draws a circle with a given radius.
        Parameters:
            a_turtle -- an instance of Turtle
            size -- the radius of the circle
        Returns:
            Nothing. Draws a circle in the graphics windo.
    '''
    a_turtle.pendown()
    a_turtle.circle(radius)
    a_turtle.penup()


if __name__ == "__main__":
    main()
