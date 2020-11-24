'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is the first milestone of the final project
'''
from gamestate import GameState
from drawing import DrawingUI
import turtle
NUM_SQUARES = 8
SQUARE = 50
BOARD_SIZE = NUM_SQUARES * SQUARE
CORNER = -BOARD_SIZE / 2
SQUARE_COLORS = ("light gray", "white")
PIECE_COLORS = ("black", "red")
TURN_STARTED = 0
PIECE_SELECTED = 1
MOVE_SELECTED = 2
EMPTY = ""
BLACK = "b"
RED = "r"

game_state = GameState()
board_ui = DrawingUI()

def click_handler(x, y):
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
    try:
        #click_validator(x, y)
        #print("Clicked at", x, y)
        index_lst = calculates_index(x, y)
        col = index_lst[0]
        row = index_lst[1]
        if game_state.stage == TURN_STARTED:
            if game_state.contains_cur_piece:
                game_state.changes_stage()
        elif game_state.stage == PIECE_SELECTED:
            game_state.ready_to_move(col, row)
            game_state.psb_noncpt_move(col, row)
            board_ui.choosing_notation(col, row, game_state.valid_moves)
            game_state.changes_stage()
        elif game_state.stge == MOVE_SELECTED:
            if is_psb_move(col, row, game_state.valid_moves):
                game_state.after_move(col, row)
                pre_location = game_state.clicks[0]
                new_location = game_state.clicks[1]
                if game_state.current_player == BLACK:
                    board_ui.move_piece("black", pre_location, new_location)
                else:
                    board_ui.move_piece("red", pre_location, new_location)

    except:
        print("Clicked out of range")


def click_validator(x, y):
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
    out_of_bounds = x < CORNER or x > -CORNER or y > -CORNER or y < CORNER
    if out_of_bounds:
        raise ValueError


def calculates_index(x, y):
    col = calculates_col(x)
    row = calculates_row(y)
    return [col, row]


def calculates_col(x):
    return (x - CORNER) // SQUARE


def calculates_row(y):
    return (y - CORNER) // SQUARE


    
def choose_piece(board_ui, gamestate, col, row):
    if gamestate.contains_cur_piece(col, row):
        valid_noncpt_moves = gamestate.psb_noncpt_move(
            col, row, gamestate.current_player)
        #choosing_notation(a_turtle, col, row, valid_noncpt_moves)
    return valid_noncpt_moves


def is_psb_move(col, row, valid_moves):
    return [col, row] in valid_moves


#def non_cpt_move(a_turtle, gamestate, col, row, valid_moves):
   #if is_psb_move(col, row, valid_moves):

        
def main():
    CIRCLE_RADIUS = 0.5 * SQUARE
    WINDOW_SIZE = BOARD_SIZE + SQUARE

    turtle.setup(WINDOW_SIZE, WINDOW_SIZE)
    turtle.screensize(BOARD_SIZE, BOARD_SIZE)
    turtle.bgcolor("white")
    turtle.tracer(0, 0)

    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()

    pen.color("black", "white")
    pen.setposition(CORNER, CORNER)
    draw_square(pen, BOARD_SIZE)

    for col in range(NUM_SQUARES):
        for row in range(NUM_SQUARES):
            if col % 2 != row % 2:
                pen.color("black", SQUARE_COLORS[0])
                pen.setposition(CORNER + SQUARE * col, CORNER + SQUARE * row)
                draw_square(pen, SQUARE)
                if (black_pieces_starting_row(row) or
                    red_pieces_starting_row(row)):
                    if black_pieces_starting_row(row):
                        pen.color(PIECE_COLORS[0], PIECE_COLORS[0])
                    else:
                        pen.color(PIECE_COLORS[1], PIECE_COLORS[1])
                    pen.setposition(CORNER + SQUARE * col + CIRCLE_RADIUS,
                                    CORNER + SQUARE * row)
                    draw_circle(pen, CIRCLE_RADIUS)

    screen = turtle.Screen()
    screen.onclick(click_handler)
    turtle.done()


if __name__ == "__main__":
    main()
