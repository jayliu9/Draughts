'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is game state class.
'''

class GameState:
    NUM_SQUARES = 8
    SQUARE = 50
    BOARD_SIZE = NUM_SQUARES * SQUARE
    CORNER = -BOARD_SIZE / 2
    EMPTY = ""
    BLACK = "b"
    RED = "r"
    
    INITIAL_POSITION = [
        [EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK],
        [BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY],
        [EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK, EMPTY, BLACK],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [RED, EMPTY, RED, EMPTY, RED, EMPTY, RED, EMPTY],
        [EMPTY, RED, EMPTY, RED, EMPTY, RED, EMPTY, RED],
        [RED, EMPTY, RED, EMPTY, RED, EMPTY, RED, EMPTY]
    ]
    TURN_STARTED = 3
    PIECE_SELECTED = 0
    MOVE_SELECTED = 1
    NUM_OF_STAGE = 2

    def __init__(self):
        self.squares = self.INITIAL_POSITION
        self.current_player = self.BLACK
        self.stage = self.PIECE_SELECTED
        self.clicks = [self.EMPTY, self.EMPTY]
        self.valid_moves = []

    def contains_any_piece(self, row, col):
        return self.squares[row][col] != self.EMPTY

    def contains_cur_piece(self, row, col):
        return self.squares[row][col] == self.current_player

    def out_of_index(self, row, col):
        return (row > self.NUM_SQUARES - 1 or row < 0 or
                col > self.NUM_SQUARES - 1 or col < 0)


    def psb_noncpt_move(self, row, col, turn):
        left = col - 1
        right = col + 1
        if turn == self.BLACK:
            forward = row + 1
        else:
            forward = row - 1
        self.valid_moves = [[forward, left], [forward, right]]
        valid_moves_copy = self.valid_moves.copy()
        for position in valid_moves_copy:
            if (self.out_of_index(position[0], position[1]) or
                self.contains_any_piece(position[0], position[1])):
                self.valid_moves.remove(position)

    def after_move(self, row, col):
        self.squares[row][col] = self.current_player
        self.move_occurs(col, row)

    def ready_to_move(self, row, col):
        self.squares[row][col] = self.EMPTY
        self.selection_occurs(row, col)

    def changes_stage(self):
        self.stage = (self.stage + 1) % self.NUM_OF_STAGE
    
    def selection_occurs(self, row, col):
        self.clicks[0] = [row, col]

    def move_occurs(self, col, row):
        self.clicks[1] = [row, col]

    def switches_turn(self):
        if self.current_player == self.BLACK:
            self.current_player = self.RED
        else:
            self.current_player = self.BLACK