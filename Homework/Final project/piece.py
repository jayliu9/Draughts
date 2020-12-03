'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is piece class.
'''
class Piece:
    def __init__(self, color):
        self.color = color
        self.initial_direction()
        self.is_king = False

    def initial_direction(self):
        BLACK = "b"
        RED = "r"
        B_RGL_DIRECTION = [[1, -1], [1, 1]]
        R_RGL_DIRECTION = [[-1, -1], [-1, 1]]

        if self.color == BLACK:
            self.directions = B_RGL_DIRECTION
        else:
            self.directions = R_RGL_DIRECTION

    def becomes_king(self):
        KING_DIRECTION = [[1, -1], [1, 1], [-1, -1], [-1, 1]]

        self.directions = KING_DIRECTION
        self.is_king = True
