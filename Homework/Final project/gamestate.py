'''
Name: Shijie Liu
NUID: 001561546
Course Number: 18533
Semester: Fall 2020

This code is game state class.
'''
from piece import Piece
from move import Move


class GameState:
    NUM_SQUARES = 8
    SQUARE = 50
    BOARD_SIZE = NUM_SQUARES * SQUARE
    CORNER = -BOARD_SIZE / 2
    EMPTY = ""
    BLACK = "b"
    RED = "r"
    EMPTY_LIST = []
    INITIAL_CLICK_LIST = [[0, 0], [0, 0]]

    INITIAL_POSITION = [
        [EMPTY, Piece(BLACK), EMPTY, Piece(BLACK), EMPTY, Piece(BLACK), EMPTY, Piece(BLACK)],
        [Piece(BLACK), EMPTY, Piece(BLACK), EMPTY, Piece(BLACK), EMPTY, Piece(BLACK), EMPTY],
        [EMPTY, Piece(BLACK), EMPTY, Piece(BLACK), EMPTY, Piece(BLACK), EMPTY, Piece(BLACK)],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY, EMPTY],
        [Piece(RED), EMPTY, Piece(RED), EMPTY, Piece(RED), EMPTY, Piece(RED), EMPTY],
        [EMPTY, Piece(RED), EMPTY, Piece(RED), EMPTY, Piece(RED), EMPTY, Piece(RED)],
        [Piece(RED), EMPTY, Piece(RED), EMPTY, Piece(RED), EMPTY, Piece(RED), EMPTY]
    ]
    TURN_STARTED = 3
    PIECE_SELECTED = 0
    MOVE_SELECTED = 1
    NUM_OF_STAGE = 2

    def __init__(self):
        self.squares = self.INITIAL_POSITION
        self.current_player = self.BLACK
        self.stage = self.PIECE_SELECTED
        self.clicks = self.INITIAL_CLICK_LIST
        self.initialize_valid_move_lst()
        self.all_pieces_move()

    def contains_any_piece(self, row, col):
        if not self.out_of_index(row, col):
            return self.squares[row][col] != self.EMPTY
        return False

    def contains_cur_piece(self, row, col):
        if self.contains_any_piece(row, col):
            return self.squares[row][col].color == self.current_player
        return False

    def out_of_index(self, row, col):
        return (row > self.NUM_SQUARES - 1 or row < 0 or
                col > self.NUM_SQUARES - 1 or col < 0)

    def psb_noncpt_move(self, row, col):
        noncpt_move_lst = []
        piece = self.squares[row][col]
        for direction in piece.directions:
            move_row = row + direction[0]
            move_col = col + direction[1]
            if not self.contains_any_piece(move_row, move_col):
                noncpt_move_lst.append(Move([row, col], [move_row, move_col], False))
        return noncpt_move_lst
              
        #self.valid_moves = [[forward, left], [forward, right]]
        #valid_moves_copy = self.valid_moves.copy()
        #for position in valid_moves_copy:
            #if (self.out_of_index(position[0], position[1]) or
                #self.contains_any_piece(position[0], position[1])):
                #self.valid_moves.remove(position)
    
    def psb_cpt_move(self, row, col):
        cpt_move_lst = []
        piece = self.squares[row][col]
        for direction in piece.directions:
            move_row = row + direction[0]
            move_col = col + direction[1]
            contains_enemy = self.contains_any_piece(row, col) and not self.contains_cur_piece(row, col)
            if contains_enemy:
                next_row = row + direction[0]
                next_col = col + direction[1]
                if not self.contains_any_piece(next_row, next_col):
                    cpt_move_lst.append(Move([row, col], [next_row, next_col], True))
        return cpt_move_lst

    def initialize_valid_move_lst(self):
        self.valid_moves = self.EMPTY_LIST
    
    def a_piece_move(self, row, col):
        self.initialize_valid_move_lst()
        moves = self.psb_cpt_move(row, col) + self.psb_noncpt_move(row, col)
        for move in moves:
            self.valid_moves.append(move.end)

    def all_pieces_move(self):
        move_lst = []
        for row in range(self.NUM_SQUARES):
            for col in range(self.NUM_SQUARES):
                if self.contains_cur_piece(row, col):
                    move_lst = self.psb_noncpt_move(row, col) + move_lst
                    move_lst = move_lst + self.psb_cpt_move(row, col)
        self.all_move_lst = move_lst

                

    def updates_board(self, row, col):
        pre_row = self.clicks[0][0]
        pre_col = self.clicks[0][1]
        temp = self.squares[pre_row][pre_col]
        self.squares[pre_row][pre_col] = self.EMPTY
        self.squares[row][col] = temp

    def selection_occurs(self, row, col):
        self.clicks[0] = [row, col]

    def changes_stage(self):
        self.stage = (self.stage + 1) % self.NUM_OF_STAGE

    def move_occurs(self, row, col):
        self.clicks[1] = [row, col]

    def switches_turn(self):
        if self.current_player == self.BLACK:
            self.current_player = self.RED
        else:
            self.current_player = self.BLACK

    def reset_moves_lst(self):
        self.valid_moves = self.EMPTY_LIST

    def back_pre_stage(self):
        self.stage = (self.stage - 1) % self.NUM_OF_STAGE
