from piece import Piece
BLACK = 0
RED = 1
B_RGL_DIRECTION = [[1, -1], [1, 1]]
R_RGL_DIRECTION = [[-1, -1], [-1, 1]]


def test_constructor():
    a_black_piece = Piece(BLACK)
    assert(a_black_piece.color == BLACK)
    assert(a_black_piece.directions == B_RGL_DIRECTION)
    assert(not a_black_piece.is_king)

    a_red_piece = Piece(RED)
    assert(a_red_piece.color == RED)
    assert(a_red_piece.directions == R_RGL_DIRECTION)
    assert(not a_red_piece.is_king)


def test_become_king():
    a_black_piece = Piece(BLACK)
    assert(not a_black_piece.is_king)
    a_black_piece.become_king()
    assert(a_black_piece.is_king)


def test_eq():
