'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

This code is game state class.
'''
from piece import Piece
from move import Move
import random


class GameState:
    NUM_SQUARES = 8
    SQUARE = 50
    BOARD_SIZE = NUM_SQUARES * SQUARE
    CORNER = -BOARD_SIZE / 2
    EMPTY = ""
    BLACK = 0
    RED = 1
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
    CONTINUE_MOVE_SELECTED = 2
    PIECE_SELECTED = 0
    MOVE_SELECTED = 1
    NUM_OF_STAGE = 2

    def __init__(self):
        self.squares = self.INITIAL_POSITION
        self.current_player = self.BLACK
        self.stage = self.PIECE_SELECTED
        self.clicks = self.INITIAL_CLICK_LIST
        self.valid_moves = []
        self.valid_end_locations = []
        self.all_pieces_move()

    def contains_any_piece(self, row, col):
        return self.squares[row][col] != self.EMPTY

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
            if not self.out_of_index(move_row, move_col) and not self.contains_any_piece(move_row, move_col):
                noncpt_move_lst.append(Move([row, col], [move_row, move_col], False))
        return noncpt_move_lst

    def psb_cpt_move(self, row, col):
        cpt_move_lst = []
        piece = self.squares[row][col]
        for direction in piece.directions:
            move_row = row + direction[0]
            move_col = col + direction[1]
            contains_enemy = not self.out_of_index(move_row, move_col) and self.contains_any_piece(move_row, move_col) and not self.contains_cur_piece(move_row, move_col)
            if contains_enemy:
                next_row = move_row + direction[0]
                next_col = move_col + direction[1]
                if not self.out_of_index(next_row, next_col) and not self.contains_any_piece(next_row, next_col):
                    cpt_move_lst.append(Move([row, col], [next_row, next_col], True))
        return cpt_move_lst

    def reset_endlocations_lst(self):
        self.valid_end_locations.clear()

    def reset_valid_move_lst(self):
        self.valid_moves.clear()

    def a_piece_move(self, row, col):
        self.reset_valid_move_lst()
        self.reset_endlocations_lst()
        moves = self.psb_cpt_move(row, col) + self.psb_noncpt_move(row, col)
        for move in moves:
            self.valid_moves.append(move)
            self.valid_end_locations.append(move.end)
            
    def all_pieces_move(self):
        move_lst = []
        for row in range(self.NUM_SQUARES):
            for col in range(self.NUM_SQUARES):
                if self.contains_cur_piece(row, col):
                    move_lst = self.psb_cpt_move(row, col) + move_lst
                    move_lst = move_lst + self.psb_noncpt_move(row, col)
        self.all_move_lst = move_lst

    def updates_board(self):
        MIDDLE = 0.5
        pre_row = self.clicks[0][0]
        pre_col = self.clicks[0][1]
        moved_row = self.clicks[1][0]
        moved_col = self.clicks[1][1]
        temp = self.squares[pre_row][pre_col]
        self.squares[pre_row][pre_col] = self.EMPTY
        self.squares[moved_row][moved_col] = temp
        if abs(moved_row - pre_row) > 1:
            removed_row = int((pre_row + moved_row) * MIDDLE)
            removed_col = int((pre_col + moved_col) * MIDDLE)
            self.squares[removed_row][removed_col] = self.EMPTY

    def selection_occurs(self, row, col):
        self.clicks[0] = [row, col]

    def stage_of_selection(self):
        self.stage = self.PIECE_SELECTED

    def stage_of_move(self):
        self.stage = self.MOVE_SELECTED

    def stage_of_continue_move(self):
        self.stage = self.CONTINUE_MOVE_SELECTED

    def move_occurs(self, row, col):
        self.clicks[1] = [row, col] 

    def switches_turn(self):
        if self.current_player == self.BLACK:
            self.current_player = self.RED
        else:
            self.current_player = self.BLACK

    def is_king_upgrading_move(self, row, col):
        TOP_ROW = 7
        BOTTOM_ROW = 0
        
        return self.current_player == self.BLACK and row == TOP_ROW or self.current_player == self.RED and row == BOTTOM_ROW
    
    def contains_cpt_move(self, move_lst):
        if not self.is_empty_lst(move_lst):
            return move_lst[0].is_capt
        return False

    def is_empty_lst(self, lst):
        return len(lst) == 0

    def is_cpt_move(self, row, col):
        for move in self.valid_moves:
            if move.is_capt and [row, col] == move.end:
                return True
        return False

    def get_cpt_end_locations(self):
        new_list = []
        for move in self.valid_moves:
            if move.is_capt:
                new_list.append(move.end)
        self.valid_end_locations = new_list

    def is_psb_end_location(self, row, col):
        return [row, col] in self.valid_end_locations

    def all_cur_pieces_captured(self):
        are_captured = True
        for row in range(self.NUM_SQUARES):
            for col in range(self.NUM_SQUARES):
                if self.contains_cur_piece(row, col):
                    are_captured = False
        return are_captured

    def game_over(self):
        return self.is_empty_lst(self.all_move_lst) or self.all_cur_pieces_captured()

    def gets_cpt_moves(self, move_lst):
        new_list = []
        for move in move_lst:
            if move.is_capt:
                new_list.append(move)
        return new_list

    def get_random_ai_move(self, all_possible_moves):
        if self.contains_cpt_move(all_possible_moves):
            all_possible_moves = self.gets_cpt_moves(all_possible_moves)
        ai_move = random.choice(all_possible_moves)
        return ai_move
