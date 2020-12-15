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
    NUM_SQUARES = 8
    SQUARE = 50
    BOARD_SIZE = NUM_SQUARES * SQUARE
    CORNER = -BOARD_SIZE / 2
    SQUARE_COLORS = ("light gray", "white")
    PIECE_COLORS = ("black", "red")
    CIRCLE_RADIUS = 0.5 * SQUARE
    WINDOW_SIZE = BOARD_SIZE + 4 * SQUARE
    KING_MARK_SIZE = 10

    def __init__(self):
        self.game_state = GameState()
        self.initial_board()
        self.black_turn_notion()
        self.screen.onclick(self.click_handler)
        turtle.done()

    def click_handler(self, x, y):
        '''
            Function -- click_handler
                Called when a click occurs.
            Parameters:
                x -- X coordinate of the click. Automatically provided by Turtle.
                y -- Y coordinate of the click. Automatically provided by Turtle.
            Returns:
                Does not and should not return. Click handlers are a special type
                of function automatically called by Turtle. You will not have
                access to anything returned by this function.
        '''
        CAPTURE_MOVE_HINT = "Attention: There exists a capturing move somewhere. Please try again."
        INVALID_MOVE_WARNING = "Warning: Invalid move."
        CONTINUE_CAPTURE_HINT = "Attention: You can continue to capture with the piece you just selected."

        #try:
        if self.game_state.current_player == self.game_state.BLACK:
            #self.click_validator(x, y)
            row = self.get_square(y)
            col = self.get_square(x)
            self.remove_hint()
            if self.game_state.stage == self.game_state.PIECE_SELECTED:
                if self.game_state.contains_cur_piece(row, col):
                    self.game_state.selection_occurs(row, col)
                    self.game_state.a_piece_move(row, col)
                    self.choosing_notation()
                    self.game_state.stage_of_move()
                    

            elif self.game_state.stage == self.game_state.MOVE_SELECTED or self.game_state.stage == self.game_state.CONTINUE_MOVE_SELECTED:
                if self.game_state.contains_cpt_move(self.game_state.all_move_lst):
                    if self.game_state.is_cpt_end_location(row, col):
                        self.game_state.move_occurs(row, col)
                        if self.game_state.is_king_upgrading_move(row):
                            pre_row = self.game_state.clicks[0][0]
                            pre_col = self.game_state.clicks[0][1]
                            self.game_state.squares[pre_row][pre_col].becomes_king()
                        self.game_state.updates_board()
                        self.game_state.reset_endlocations_lst()
                        self.game_state.reset_valid_move_lst()
                        self.draw_board()

                        self.game_state.a_piece_move(row, col)
                        if self.game_state.contains_cpt_move(self.game_state.valid_moves):
                            self.game_state.stage_of_continue_move()
                            self.game_state.selection_occurs(row, col)
                            self.game_state.get_cpt_end_locations()
                            self.choosing_notation()
                        else:
                            self.game_state.switches_turn()
                            self.game_state.all_pieces_move()
                            self.game_state.stage_of_selection()
                    elif self.game_state.contains_cur_piece(row, col):
                        self.game_state.a_piece_move(row, col)
                        if self.game_state.stage == self.game_state.MOVE_SELECTED:
                            self.game_state.selection_occurs(row, col)
                            self.choosing_notation()
                        elif row == self.game_state.clicks[0][0] and col == self.game_state.clicks[0][1]:
                            self.game_state.get_cpt_end_locations()
                            self.choosing_notation()
                        else:
                            print(CONTINUE_CAPTURE_HINT)    
                    else:
                        if self.game_state.stage == self.game_state.MOVE_SELECTED:
                            self.game_state.stage_of_selection()
                            if self.game_state.is_psb_end_location(row, col):
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
                            self.game_state.squares[pre_row][pre_col].becomes_king()
                        self.game_state.updates_board()
                        self.game_state.reset_endlocations_lst()
                        self.game_state.reset_valid_move_lst()
                        self.draw_board()

                        self.game_state.switches_turn()
                        self.game_state.all_pieces_move()
                        self.game_state.stage_of_selection()
                elif self.game_state.contains_cur_piece(row, col):
                    self.game_state.selection_occurs(row, col)
                    self.game_state.a_piece_move(row, col)
                    self.choosing_notation()
                else:
                    print(INVALID_MOVE_WARNING)
                    self.game_state.reset_endlocations_lst()
                    self.game_state.reset_valid_move_lst()
                    self.game_state.stage_of_selection()

            self.notion_display()

        if self.game_state.current_player == self.game_state.RED:
            self.remove_hint()

            if not self.game_state.game_over():
                chosen_ai_move = self.game_state.get_random_ai_move(self.game_state.all_move_lst)
                ai_start_row = chosen_ai_move.start[0]
                ai_start_col = chosen_ai_move.start[1]
                self.game_state.selection_occurs(ai_start_row, ai_start_col)
                self.game_state.a_piece_move(ai_start_row, ai_start_col)
                self.choosing_notation()
                self.game_state.stage_of_move()

                while self.game_state.stage == self.game_state.MOVE_SELECTED or self.game_state.stage == self.game_state.CONTINUE_MOVE_SELECTED:
                    self.remove_hint()
                    print("loop")
                    ai_end_row = chosen_ai_move.end[0]
                    ai_end_col = chosen_ai_move.end[1]
                    self.game_state.move_occurs(ai_end_row, ai_end_col)
                    if self.game_state.is_king_upgrading_move(ai_end_row):
                        ai_pre_row = self.game_state.clicks[0][0]
                        ai_pre_col = self.game_state.clicks[0][1]
                        self.game_state.squares[ai_pre_row][ai_pre_col].becomes_king()
                    self.game_state.updates_board()
                    self.game_state.reset_endlocations_lst()
                    self.game_state.reset_valid_move_lst()
                    self.draw_board()
                    self.game_state.a_piece_move(ai_end_row, ai_end_col)
                    if chosen_ai_move.is_capt and self.game_state.contains_cpt_move(self.game_state.valid_moves):
                        self.game_state.stage_of_continue_move()
                        self.game_state.selection_occurs(ai_end_row, ai_end_col)
                        self.game_state.get_cpt_end_locations()
                        self.choosing_notation()
                        chosen_ai_move = self.game_state.get_random_ai_move(self.game_state.valid_moves)
                    else:
                        self.game_state.switches_turn()
                        self.game_state.all_pieces_move()
                        self.game_state.stage_of_selection()
                self.notion_display()

                if self.game_state.game_over():
                    print("Game Over. You lost!")
                    self.screen.onclick(None)

            else:
                print("Game Over. You win!")
                self.screen.onclick(None)
        #except:
            #print("out of range")


    def get_square(self, coord):
        return int((coord - self.CORNER) // self.SQUARE)


    def remove_hint(self):
        selection_click = self.game_state.clicks[0]
        chosen_row = selection_click[0]
        chosen_col = selection_click[1]
        self.remove_choice_mark(chosen_row, chosen_col)
        for end_location in self.game_state.valid_end_locations:
            row_to_move = end_location[0]
            col_to_move = end_location[1]
            self.remove_move_mark(row_to_move, col_to_move)
    

    def click_validator(self, x, y):
        '''
            Function -- click_validation
                Checks that the click was in bounds of the board.
            Parameters:
                x -- X coordinate of the click. Automatically provided by Turtle.
                y -- Y coordinate of the click. Automatically provided by Turtle.
            Raises:
                ValueError -- If the click was out of bounds of the board.
            Returns:
                Nothing
        '''
        out_of_bounds = x < self.CORNER or x > -self.CORNER or y > -self.CORNER or y < self.CORNER
        if out_of_bounds:
            raise ValueError


    def draw_square(self, size):
        '''
            Method -- draw_square
                Draw a square of a given size.
            Parameters:
                a_turtle -- an instance of Turtle
                size -- the length of each side of the square
            Returns:
                Nothing. Draws a square in the graphics window.
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
                Draw a circle with a given radius.
            Parameters:
                a_turtle -- an instance of Turtle
                size -- the radius of the circle
            Returns:
                Nothing. Draws a circle in the graphics windo.
        '''
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.circle(radius)
        self.pen.end_fill()
        self.pen.penup()
    

    def draw_board(self):
        cells = self.game_state.squares
        for row in range(self.game_state.NUM_SQUARES):
            for col in range(self.game_state.NUM_SQUARES):
                if col % 2 != row % 2:
                    self.pen.color("black", self.SQUARE_COLORS[0])
                    self.pen.setposition(self.CORNER + self.SQUARE * col, self.CORNER + self.SQUARE * row)
                    self.draw_square(self.SQUARE)
                    if self.game_state.contains_any_piece(row, col):
                        a_piece = cells[row][col]
                        piece_color = a_piece.color
                        self.pen.color(self.PIECE_COLORS[piece_color])
                        self.pen.setposition(self.CORNER + self.SQUARE * col + self.CIRCLE_RADIUS, self.CORNER + self.SQUARE * row)
                        self.draw_circle(self.CIRCLE_RADIUS)
                        if a_piece.is_king:
                            self.king_mark(row, col)

    def draws_nonfilled_square(self, size):
        RIGHT_ANGLE = 90
        self.pen.pendown()
        for i in range(4):
            self.pen.forward(size)
            self.pen.left(RIGHT_ANGLE)
        self.pen.penup()
    
    def choosing_notation(self):
        CHOOSING_COLOR = "light green"
        ORIGINAL_COLOR = "black"
        HINT_COLOR = "red"

        selection_click = self.game_state.clicks[0]
        chosen_row = selection_click[0]
        chosen_col = selection_click[1]

        self.pen.setposition(self.CORNER + chosen_col * self.SQUARE, self.CORNER + chosen_row * self.SQUARE)
        self.pen.color(CHOOSING_COLOR)
        self.draws_nonfilled_square(self.SQUARE)

        self.pen.color(HINT_COLOR)
        for end_location in self.game_state.valid_end_locations:
            next_row = end_location[0]
            next_col = end_location[1]
            self.pen.setposition(self.CORNER + next_col * self.SQUARE,
                                 self.CORNER + next_row * self.SQUARE)
            self.draws_nonfilled_square(self.SQUARE)
        self.pen.color(ORIGINAL_COLOR)

    def remove_move_mark(self, row, col):
        self.pen.color("black", self.SQUARE_COLORS[0])
        self.pen.setposition(self.CORNER + col * self.SQUARE, self.CORNER + row * self.SQUARE)
        self.draw_square(self.SQUARE)

    def remove_choice_mark(self, row, col):
        self.pen.color("black")
        self.pen.setposition(self.CORNER + col * self.SQUARE, self.CORNER + row * self.SQUARE)
        self.draws_nonfilled_square(self.SQUARE)

    def initial_board(self):
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

    def notion_frame(self):
        self.pen.color("black", "white")
        self.pen.setposition(self.CORNER - 1 * self.SQUARE, self.CORNER + 3.5 * self.SQUARE)
        self.draw_square(0.5 * self.SQUARE)
        self.pen.setposition(self.CORNER - 1 * self.SQUARE, 0)
        self.draw_square(0.5 * self.SQUARE)

    def black_turn_notion(self):
        self.notion_frame()
        self.pen.color(self.PIECE_COLORS[0], self.PIECE_COLORS[0])
        self.pen.setposition(self.CORNER - 1 * self.SQUARE + 0.5 * self.CIRCLE_RADIUS,
                             self.CORNER + 3.5 * self.SQUARE)
        self.draw_circle(0.5 * self.CIRCLE_RADIUS)
    
    def red_turn_notion(self):
        self.notion_frame()
        self.pen.color(self.PIECE_COLORS[1], self.PIECE_COLORS[1])
        self.pen.setposition(self.CORNER - 1 * self.SQUARE + 0.5 * self.CIRCLE_RADIUS, 0)
        self.draw_circle(0.5 * self.CIRCLE_RADIUS)

    def king_mark(self, row, col):
        self.pen.color("yellow", "yellow")
        self.pen.setposition(self.CORNER + self.SQUARE * col + self.CIRCLE_RADIUS,
                             self.CORNER + self.SQUARE * row + self.CIRCLE_RADIUS - self.KING_MARK_SIZE)
        self.draw_circle(self.KING_MARK_SIZE)

    def notion_display(self):
        if self.game_state.current_player == self.game_state.RED:
            self.red_turn_notion()
        else:
            self.black_turn_notion()
