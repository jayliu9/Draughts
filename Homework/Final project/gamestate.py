'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is game state class.
'''
NUM_SQUARES = 8
SQUARE = 50
BOARD_SIZE = NUM_SQUARES * SQUARE
CORNER = -BOARD_SIZE / 2

class GameState:
    EMPTY = 0
    BLACK = 1
    RED = 2
    INITIAL_POSITION = [
        [EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK]
        [BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY]
        [EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK]
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY]
        [RED, EMPTY, RED, EMPTY, RED, EMPTY, RED, EMPTY]
        [EMPTY, RED, EMPTY, RED, EMPTY, RED, EMPTY, RED]
        [RED, EMPTY, RED, EMPTY, RED, EMPTY, RED, EMPTY]
    ]
    def __init__(self):
        self.squares = INITIAL_POSITION
        self.current_player = BLACK

    def contains_cur_piece(self, x, y):
        col = self.calculates_col(x)
        row = self.calculates_row(y)
        return self.squares[col][row] == self.current_player

    def calculates_col(self, x):
        return (x - CORNER) // SQUARE

    def calculates_row(self, y):
        return (y - CORNER) // SQUARE
    
    def move_piece(self, x, y)