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
import random
import time

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
        remove_hint(game_state.clicks[0], game_state.valid_end_locations)
        if game_state.stage == game_state.PIECE_SELECTED:
            if game_state.contains_cur_piece(row, col):
                game_state.selection_occurs(row, col)
                game_state.a_piece_move(row, col)
                board_ui.choosing_notation(row, col, game_state.valid_end_locations)
                game_state.stage_of_move()

        elif game_state.stage == game_state.MOVE_SELECTED or game_state.stage == game_state.CONTINUE_MOVE_SELECTED:
            if contains_cpt_move(game_state.all_move_lst):
                if is_cpt_move(row, col, game_state.valid_moves):
                    game_state.move_occurs(row, col)
                    board_ui.screen.onclick(None)
                    if game_state.is_king_upgrading_move(row, col):
                        pre_row = game_state.clicks[0][0]
                        pre_col = game_state.clicks[0][1]
                        game_state.squares[pre_row][pre_col].becomes_king()
                    game_state.updates_board(row, col)
                    game_state.reset_endlocations_lst()
                    game_state.reset_valid_move_lst()
                    pre_location = game_state.clicks[0]
                    new_location = game_state.clicks[1]
                    moved_piece = game_state.squares[row][col]
                    board_ui.cpt_move_piece(game_state.current_player, pre_location, new_location, moved_piece)

                    game_state.a_piece_move(row, col)
                    if contains_cpt_move(game_state.valid_moves):
                        game_state.stage_of_continue_move()
                        game_state.selection_occurs(row, col)
                        cpt_end_locations = gets_cpt_end_locations(game_state.valid_moves)
                        board_ui.choosing_notation(row, col, cpt_end_locations)
                    else:
                        game_state.switches_turn()
                        game_state.all_pieces_move()
                        game_state.stage_of_selection()
                elif game_state.contains_cur_piece(row, col):
                    game_state.a_piece_move(row, col)
                    if game_state.stage == game_state.MOVE_SELECTED:
                        game_state.selection_occurs(row, col)
                        board_ui.choosing_notation(row, col, game_state.valid_end_locations)
                    elif row == game_state.clicks[0][0] and col == game_state.clicks[0][1]:
                        cpt_end_locations = gets_cpt_end_locations(game_state.valid_moves)
                        board_ui.choosing_notation(row, col, cpt_end_locations)    
                else:
                    game_state.reset_endlocations_lst()
                    game_state.reset_valid_move_lst()
                    if game_state.stage == game_state.MOVE_SELECTED:
                        game_state.stage_of_selection()
                    
            elif is_psb_move(row, col, game_state.valid_end_locations):
                    game_state.move_occurs(row, col)
                    board_ui.screen.onclick(None)
                    if game_state.is_king_upgrading_move(row, col):
                        pre_row = game_state.clicks[0][0]
                        pre_col = game_state.clicks[0][1]
                        game_state.squares[pre_row][pre_col].becomes_king()
                    game_state.updates_board(row, col)
                    game_state.reset_endlocations_lst()
                    game_state.reset_valid_move_lst()
                    pre_location = game_state.clicks[0]
                    new_location = game_state.clicks[1]
                    new_row = new_location[0]
                    new_col = new_location[1]
                    moved_piece = game_state.squares[new_row][new_col]
                    board_ui.move_piece(game_state.current_player, pre_location, new_location, moved_piece)


                    game_state.switches_turn()
                    game_state.all_pieces_move()
                    game_state.stage_of_selection()
            elif game_state.contains_cur_piece(row, col):
                game_state.selection_occurs(row, col)
                game_state.a_piece_move(row, col)
                board_ui.choosing_notation(row, col, game_state.valid_end_locations)
            else:
                game_state.reset_endlocations_lst()
                game_state.reset_valid_move_lst()
                game_state.stage_of_selection()
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



def is_psb_move(row, col, valid_end_locations):
    return [row, col] in valid_end_locations


def remove_hint(chosen_piece, valid_end_locations):
    chosen_row = chosen_piece[0]
    chosen_col = chosen_piece[1]
    board_ui.remove_choice_mark(chosen_row, chosen_col)
    for end_location in valid_end_locations:
        row_to_move = end_location[0]
        col_to_move = end_location[1]
        board_ui.remove_move_mark(row_to_move, col_to_move)

def notion_display(current_player):
    if current_player == game_state.RED:
        board_ui.red_turn_notion()
    else:
        board_ui.black_turn_notion()

def is_cpt_move(row, col, move_lst):
    for move in move_lst:
        if move.is_capt and [row, col] == move.end:
            return True
    return False

def contains_cpt_move(move_lst):
    if not is_empty_lst(move_lst):
        return move_lst[0].is_capt
    return False

def is_empty_lst(lst):
    return len(lst) == 0


def gets_cpt_end_locations(move_lst):
    new_list = []
    for move in move_lst:
        if move.is_capt:
            new_list.append(move.end)
    return new_list

def gets_cpt_move(move_lst):
    new_list = []
    for move in move_lst:
        if move.is_capt:
            new_list.append(move)
    return new_list

def back_to_xy(location):
    row = location[0]
    col = location[1]
    x = board_ui.CORNER + col * board_ui.SQUARE
    y = board_ui.CORNER + row * board_ui.SQUARE
    return [x, y]


def ai_single_move(all_possible_moves):
    if contains_cpt_move(all_possible_moves):
        all_possible_moves = gets_cpt_move(all_possible_moves)
    ai_move = random.choice(all_possible_moves)
    start_xy = back_to_xy(ai_move.start)
    end_xy = back_to_xy(ai_move.end)
    #ai_first_click = ai_move.start
    #ai_second_click = ai_move.end
    #print(ai_first_click[0])
    #print(ai_first_click[1])
    #ai_x_start = board_ui.CORNER + ai_first_click[1] * board_ui.SQUARE
    #ai_y_start = board_ui.CORNER + ai_first_click[0] * board_ui.SQUARE
    ai_x_start = start_xy[0]
    ai_y_start = start_xy[1]
    click_handler(ai_x_start, ai_y_start)
    ai_x_end = end_xy[0]
    ai_y_end = end_xy[1]
    click_handler(ai_x_end, ai_y_end)


def ai_continue_move(a_piece_moves):
    cpt_end_lst = gets_cpt_end_locations(a_piece_moves)
    ai_continue_end = random.choice(cpt_end_lst)
    continue_end_xy = back_to_xy(ai_continue_end)
    ai_continue_end_x = continue_end_xy[0]
    ai_continue_end_y = continue_end_xy[1]
    click_handler(ai_continue_end_x, ai_continue_end_y)


def all_cur_pieces_captured():
    are_captured = True
    #have_no_red_piece = True
    #have_no_black_piece = True
    #captured = have_no_black_piece or have_no_red_piece 
    for row in range(game_state.NUM_SQUARES):
        for col in range(game_state.NUM_SQUARES):
            if game_state.contains_cur_piece(row, col):
                are_captured = False
            #if game_state.squares[row][col].color == game_state.BLACK:
                #have_no_black_piece = False
            #elif game_state.squares[row][col].color == game_state.RED:
                #have_no_red_piece = False
    return are_captured


def contains_no_move(all_moves_lst):
    return len(all_moves_lst) == 0


def main():
    #screen = turtle.Screen()
    game_over = False
    
    while not game_over:
        if game_state.current_player == game_state.BLACK:
            ai_single_move(game_state.all_move_lst)
            if game_state.stage == game_state.CONTINUE_MOVE_SELECTED:
                ai_continue_move(game_state.valid_moves)
            print(game_state.current_player)
            print(game_state.stage)
            #board_ui.screen.onclick(click_handler)
            #print("hello")
            if all_cur_pieces_captured() or contains_no_move(game_state.all_move_lst):
                print("Black Piece Win!")
                notion_display(game_state.BLACK)
                break
        '''
        elif not contains_cpt_move(game_state.all_move_lst):
            
            ai_move = random.choice(game_state.all_move_lst)
            ai_first_click = ai_move.start
            print(ai_first_click[0])
            print(ai_first_click[1])
            ai_x_start = board_ui.CORNER + ai_first_click[1] * board_ui.SQUARE
            ai_y_start = board_ui.CORNER + ai_first_click[0] * board_ui.SQUARE
            board_ui.screen.ontimer(click_handler(ai_x_start, ai_y_start), 500)
            ai_x_end = board_ui.CON
            ai_x_end
            board_ui.screen.ontimer(click_handler())
            
            board_ui.screen.onclick(click_handler)
            if all_cur_pieces_captured() or contains_no_move(game_state.all_move_lst):
                print("Red Piece Win!")
                notion_display(game_state.RED)
                game_over = True
        '''

    turtle.done()


if __name__ == "__main__":
    main()
