'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

This code is drawing UI class.
'''
import turtle
from gamestate import GameState


class DrawingUI:
    '''
        Class -- DrawingUI
            The board UI.
        Attributes:
            game_state -- A GameState object, used to keep track of the status
            of the game.
            pen -- The Turtle responsible for drawing
            screen -- The screen
        Methods:
            (none intended to be accessed outside the class)
    '''
    NUM_SQUARES = 8
    SQUARE = 50
    BOARD_SIZE = NUM_SQUARES * SQUARE
    CORNER = -BOARD_SIZE / 2
    SQUARE_COLORS = ("light gray", "white")
    PIECE_COLORS = ("black", "red")
    CIRCLE_RADIUS = 0.5 * SQUARE
    WINDOW_SIZE = BOARD_SIZE + 4 * SQUARE
    KING_MARK_SIZE = 10
    INDICATOR_X_COORD = CORNER - SQUARE
    INDICATOR_Y_COORD = CORNER + 3.5 * SQUARE
    INDICATOR_SQUARE_SIZE = 0.5 * SQUARE
    TURN_SIGN_RADUIS = 0.5 * CIRCLE_RADIUS
    DELAY_TIME = 500

    def __init__(self):
        '''
            Constructor -- Creates a new instance of DrawingUI
            Parameters:
                self -- The current DrawingUI object.
        '''
        self.game_state = GameState()
        self.initialize_board()
        self.black_turn_sign()
        self.screen.onclick(self.click_handler)
        turtle.done()

    def click_handler(self, x, y):
        '''
            Method -- click_handler
                Called when a click occurs.
            Parameters:
                self -- The current DrawingUI object.
                x -- X coordinate of the click.
                y -- Y coordinate of the click.
        '''
        CAPTURE_MOVE_HINT = ("Attention: " +
                             "There exists a capturing move somewhere. " +
                             "Please try again.")
        INVALID_MOVE_WARNING = "Warning: Invalid move."
        CONTINUE_CAPTURE_HINT = ("Attention: " +
                                 "You can continue to capture " +
                                 "with the piece you just selected.")
        try:
            if self.game_state.current_player == self.game_state.BLACK:
                self.click_validator(x, y)
                row = self.convert_to_location(y)
                col = self.convert_to_location(x)
                self.remove_mark()
                if self.game_state.stage == self.game_state.PIECE_SELECTED:
                    if self.game_state.contain_cur_piece(row, col):
                        self.game_state.selection_occurs(row, col)
                        self.game_state.a_piece_move(row, col)
                        self.draw_highlighting_mark()
                        self.game_state.stage_of_move()
                elif (self.game_state.stage == self.game_state.MOVE_SELECTED or
                      self.game_state.stage == self.game_state.CONTINUE_MOVE):
                    if self.game_state.contain_cpt_move(
                       self.game_state.all_move_lst):
                        if self.game_state.is_cpt_end_location(row, col):
                            self.game_state.move_occurs(row, col)
                            if self.game_state.is_king_upgrading_move(row):
                                pre_row = self.game_state.clicks[0][0]
                                pre_col = self.game_state.clicks[0][1]
                                self.game_state.squares[pre_row][pre_col] \
                                    .become_king()
                            self.game_state.update_board()
                            self.game_state.reset_endlocations_lst()
                            self.game_state.reset_valid_move_lst()
                            self.draw_board()

                            self.game_state.a_piece_move(row, col)
                            if self.game_state.contain_cpt_move(
                               self.game_state.valid_moves):
                                self.game_state.stage_of_continue_move()
                                self.game_state.selection_occurs(row, col)
                                self.game_state.get_cpt_end_locations()
                                self.draw_highlighting_mark()
                            else:
                                self.game_state.switch_turn()
                                self.game_state.all_pieces_move()
                                self.game_state.stage_of_selection()
                        elif self.game_state.contain_cur_piece(row, col):
                            self.game_state.a_piece_move(row, col)
                            if (self.game_state.stage ==
                               self.game_state.MOVE_SELECTED):
                                self.game_state.selection_occurs(row, col)
                                self.draw_highlighting_mark()
                            elif (row == self.game_state.clicks[0][0] and
                                  col == self.game_state.clicks[0][1]):
                                self.game_state.get_cpt_end_locations()
                                self.draw_highlighting_mark()
                            else:
                                print(CONTINUE_CAPTURE_HINT)
                        else:
                            if (self.game_state.stage ==
                               self.game_state.MOVE_SELECTED):
                                self.game_state.stage_of_selection()
                                if self.game_state.is_psb_end_location(row,
                                                                       col):
                                    print(CAPTURE_MOVE_HINT)
                                else:
                                    print(INVALID_MOVE_WARNING)
                            else:
                                print(CONTINUE_CAPTURE_HINT)
                            self.game_state.reset_endlocations_lst()
                            self.game_state.reset_valid_move_lst()
                    elif self.game_state.is_psb_end_location(row, col):
                        self.game_state.move_occurs(row, col)
                        if self.game_state.is_king_upgrading_move(row):
                            pre_row = self.game_state.clicks[0][0]
                            pre_col = self.game_state.clicks[0][1]
                            self.game_state.squares[pre_row][pre_col] \
                                .become_king()
                        self.game_state.update_board()
                        self.game_state.reset_endlocations_lst()
                        self.game_state.reset_valid_move_lst()
                        self.draw_board()

                        self.game_state.switch_turn()
                        self.game_state.all_pieces_move()
                        self.game_state.stage_of_selection()
                    elif self.game_state.contain_cur_piece(row, col):
                        self.game_state.selection_occurs(row, col)
                        self.game_state.a_piece_move(row, col)
                        self.draw_highlighting_mark()
                    else:
                        print(INVALID_MOVE_WARNING)
                        self.game_state.reset_endlocations_lst()
                        self.game_state.reset_valid_move_lst()
                        self.game_state.stage_of_selection()

                self.indicator_display()

            if self.game_state.current_player == self.game_state.RED:
                self.screen.onclick(None)
                self.remove_mark()
                if not self.game_state.game_over():
                    self.screen.ontimer(self.show_ai_begin, self.DELAY_TIME)
                else:
                    print("Game Over. You win!")
                    self.screen.onclick(None)
        except ValueError:
            print("out of range")

    def convert_to_location(self, coord):
        '''
            Method -- convert_to_location
                Converts a click coordinate to a square location.
            Parameters:
                self -- the current Board object
                coord -- the click coordinate (x or y)
            Returns:
                The index of the square that was clicked. Works for row and col
        '''
        return int((coord - self.CORNER) // self.SQUARE)

    def remove_mark(self):
        '''
            Method -- remove_mark
                Removes the marks that highlight the selected square containing
                a piece and those which highlight possibly reachable squares of
                the piece.
            Parameters:
                self -- The current DrawingUI object.
        '''
        selection_click = self.game_state.clicks[0]
        chosen_row = selection_click[0]
        chosen_col = selection_click[1]
        self.remove_choice_mark(chosen_row, chosen_col)
        for end_location in self.game_state.valid_end_locations:
            row_to_move = end_location[0]
            col_to_move = end_location[1]
            self.remove_reachable_mark(row_to_move, col_to_move)

    def click_validator(self, x, y):
        '''
            Method -- click_validator
                Checks that the click was in bounds of the board.
            Parameters:
                self -- The current DrawingUI object.
                x -- X coordinate of the click.
                y -- Y coordinate of the click.
            Raises:
                ValueError -- If the click was out of bounds of the board.
            Returns:
                Nothing
        '''
        out_of_bounds = (x < self.CORNER or x > -self.CORNER or
                         y > -self.CORNER or y < self.CORNER)
        if out_of_bounds:
            raise ValueError

    def draw_square(self, size):
        '''
            Method -- draw_square
                Draws a filled square of a given size.
            Parameters:
                self -- The current DrawingUI object.
                size -- the length of each side of the square
        '''
        RIGHT_ANGLE = 90
        self.pen.begin_fill()
        self.pen.pendown()
        for i in range(4):
            self.pen.forward(size)
            self.pen.left(RIGHT_ANGLE)
        self.pen.end_fill()
        self.pen.penup()

    def draw_circle(self, radius):
        '''
            Method -- draw_circle
                Draws a filled circle with a given radius.
            Parameters:
                self -- The current DrawingUI object.
                radius -- the radius of the circle
        '''
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(radius)
        self.pen.end_fill()
        self.pen.penup()

    def draw_board(self):
        '''
            Method -- draw_board
                Draws the whole board containing all the pieces on the board.
            Parameters:
                self -- The current DrawingUI object.
        '''
        cells = self.game_state.squares
        for row in range(self.game_state.NUM_SQUARES):
            for col in range(self.game_state.NUM_SQUARES):
                if col % 2 != row % 2:
                    self.pen.color("black", self.SQUARE_COLORS[0])
                    self.pen.setposition(self.CORNER + self.SQUARE * col,
                                         self.CORNER + self.SQUARE * row)
                    self.draw_square(self.SQUARE)
                    if self.game_state.contain_any_piece(row, col):
                        a_piece = cells[row][col]
                        piece_color = a_piece.color
                        self.pen.color(self.PIECE_COLORS[piece_color])
                        self.pen.setposition(self.CORNER + self.SQUARE * col +
                                             self.CIRCLE_RADIUS, self.CORNER +
                                             self.SQUARE * row)
                        self.draw_circle(self.CIRCLE_RADIUS)
                        if a_piece.is_king:
                            self.draw_king_mark(row, col)

    def draw_nonfilled_square(self, size):
        '''
            Method -- draw_nonfilled_square
                Draws a unfilled square of a given size.
            Parameters:
                self -- The current DrawingUI object.
                size -- the length of each side of the square
        '''
        RIGHT_ANGLE = 90
        self.pen.pendown()
        for i in range(4):
            self.pen.forward(size)
            self.pen.left(RIGHT_ANGLE)
        self.pen.penup()

    def draw_highlighting_mark(self):
        '''
            Method -- draw_highlighting_mark
                Draws the marks that highlight the selected square containing
                a piece and those highlighting possibly reachable squares of
                the piece.
            Parameters:
                self -- The current DrawingUI object.
        '''
        CHOOSING_COLOR = "light green"
        ORIGINAL_COLOR = "black"
        HINT_COLOR = "red"

        selection_click = self.game_state.clicks[0]
        chosen_row = selection_click[0]
        chosen_col = selection_click[1]

        self.pen.setposition(self.CORNER + chosen_col * self.SQUARE,
                             self.CORNER + chosen_row * self.SQUARE)
        self.pen.color(CHOOSING_COLOR)
        self.draw_nonfilled_square(self.SQUARE)

        self.pen.color(HINT_COLOR)
        for end_location in self.game_state.valid_end_locations:
            next_row = end_location[0]
            next_col = end_location[1]
            self.pen.setposition(self.CORNER + next_col * self.SQUARE,
                                 self.CORNER + next_row * self.SQUARE)
            self.draw_nonfilled_square(self.SQUARE)
        self.pen.color(ORIGINAL_COLOR)

    def remove_reachable_mark(self, row, col):
        '''
            Method -- remove_reachable_mark
                Removes the mark highlighting the possibly reachable square.
            Parameters:
                self -- The current DrawingUI object.
                row -- The row where the mark is
                col -- The column where the mark is
        '''
        self.pen.color("black", self.SQUARE_COLORS[0])
        self.pen.setposition(self.CORNER + col * self.SQUARE,
                             self.CORNER + row * self.SQUARE)
        self.draw_square(self.SQUARE)

    def remove_choice_mark(self, row, col):
        '''
            Method -- remove_choice_mark
                Removes the mark that highlights the selected square containing
                a piece.
            Parameters:
                self -- The current DrawingUI object.
                row -- The row where the mark is
                col -- The column where the mark is
        '''
        self.pen.color("black")
        self.pen.setposition(self.CORNER + col * self.SQUARE,
                             self.CORNER + row * self.SQUARE)
        self.draw_nonfilled_square(self.SQUARE)

    def initialize_board(self):
        '''
            Method -- initialize_board
                Helper method to initialize the board.
            Parameter:
                self -- The current DrawingUI object.
        '''
        turtle.setup(self.WINDOW_SIZE, self.WINDOW_SIZE)
        turtle.screensize(self.BOARD_SIZE, self.BOARD_SIZE)
        turtle.bgcolor("white")
        turtle.tracer(0, 0)

        self.pen = turtle.Turtle()
        self.screen = turtle.Screen()
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.color("black", "white")
        self.pen.setposition(self.CORNER, self.CORNER)
        self.draw_square(self.BOARD_SIZE)

        self.draw_board()

    def indicator_frame(self):
        '''
            Method -- indicator_frame
                Creates the frame of the indicator.
            Parameters:
                self -- The current DrawingUI object.
        '''
        self.pen.color("black", "white")
        self.pen.setposition(self.INDICATOR_X_COORD, self.INDICATOR_Y_COORD)
        self.draw_square(self.INDICATOR_SQUARE_SIZE)
        self.pen.setposition(
            self.INDICATOR_X_COORD,
            self.INDICATOR_Y_COORD + self.INDICATOR_SQUARE_SIZE
        )
        self.draw_square(self.INDICATOR_SQUARE_SIZE)

    def black_turn_sign(self):
        '''
            Method -- black_turn_sign
                Displays the specific sign when it is black's turn.
            Parameters:
                self -- The current DrawingUI object.
        '''
        self.indicator_frame()
        self.pen.color(self.PIECE_COLORS[0])
        self.pen.setposition(self.INDICATOR_X_COORD + self.TURN_SIGN_RADUIS,
                             self.INDICATOR_Y_COORD)
        self.draw_circle(self.TURN_SIGN_RADUIS)

    def red_turn_sign(self):
        '''
            Method -- red_turn_sign
                Displays the specific sign when it is red's turn.
            Parameters:
                self -- The current DrawingUI object.
        '''
        self.indicator_frame()
        self.pen.color(self.PIECE_COLORS[1])
        self.pen.setposition(
            self.INDICATOR_X_COORD + self.TURN_SIGN_RADUIS,
            self.INDICATOR_Y_COORD + self.INDICATOR_SQUARE_SIZE
        )
        self.draw_circle(self.TURN_SIGN_RADUIS)

    def draw_king_mark(self, row, col):
        '''
            Method -- draw_king_mark
                Draws the mark distinguishing a king piece from normal pieces.
            Parameters:
                self -- The current DrawingUI object.
        '''
        self.pen.color("yellow")
        self.pen.setposition(
            self.CORNER + self.SQUARE * col + self.CIRCLE_RADIUS,
            (self.CORNER + self.SQUARE * row + self.CIRCLE_RADIUS -
             self.KING_MARK_SIZE)
        )
        self.draw_circle(self.KING_MARK_SIZE)

    def indicator_display(self):
        '''
            Method -- indicator_display
                Displays the indicator which shows whose turn it is.
            Parameters:
                self -- The current DrawingUI object.
        '''
        if self.game_state.current_player == self.game_state.RED:
            self.red_turn_sign()
        else:
            self.black_turn_sign()

    def show_ai_begin(self):
        '''
            Method -- show_ai_begin
                Highlights the start square and the end square of the move
                randomly selected by AI, also updates relevant information on
                the state of game. Starts a time to move the piece selected by
                AI.
            Parameters:
                self -- The current DrawingUI object.
        '''
        self.game_state.get_random_ai_move(self.game_state.all_move_lst)
        ai_start_row = self.game_state.chosen_ai_move.start[0]
        ai_start_col = self.game_state.chosen_ai_move.start[1]
        self.game_state.selection_occurs(ai_start_row, ai_start_col)
        self.game_state.a_piece_move(ai_start_row, ai_start_col)
        self.draw_highlighting_mark()
        self.game_state.stage_of_move()
        self.screen.ontimer(self.complete_ai_move, self.DELAY_TIME)

    def complete_ai_move(self):
        '''
            Method -- complete_ai_move
                Completes the move randomly chosen by AI. Also updates relevant
                information on the state of game.
            Parameters:
                self -- The current DrawingUI object.
        '''
        while (self.game_state.stage == self.game_state.MOVE_SELECTED or
               self.game_state.stage == self.game_state.CONTINUE_MOVE):
            self.remove_mark()
            ai_end_row = self.game_state.chosen_ai_move.end[0]
            ai_end_col = self.game_state.chosen_ai_move.end[1]
            self.game_state.move_occurs(ai_end_row, ai_end_col)
            if self.game_state.is_king_upgrading_move(ai_end_row):
                ai_pre_row = self.game_state.clicks[0][0]
                ai_pre_col = self.game_state.clicks[0][1]
                self.game_state.squares[ai_pre_row][ai_pre_col].become_king()
            self.game_state.update_board()
            self.game_state.reset_endlocations_lst()
            self.game_state.reset_valid_move_lst()
            self.draw_board()
            self.game_state.a_piece_move(ai_end_row, ai_end_col)
            if (self.game_state.chosen_ai_move.is_capt and
               self.game_state.contain_cpt_move(self.game_state.valid_moves)):
                self.game_state.stage_of_continue_move()
                self.game_state.selection_occurs(ai_end_row, ai_end_col)
                self.game_state.get_cpt_end_locations()
                self.draw_highlighting_mark()
                self.game_state.get_random_ai_move(self.game_state.valid_moves)
            else:
                self.game_state.switch_turn()
                self.game_state.all_pieces_move()
                self.game_state.stage_of_selection()
                self.indicator_display()
                self.screen.onclick(self.click_handler)
                if self.game_state.game_over():
                    print("Game Over. You lost!")
                    self.screen.onclick(None)
