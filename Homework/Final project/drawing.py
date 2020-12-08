'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

This code is drawing UI class.
'''
import turtle


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
        self.initial_board()
        self.black_turn_notion()

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
    
    def black_pieces_starting_row(self, row):
        '''
            Method -- black_pieces_starting_row
                Checks if the row is the starting position of black pieces, which 
                is from the bottom row of the board to row 2 (the bottom row of the 
                board is counted row 0).
            Parameters:
                row -- the row number
            Returns:
                True if the row is one of the starting row of black pieces, False
                otherwise.
        '''
        LOWEREST_BLACK_STARTING_ROW = 0
        HIGHEST_BLACK_STARTING_ROW = 2
        return (row <= HIGHEST_BLACK_STARTING_ROW and
                row >= LOWEREST_BLACK_STARTING_ROW)
        
    def red_pieces_starting_row(self, row):
        '''
            Method -- red_pieces_starting_row
                Checks if the row is the starting position of red pieces, which is
                from the top row of the board to row 5 (the bottom row of the board
                is counted row 0).
            Parameters:
                row -- the row number
            Returns:
                True if the row is one of the starting row of red pieces, False
                otherwise.
        '''
        LOWEREST_RED_STARTING_ROW = 5
        HIGHEST_RED_STARTING_ROW = 7
        return row >= LOWEREST_RED_STARTING_ROW and row <= HIGHEST_RED_STARTING_ROW

    def draws_nonfilled_square(self, size):
        RIGHT_ANGLE = 90
        self.pen.pendown()
        for i in range(4):
            self.pen.forward(size)
            self.pen.left(RIGHT_ANGLE)
        self.pen.penup()
    
    def choosing_notation(self, row, col, valid_end_locations):
        CHOOSING_COLOR = "light green"
        ORIGINAL_COLOR = "black"
        HINT_COLOR = "red"

        self.pen.setposition(self.CORNER + col * self.SQUARE, self.CORNER + row * self.SQUARE)
        self.pen.color(CHOOSING_COLOR)
        self.draws_nonfilled_square(self.SQUARE)

        self.pen.color(HINT_COLOR)
        for end_location in valid_end_locations:
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

    def move_piece(self, current_player, piece_location, new_location, piece):
        BLACK_PLAYER = "b"
        RED_PLAYER = "r"

        pre_row = piece_location[0]
        pre_col = piece_location[1]
        post_row = new_location[0]
        post_col = new_location[1]
        self.pen.color("black", self.SQUARE_COLORS[0])
        self.pen.setposition(self.CORNER + self.SQUARE * pre_col,
                             self.CORNER + self.SQUARE * pre_row)
        self.draw_square(self.SQUARE)
        if current_player == BLACK_PLAYER:
            self.pen.color(self.PIECE_COLORS[0], self.PIECE_COLORS[0])
        else:
            self.pen.color(self.PIECE_COLORS[1], self.PIECE_COLORS[1])
        self.pen.setposition(self.CORNER + self.SQUARE * post_col + self.CIRCLE_RADIUS,
                             self.CORNER + self.SQUARE * post_row)
        self.draw_circle(self.CIRCLE_RADIUS)
        if piece.is_king:
            self.king_mark(post_row, post_col)

    def cpt_move_piece(self, current_player, piece_location, new_location, piece):
        MIDDLE = 0.5
        self.move_piece(current_player, piece_location, new_location, piece)
        self.pen.color("black", self.SQUARE_COLORS[0])

        removed_row = (piece_location[0] + new_location[0]) * MIDDLE
        removed_col = (piece_location[1] + new_location[1]) * MIDDLE
        self.pen.setposition(self.CORNER + self.SQUARE * removed_col,
                             self.CORNER + self.SQUARE * removed_row)
        self.draw_square(self.SQUARE)

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

        for col in range(self.NUM_SQUARES):
            for row in range(self.NUM_SQUARES):
                if col % 2 != row % 2:
                    self.pen.color("black", self.SQUARE_COLORS[0])
                    self.pen.setposition(self.CORNER + self.SQUARE * col, self.CORNER + self.SQUARE * row)
                    self.draw_square(self.SQUARE)
                    if (self.black_pieces_starting_row(row) or
                        self.red_pieces_starting_row(row)):
                        if self.black_pieces_starting_row(row):
                            self.pen.color(self.PIECE_COLORS[0], self.PIECE_COLORS[0])
                        else:
                            self.pen.color(self.PIECE_COLORS[1], self.PIECE_COLORS[1])
                        self.pen.setposition(self.CORNER + self.SQUARE * col + self.CIRCLE_RADIUS,
                                             self.CORNER + self.SQUARE * row)
                        self.draw_circle(self.CIRCLE_RADIUS)
    
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

