from gamestate import GameState
from piece import Piece
from move import Move
BLACK = 0
RED = 1
CONTINUE_MOVE_SELECTED = 2
PIECE_SELECTED = 0
MOVE_SELECTED = 1
INITIAL_CLICK_LIST = [[0, 0], [0, 0]]


def test_constructor():
    game = GameState()
    black_p = Piece(BLACK)
    red_p = Piece(RED)
    squares = [
        [-1, black_p, -1, black_p, -1, black_p, -1, black_p],
        [black_p, -1, black_p, -1, black_p, -1, black_p, -1],
        [-1, black_p, -1, black_p, -1, black_p, -1, black_p],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [red_p, -1, red_p, -1, red_p, -1, red_p, -1],
        [-1, red_p, -1, red_p, -1, red_p, -1, red_p],
        [red_p, -1, red_p, -1, red_p, -1, red_p, -1]
    ]
    all_move_list = [
        Move([2, 1], [3, 0], False),
        Move([2, 1], [3, 2], False),
        Move([2, 3], [3, 2], False),
        Move([2, 3], [3, 4], False),
        Move([2, 5], [3, 4], False),
        Move([2, 5], [3, 6], False),
        Move([2, 7], [3, 6], False),
    ]
    assert(game.squares == squares)
    assert(game.current_player == BLACK)
    assert(game.stage == PIECE_SELECTED)
    assert(game.clicks == INITIAL_CLICK_LIST)
    assert(game.valid_moves == [])
    assert(game.valid_end_locations == [])
    assert(game.all_move_lst == all_move_list)
    assert(game.chosen_ai_move is None)


def test_contain_any_piece():
    game = GameState()
    assert(game.contain_any_piece(0, 7))
    assert(game.contain_any_piece(6, 3))
    assert(not game.contain_any_piece(3, 4))


def test_contain_cur_piece():
    game = GameState()
    assert(game.contain_cur_piece(0, 7))
    assert(not game.contain_cur_piece(6, 3))
    assert(not game.contain_cur_piece(3, 4))

    game.switch_turn()

    assert(not game.contain_cur_piece(0, 7))
    assert(game.contain_cur_piece(6, 3))
    assert(not game.contain_cur_piece(3, 4))


def test_out_of_index():
    game = GameState()
    assert(game.out_of_index(-1, 0))
    assert(game.out_of_index(10, 3))
    assert(not game.out_of_index(6, 4))
    assert(game.out_of_index(-1, 8))


def test_psb_noncpt_move():
    game = GameState()
    # If the black piece in 2, 1 is selected
    assert(game.psb_noncpt_move(2, 1) == [Move([2, 1], [3, 0], False),
                                          Move([2, 1], [3, 2], False)])

    # If the black piece in 0, 3 is selected
    assert(game.psb_noncpt_move(0, 3) == [])


def test_psb_cpt_move():
    game = GameState()
    black_p = Piece(BLACK)
    red_p = Piece(RED)

    # For the black piece in 2, 1 and the black piece in 2, 3
    # assume that there exist a capturing move in the state of board.
    game.squares = [
        [-1, black_p, -1, black_p, -1, black_p, -1, black_p],
        [black_p, -1, black_p, -1, black_p, -1, black_p, -1],
        [-1, black_p, -1, black_p, -1, black_p, -1, black_p],
        [-1, -1, red_p, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, red_p, -1, red_p, -1, red_p, -1],
        [-1, red_p, -1, red_p, -1, red_p, -1, red_p],
        [red_p, -1, red_p, -1, red_p, -1, red_p, -1]
    ]

    assert(game.psb_cpt_move(2, 1) == [Move([2, 1], [4, 3], True)])
    assert(game.psb_cpt_move(2, 3) == [Move([2, 3], [4, 1], True)])
    assert(game.psb_cpt_move(2, 5) == [])


def test_is_empty_lst():
    game = GameState()
    assert(game.is_empty_lst([]))
    assert(not game.is_empty_lst([[4, 1], [4, 3]]))


def test_a_piece_move():
    game = GameState()
    black_p = Piece(BLACK)
    red_p = Piece(RED)

    # For the black piece in 2, 1
    # assume that there exist a capturing move in the state of board.
    game.squares = [
        [-1, black_p, -1, black_p, -1, black_p, -1, black_p],
        [black_p, -1, black_p, -1, black_p, -1, black_p, -1],
        [-1, black_p, -1, black_p, -1, black_p, -1, black_p],
        [-1, -1, red_p, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, red_p, -1, red_p, -1, red_p, -1],
        [-1, red_p, -1, red_p, -1, red_p, -1, red_p],
        [red_p, -1, red_p, -1, red_p, -1, red_p, -1]
    ]

    assert(game.valid_moves == [])
    assert(game.valid_end_locations == [])
    # If the black piece in 2, 1 is considered to be moved
    game.a_piece_move(2, 1)
    assert(game.valid_moves == [Move([2, 1], [4, 3], True),
                                Move([2, 1], [3, 0], False)])
    assert(game.valid_end_locations == [[4, 3], [3, 0]])

    # If the black piece in 2, 7 is considered to be moved
    game.a_piece_move(2, 7)
    assert(game.valid_moves == [Move([2, 7], [3, 6], False)])
    assert(game.valid_end_locations == [[3, 6]])

    # If the black piece in 0, 1 is considered to be moved
    game.a_piece_move(0, 1)
    assert(game.valid_moves == [])
    assert(game.valid_end_locations == [])


def test_reset_endlocations_lst():
    game = GameState()
    # If the black piece in 2, 1 is considered to be moved
    game.a_piece_move(2, 1)
    # Then clear the end locations list.
    game.reset_endlocations_lst()
    assert(game.valid_end_locations == [])


def test_reset_valid_move_lst():
    game = GameState()
    # If the black piece in 2, 1 is considered to be moved
    game.a_piece_move(2, 1)
    # Then clear the valid moves list.
    game.reset_valid_move_lst()
    assert(game.valid_moves == [])


def test_all_pieces_move():
    game = GameState()
    black_p = Piece(BLACK)
    red_p = Piece(RED)
    all_move_list = [
        Move([2, 1], [3, 0], False),
        Move([2, 1], [3, 2], False),
        Move([2, 3], [3, 2], False),
        Move([2, 3], [3, 4], False),
        Move([2, 5], [3, 4], False),
        Move([2, 5], [3, 6], False),
        Move([2, 7], [3, 6], False),
    ]
    assert(game.all_move_lst == all_move_list)

    # For the black piece in 2, 1 and the black piece in 2, 3
    # assume that there exist a capturing move in the state of board.
    game.squares = [
        [-1, black_p, -1, black_p, -1, black_p, -1, black_p],
        [black_p, -1, black_p, -1, black_p, -1, black_p, -1],
        [-1, black_p, -1, black_p, -1, black_p, -1, black_p],
        [-1, -1, red_p, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, red_p, -1, red_p, -1, red_p, -1],
        [-1, red_p, -1, red_p, -1, red_p, -1, red_p],
        [red_p, -1, red_p, -1, red_p, -1, red_p, -1]
    ]
    game.all_pieces_move()
    assert(game.all_move_lst == [Move([2, 3], [4, 1], True),
                                 Move([2, 1], [4, 3], True),
                                 Move([2, 1], [3, 0], False),
                                 Move([2, 3], [3, 4], False),
                                 Move([2, 5], [3, 4], False),
                                 Move([2, 5], [3, 6], False),
                                 Move([2, 7], [3, 6], False)])


def test_update_board():
    game = GameState()
    black_p = Piece(BLACK)
    red_p = Piece(RED)

    updated_squares = [
        [-1, black_p, -1, black_p, -1, black_p, -1, black_p],
        [black_p, -1, black_p, -1, black_p, -1, black_p, -1],
        [-1, black_p, -1, -1, -1, black_p, -1, black_p],
        [-1, -1, -1, -1, black_p, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [red_p, -1, red_p, -1, red_p, -1, red_p, -1],
        [-1, red_p, -1, red_p, -1, red_p, -1, red_p],
        [red_p, -1, red_p, -1, red_p, -1, red_p, -1]
    ]

    game.selection_occurs(2, 3)
    game.move_occurs(3, 4)
    game.update_board()

    assert(game.squares == updated_squares)


def test_selection_occurs():
    game = GameState()
    game.selection_occurs(2, 1)
    assert(game.clicks[0] == [2, 1])


def test_move_occurs():
    game = GameState()
    game.move_occurs(3, 4)
    assert(game.clicks[1] == [3, 4])


def test_stage_of_selection():
    game = GameState()
    # assume that the current turn is in the stage of move selection.
    game.stage = MOVE_SELECTED
    game.stage_of_selection()
    assert(game.stage == PIECE_SELECTED)


def test_stage_of_move():
    game = GameState()
    game.stage_of_move()
    assert(game.stage == MOVE_SELECTED)


def test_stage_of_continue_move():
    game = GameState()
    game.stage_of_continue_move()
    assert(game.stage == CONTINUE_MOVE_SELECTED)


def test_switch_turn():
    game = GameState()
    game.switch_turn()
    assert(game.current_player == RED)
    game.switch_turn()
    assert(game.current_player == BLACK)


def test_is_king_upgrading_move():
    game = GameState()
    assert(not game.is_king_upgrading_move(5))
    assert(game.is_king_upgrading_move(7))

    game.switch_turn()
    assert(not game.is_king_upgrading_move(3))
    assert(game.is_king_upgrading_move(0))


def test_contain_cpt_move():
    game = GameState()
    have_capt_move_list = [Move([2, 3], [4, 1], True),
                           Move([2, 1], [4, 3], True),
                           Move([2, 3], [3, 4], False),
                           Move([2, 5], [3, 4], False)]

    no_capt_move_list = [Move([2, 3], [3, 4], False),
                         Move([2, 5], [3, 4], False),
                         Move([2, 7], [3, 6], False)]

    assert(game.contain_cpt_move(have_capt_move_list))
    assert(not game.contain_cpt_move(no_capt_move_list))


def test_is_cpt_end_location():
    game = GameState()
    black_p = Piece(BLACK)
    red_p = Piece(RED)
    # For the black piece in 2, 1
    # assume that there exist a capturing move in the state of board.
    game.squares = [
        [-1, black_p, -1, black_p, -1, black_p, -1, black_p],
        [black_p, -1, black_p, -1, black_p, -1, black_p, -1],
        [-1, black_p, -1, black_p, -1, black_p, -1, black_p],
        [-1, -1, red_p, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, red_p, -1, red_p, -1, red_p, -1],
        [-1, red_p, -1, red_p, -1, red_p, -1, red_p],
        [red_p, -1, red_p, -1, red_p, -1, red_p, -1]
    ]

    # If the black piece in 2, 1 is considered to be moved
    game.a_piece_move(2, 1)
    assert(game.is_cpt_end_location(4, 3))
    assert(not game.is_cpt_end_location(2, 1))
    assert(not game.is_cpt_end_location(4, 1))


def test_get_cpt_end_locations():
    game = GameState()
    black_p = Piece(BLACK)
    red_p = Piece(RED)
    # For the black piece in 2, 1
    # assume that there exist a capturing move in the state of board.
    game.squares = [
        [-1, black_p, -1, black_p, -1, black_p, -1, black_p],
        [black_p, -1, black_p, -1, black_p, -1, black_p, -1],
        [-1, black_p, -1, black_p, -1, black_p, -1, black_p],
        [-1, -1, red_p, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, red_p, -1, red_p, -1, red_p, -1],
        [-1, red_p, -1, red_p, -1, red_p, -1, red_p],
        [red_p, -1, red_p, -1, red_p, -1, red_p, -1]
    ]
    # If the black piece in 2, 1 is considered to be moved
    game.a_piece_move(2, 1)
    assert(game.valid_end_locations == [[4, 3], [3, 0]])
    game.get_cpt_end_locations()
    assert(game.valid_end_locations == [[4, 3]])

    # If the black piece in 2, 5 is considered to be moved
    game.a_piece_move(2, 5)
    assert(game.valid_end_locations == [[3, 4], [3, 6]])
    game.get_cpt_end_locations()
    assert(game.valid_end_locations == [])


def test_is_psb_end_location():
    game = GameState()

    game.a_piece_move(2, 1)
    assert(game.is_psb_end_location(3, 0))
    assert(game.is_psb_end_location(3, 2))
    assert(not game.is_psb_end_location(3, 6))


def test_all_cur_pieces_captured():
    game = GameState()
    black_p = Piece(BLACK)
    red_p = Piece(RED)
    assert(not game.all_cur_pieces_captured())
    # Assume that all the black pieces are captured on this board
    game.squares = [
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, red_p, -1, red_p, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1]
    ]
    game.all_pieces_move()
    assert(game.all_cur_pieces_captured())


def test_game_over():
    game = GameState()
    black_p = Piece(BLACK)
    red_p = Piece(RED)
    assert(not game.game_over())
    # Assume that all the black pieces are captured on this board
    game.squares = [
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, red_p, -1, red_p, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1]
    ]
    game.all_pieces_move()
    assert(game.game_over())

    # Assume that all the remaining black pieces have no place to move to.
    game.squares = [
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [black_p, -1, -1, -1, -1, -1, -1, -1],
        [-1, red_p, -1, -1, -1, -1, -1, -1],
        [-1, -1, red_p, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1]
    ]
    game.all_pieces_move()
    assert(game.game_over())


def test_get_cpt_moves():
    game = GameState()
    have_capt_move_list = [Move([2, 3], [4, 1], True),
                           Move([2, 1], [4, 3], True),
                           Move([2, 3], [3, 4], False),
                           Move([2, 5], [3, 4], False)]
    no_capt_move_list = [Move([2, 3], [3, 4], False),
                         Move([2, 5], [3, 4], False),
                         Move([2, 7], [3, 6], False)]

    assert(game.get_cpt_moves(have_capt_move_list) ==
           [Move([2, 3], [4, 1], True), Move([2, 1], [4, 3], True)])
    assert(game.get_cpt_moves(no_capt_move_list) == [])
