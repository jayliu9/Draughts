'''
Name: Shijie Liu
NUID: 001561546
Course: CS 5001
Course Number: 18529
Semester: Fall 2020

The code is from first milestone to second milestone of the final project
'''
from gamestate import GameState
from drawing import DrawingUI
import turtle

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
        click_validator(x, y)
        print("click at", x, y)
        index_lst = calculates_index(x, y)
        row = index_lst[0]
        col = index_lst[1]

        remove_hint(game_state.clicks[0], game_state.valid_moves)
        if game_state.stage == game_state.PIECE_SELECTED:
            if game_state.contains_cur_piece(row, col):
                game_state.selection_occurs(row, col)
                game_state.psb_noncpt_move(row, col, game_state.current_player)
                board_ui.choosing_notation(row, col, game_state.valid_moves)
                game_state.changes_stage()

        elif game_state.stage == game_state.MOVE_SELECTED:
            if is_psb_move(row, col, game_state.valid_moves):
                game_state.move_occurs(row, col)
                game_state.updates_board(row, col)
                game_state.reset_moves_lst()
                pre_location = game_state.clicks[0]
                new_location = game_state.clicks[1]
                if game_state.current_player == game_state.BLACK:
                    board_ui.move_piece("black", pre_location, new_location)
                else:
                    board_ui.move_piece("red", pre_location, new_location)
                game_state.switches_turn()
                game_state.changes_stage()
            elif game_state.contains_cur_piece(row, col):
                game_state.selection_occurs(row, col)
                game_state.psb_noncpt_move(row, col, game_state.current_player)
                board_ui.choosing_notation(row, col, game_state.valid_moves)
            else:
                game_state.reset_moves_lst()

        notion_display(game_state.current_player)
    except:
        print("out of range")

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
    out_of_bounds = x < board_ui.CORNER or x > -board_ui.CORNER or y > -board_ui.CORNER or y < board_ui.CORNER
    if out_of_bounds:
        raise ValueError


def calculates_index(x, y):
    col = calculates_col(x)
    row = calculates_row(y)
    return [int(row), int(col)]


def calculates_col(x):
    return (x - board_ui.CORNER) // board_ui.SQUARE


def calculates_row(y):
    return (y - board_ui.CORNER) // board_ui.SQUARE



def is_psb_move(row, col, valid_moves):
    return [row, col] in valid_moves


def remove_hint(chosen_piece, valid_moves):
    chosen_row = chosen_piece[0]
    chosen_col = chosen_piece[1]
    board_ui.remove_choice_mark(chosen_row, chosen_col)
    for move in game_state.valid_moves:
        row_to_move = move[0]
        col_to_move = move[1]
        board_ui.remove_move_mark(row_to_move, col_to_move)

def notion_display(current_player):
    if current_player == game_state.RED:
        board_ui.red_turn_notion()
    else:
        board_ui.black_turn_notion()


def main():
    screen = turtle.Screen()
    screen.onclick(click_handler)
    turtle.done()


if __name__ == "__main__":
    main()
