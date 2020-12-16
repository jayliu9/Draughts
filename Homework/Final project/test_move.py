from move import Move


def test_constructor():
    a_move = Move([2, 1], [3, 0], False)
    assert(a_move.start == [2, 1])
    assert(a_move.end == [3, 0])
    assert(not a_move.is_capt)

    another_move = Move([6, 1], [4, 3], True)
    assert(another_move.start == [6, 1])
    assert(another_move.end == [4, 3])
    assert(another_move.is_capt)


def test_eq():
    non_capturing_move = Move([2, 1], [3, 0], False)
    capturing_move = Move([6, 1], [4, 3], True)

    assert(non_capturing_move != "a non-capturing move")
    assert(non_capturing_move == Move([2, 1], [3, 0], False))
    assert(non_capturing_move != capturing_move)
