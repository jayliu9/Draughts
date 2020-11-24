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
    TURN_STARTED = 0
    PIECE_SELECTED = 1
    MOVE_SELECTED = 2
    NUM_OF_STAGE = 3

    def __init__(self):
        self.squares = INITIAL_POSITION
        self.current_player = BLACK
        self.stage = TURN_STARTED
        self.clicks = [EMPTY, EMPTY]
        self.valid_moves = None

    def contains_any_piece(self, col, row):
        return self.squares[col][row] != EMPTY

    def contains_cur_piece(self, col, row):
        return self.squares[col][row] == self.current_player

    def out_of_index(self, col, row):
        return col > NUM_SQUARES - 1 or row > NUM_SQUARES - 1

    def psb_noncpt_move(self, col, row, turn):
        left = col - 1
        right = col + 1
        if turn == BLACK:
            forward = row + 1
        else:
            forward = row - 1
        self.valid_moves = [[left, forward], [right, forward]]
        for i, position in enumerate(self.valid_moves):
            if (self.out_of_index(position[0], position[1]) or
                self.contains_any_piece(position[0], position[1])):
                self.valid_moves.pop(i)

    def after_move(self, col, row):
        self.squares[col][row] = self.current_player
        self.move_occurs(col, row)

    def ready_to_move(self, col, row):
        self.squares[col][row] = EMPTY
        self.selection_occurs(col, row)

    def changes_stage(self):
        self.stage = (self.stage + 1) % NUM_OF_STAGE
    
    def selection_occurs(self, col, row):
        self.clicks[0] = [col, row]

    def move_occurs(self, col, row):
        self.clicks[1] = [col, row]