'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is piece class.
'''
class Piece:
    def __init__(self, color, directions):
        self.color = color
        self.directions = directions
        self.is_king = False