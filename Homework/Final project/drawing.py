import turtle

class DrawingUI:
    NUM_SQUARES = 8
    SQUARE = 50
    BOARD_SIZE = NUM_SQUARES * SQUARE
    CORNER = -BOARD_SIZE / 2
    SQUARE_COLORS = ("light gray", "white")
    PIECE_COLORS = ("black", "red")
    CIRCLE_RADIUS = 0.5 * SQUARE
    WINDOW_SIZE = BOARD_SIZE + SQUARE

    def __init__(self):
        self.initial_board()

    def draw_square(self, size):
        '''
            Function -- draw_square
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
            Function -- draw_circle
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
            Function -- black_pieces_starting_row
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
            Function -- red_pieces_starting_row
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
    
    def choosing_notation(self, col, row, valid_moves):
        CHOOSING_COLOR = "green"
        ORIGINAL_COLOR = "black"
        HINT_COLOR = "red"

        self.pen.setposition(CORNER + col * SQUARE, CORNER + row * SQUARE)
        self.pen.color(CHOOSING_COLOR)
        draws_nonfilled_square(self.pen, SQUARE)

        self.pen.color(HINT_COLOR)
        for move in valid_moves:
            next_col = move[0]
            next_row = move[1]
            self.pen.setposition(CORNER + next_col * SQUARE,
                                CORNER + next_row * SQUARE)
            draws_nonfilled_square(self.pen, SQUARE)
        self.pen.color(ORIGINAL_COLOR)

    def move_piece(self, current_color, piece_location, new_location):
        pre_col = piece_location[0]
        pre_row = piece_location[1]
        post_col = new_location[0]
        post_row = new_location[1]
        self.pen.color("black", SQUARE_COLORS[0])
        self.pen.setposition(CORNER + SQUARE * pre_col,
                            CORNER + SQUARE * pre_row)
        self.draw_square(self.pen, SQUARE)
        self.pen.color(current_color, current_color)
        self.pen.setposition(CORNER + SQUARE * post_col + CIRCLE_RADIUS,
                             CORNER + SQUARE * post_row)
        self.draw_circle(self.pen, CIRCLE_RADIUS)

    def initial_board(self):
        turtle.setup(WINDOW_SIZE, WINDOW_SIZE)
        turtle.screensize(BOARD_SIZE, BOARD_SIZE)
        turtle.bgcolor("white")
        turtle.tracer(0, 0)

        self.pen = turtle.Turtle()
        self.pen.penup()
        self.pen.hideturtle()

        for col in range(NUM_SQUARES):
            for row in range(NUM_SQUARES):
                if col % 2 != row % 2:
                    self.pen.color("black", SQUARE_COLORS[0])
                    self.pen.setposition(CORNER + SQUARE * col, CORNER + SQUARE * row)
                    self.draw_square(self.pen, SQUARE)
                    if (self.black_pieces_starting_row(row) or
                        self.red_pieces_starting_row(row)):
                        if self.black_pieces_starting_row(row):
                            self.pen.color(PIECE_COLORS[0], PIECE_COLORS[0])
                        else:
                            self.pen.color(PIECE_COLORS[1], PIECE_COLORS[1])
                        self.pen.setposition(CORNER + SQUARE * col + CIRCLE_RADIUS,
                                        CORNER + SQUARE * row)
                        self.draw_circle(self.pen, CIRCLE_RADIUS)
