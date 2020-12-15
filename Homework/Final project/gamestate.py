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
    '''
        Class -- GameState
            The state of the game.
        Attributes:
            squares -- A nested list storing the state of each square that
            may contain a piece on the board.
            current_player -- An integer representing the current player's turn
            stage -- An integer representing the stage of the turn
            clicks -- A list storing the locations of the selection click and
            the move click.
            valid_moves -- A list storing the valid moves of a piece considered
            to be moved.
            valid_end_locations -- A list storing the valid end locations of a
            piece considered to be moved.
            all_move_lst -- A list containing all possible moves of all pieces.
        Methods:
            contains_any_piece -- Checks whether or not the square contains a
            piece.
            contains_cur_piece -- Checks whether or not the square contains a
            piece that belongs to current player.
            out_of_index -- Checks if the given location, a row/col, is in
            bounds of the squares list.
            psb_noncpt_move -- Gets all possible non-capturing moves of a piece
            in the given location.
            psb_cpt_move -- Gets all possible capturing moves of a piece in the
            given location.
            reset_endlocations_lst -- Clears the list storing the valid end
            locations of a piece.
            reset_valid_move_lst -- Clears the list storing the valid moves of 
            a piece.
            a_piece_move -- Updates the list containing valid moves and the
            list containing valid end locations when a piece is considered to
            be moved.
            all_pieces_move -- Updates the list containing all possible moves
            of all pieces.
            updates_board -- Updates the squares list to update the state of 
            the board.
            selection_occurs -- Updates the selection click in the clicks list.
            stage_of_selection -- Updates the stage of the turn to the
            selection stage.
            stage_of_move -- Updates the stage of the turn to the move stage.
            stage_of_continue_move -- Updates the stage of the turn to the
            continuous move stage.
            move_occurs -- Updates the move click in the clicks list.
            switches_turn -- Switches the turn and updates the current player.
            is_king_upgrading_move -- Checks if the end location of a move
            reaches to the opposite side of the board to makes the piece a
            king.
            contains_cpt_move -- Checks if the given list contains any
            capturing moves.
            is_empty_lst -- Checks if the given list is empty.
            is_cpt_end_location -- Checks if the given end location is one of
            the end locations of capturing moves of the considered piece.
            get_cpt_end_locations -- Updates the list containing valid end
            locations to the one containing only valid capturing end locations.
            is_psb_end_location -- Checks if the given end location is one of
            the end locations of the considered piece.
            all_cur_pieces_captured -- Checks if the current player's pieces on
            the board are captured
            game_over -- Checks if the game is over.
            get_cpt_moves -- Gets all capturing moves from the given list.
            get_random_ai_move -- Randomly chooses a move from the given move
            list. Non-capturing moves in the given list will be ignored if
            there exist capturing moves in the list. 
    '''
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
        '''
            Constructor -- Creates a new instance of GameState
            Parameters:
                self -- The current GameState object.
        '''
        self.squares = self.INITIAL_POSITION
        self.current_player = self.BLACK
        self.stage = self.PIECE_SELECTED
        self.clicks = self.INITIAL_CLICK_LIST
        self.valid_moves = []
        self.valid_end_locations = []
        self.all_pieces_move()

    def contains_any_piece(self, row, col):
        '''
            Method -- contains_any_piece
                Checks whether or not the square contains a piece.
            Parameters:
                self -- The current GameState object.
                row -- The row of the square
                col -- The col of the square
            Returns:
                True if the square in the given location contains a piece,
                False otherwise.
        '''
        return self.squares[row][col] != self.EMPTY

    def contains_cur_piece(self, row, col):
        '''
            Method -- contains_cur_piece
                Checks whether or not the square contains a piece that belongs
                to current player.
            Parameters:
                self -- The current GameState object.
                row -- The row of the square
                col -- The col of the square
            Returns:
                True if the square in the given location contains a piece that
                belong to current player, False otherwise.
        '''
        if self.contains_any_piece(row, col):
            return self.squares[row][col].color == self.current_player
        return False

    def out_of_index(self, row, col):
        '''
            Method -- out_of_index
                Checks if the given location, a row/col, is in bounds of the
                squares list.
            Parameters:
                self -- The current GameState object
                row -- The row to check
                col -- The column to check
            Returns:
                True if the row and col are in bounds, False otherwise.
        '''
        return (row > self.NUM_SQUARES - 1 or row < 0 or
                col > self.NUM_SQUARES - 1 or col < 0)

    def psb_noncpt_move(self, row, col):
        '''
            Method -- psb_noncpt_move
                Gets all possible non-capturing moves of a piece in the given
                location.
            Parameters:
                self -- The current GameState object
                row -- The row of the given location
                col -- The column of the given location
            Returns:
                A list of all possible non-capturing moves of a piece in the
                given location.
        '''
        noncpt_move_lst = []
        piece = self.squares[row][col]
        for direction in piece.directions:
            move_row = row + direction[0]
            move_col = col + direction[1]
            if not self.out_of_index(move_row, move_col) and not self.contains_any_piece(move_row, move_col):
                noncpt_move_lst.append(Move([row, col], [move_row, move_col], False))
        return noncpt_move_lst

    def psb_cpt_move(self, row, col):
        '''
            Method -- psb_cpt_move
                Gets all possible capturing moves of a piece in the given
                location.
            Parameters:
                self -- The current GameState object
                row -- The row of the given location
                col -- The column of the given location
            Returns:
                A list of all possible capturing moves of a piece in the
                given location.
        '''
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
        '''
            Method -- reset_endlocations_lst
                Clears the list storing the valid end locations of a piece.
            Parameters:
                self -- The current GameState object
        '''
        self.valid_end_locations.clear()

    def reset_valid_move_lst(self):
        '''
            Method -- reset_valid_move_lst
                Clears the list storing the valid moves of a piece.
            Parameters:
                self -- The current GameState object
        '''
        self.valid_moves.clear()

    def a_piece_move(self, row, col):
        '''
            Method -- a_piece_move
                Updates the list containing valid moves and the list containing
                valid end locations when a piece is considered to be moved.
            Parameters:
                self -- The current GameState object
                row -- The row of the considered piece
                col -- The column of the considered piece
        '''
        self.reset_valid_move_lst()
        self.reset_endlocations_lst()
        moves = self.psb_cpt_move(row, col) + self.psb_noncpt_move(row, col)
        for move in moves:
            self.valid_moves.append(move)
            self.valid_end_locations.append(move.end)
            
    def all_pieces_move(self):
        '''
            Method -- all_pieces_move
                Updates the list containing all possible moves of all pieces.
            Parameters:
                self -- The current GameState object
        '''
        move_lst = []
        for row in range(self.NUM_SQUARES):
            for col in range(self.NUM_SQUARES):
                if self.contains_cur_piece(row, col):
                    move_lst = self.psb_cpt_move(row, col) + move_lst
                    move_lst = move_lst + self.psb_noncpt_move(row, col)
        self.all_move_lst = move_lst

    def updates_board(self):
        '''
            Method -- updates_board
                Updates the squares list to update the state of the board.
            Parameters:
                self -- The current GameState object
        '''
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
        '''
            Method -- selection_occurs
                Updates the selection click in the clicks list.
            Parameters:
                self -- The current GameState object
                row -- The row of the piece that is selected to move
                col -- The column of the piece that is selected to move
        '''
        self.clicks[0] = [row, col]

    def stage_of_selection(self):
        '''
            Method -- stage_of_selection
                Updates the stage of the turn to the selection stage.
            Parameters:
                self -- The current GameState object
        '''
        self.stage = self.PIECE_SELECTED

    def stage_of_move(self):
        '''
            Method -- stage_of_move
                Updates the stage of the turn to the move stage.
            Parameters:
                self -- The current GameState object
        '''
        self.stage = self.MOVE_SELECTED

    def stage_of_continue_move(self):
        '''
            Method -- stage_of_continue_move
                Updates the stage of the turn to the continuous move stage.
            Parameters:
                self -- The current GameState object
        '''
        self.stage = self.CONTINUE_MOVE_SELECTED

    def move_occurs(self, row, col):
        '''
            Method -- move_occurs
                Updates the move click in the clicks list.
            Parameters:
                self -- The current GameState object
                row -- The row to which the piece has been moved
                col -- The column to which the piece has been moved
        '''
        self.clicks[1] = [row, col] 

    def switches_turn(self):
        '''
            Method -- switches_turn
                Switches the turn and updates the current player.
            Parameters:
                self -- The current GameState object
        '''
        if self.current_player == self.BLACK:
            self.current_player = self.RED
        else:
            self.current_player = self.BLACK

    def is_king_upgrading_move(self, row):
        '''
            Method -- is_king_upgrading_move
                Checks if the end location of a move reaches to the opposite
                side of the board to makes the piece a king.
            Parameters:
                self -- The current GameState object
                row -- The row of the end location to check
            Returns:
                True if the end location of a move reaches to the opposite side
                of the board, False otherwise.
        '''
        TOP_ROW = 7
        BOTTOM_ROW = 0
        
        return self.current_player == self.BLACK and row == TOP_ROW or self.current_player == self.RED and row == BOTTOM_ROW
    
    def contains_cpt_move(self, move_lst):
        '''
            Method -- contains_cpt_move
                Checks if the given list contains any capturing moves.
            Parameters:
                self -- The current GameState object
                move_lst -- The given list.
            Returns:
                True if the given list contains capturing moves, False
                otherwise.
        '''
        if not self.is_empty_lst(move_lst):
            return move_lst[0].is_capt
        return False

    def is_empty_lst(self, lst):
        '''
            Method -- is_empty_lst
                Checks if the given list is empty.
            Parameters:
                self -- The current GameState object
                lst -- The given list.
            Returns:
                True if the given list is empty, False otherwise.
        '''
        return len(lst) == 0

    def is_cpt_end_location(self, row, col):
        '''
            Method -- is_cpt_end_location
                Checks if the given end location is one of the end locations of
                capturing moves of the considered piece.
            Parameters:
                self -- The current GameState object
                row -- The row of the end location to check
                col -- The column of the end location to check
            Returns:
                True if the given end location is one of the end locations of
                capturing moves of the considered piece, False otherwise.
        '''
        for move in self.valid_moves:
            if move.is_capt and [row, col] == move.end:
                return True
        return False

    def get_cpt_end_locations(self):
        '''
            Method -- get_cpt_end_locations
                Updates the list containing valid end locations to the one
                containing only valid capturing end locations.
            Parameters:
                self -- The current GameState object
        '''
        new_list = []
        for move in self.valid_moves:
            if move.is_capt:
                new_list.append(move.end)
        self.valid_end_locations = new_list

    def is_psb_end_location(self, row, col):
        '''
            Method -- is_psb_end_location
                Checks if the given end location is one of the end locations of
                the considered piece.
            Parameters:
                self -- The current GameState object
                row -- The row of the end location to check
                col -- The column of the end location to check
            Returns:
                True if he given end location is one of the end locations of
                the considered piece, False otherwise.
        '''
        return [row, col] in self.valid_end_locations

    def all_cur_pieces_captured(self):
            '''
            Method -- all_cur_pieces_captured
                Checks if the current player's pieces on the board are captured
            Parameters:
                self -- The current GameState object
            Returns:
                True if the current player's pieces on the board are captured,
                False otherwise.
        '''
        are_captured = True
        for row in range(self.NUM_SQUARES):
            for col in range(self.NUM_SQUARES):
                if self.contains_cur_piece(row, col):
                    are_captured = False
        return are_captured

    def game_over(self):
        '''
            Method -- game_over
                Checks if the game is over.
            Parameters:
                self -- The current GameState object
            Returns:
                True if the game is over, False otherwise.
        '''
        return self.is_empty_lst(self.all_move_lst) or self.all_cur_pieces_captured()

    def get_cpt_moves(self, move_lst):
        '''
            Method -- get_cpt_moves
                Gets all capturing moves from the given list.
            Parameters:
                self -- The current GameState object
                move_lst -- The given list
            Returns:
                The list of all capturing moves from the given list.
        '''
        new_list = []
        for move in move_lst:
            if move.is_capt:
                new_list.append(move)
        return new_list

    def get_random_ai_move(self, all_possible_moves):
        '''
            Method -- get_random_ai_move
                Randomly chooses a move from the given move list. Non-capturing
                moves in the given list will be ignored if there exist
                capturing moves in the list. 
            Parameters:
                self -- The current GameState object
                all_possible_moves -- The given move list
            Returns:
                A random move from the given list.
        '''
        if self.contains_cpt_move(all_possible_moves):
            all_possible_moves = self.get_cpt_moves(all_possible_moves)
        ai_move = random.choice(all_possible_moves)
        return ai_move
