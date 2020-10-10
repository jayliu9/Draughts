from calculator import calculate_subtotal, judgement_of_quitting


def test_calculate_subtotal():
    assert(calculate_subtotal(10, "+", 2) == 12)
    assert(calculate_subtotal(12, "-", 5) == 7)
    assert(calculate_subtotal(7, "*", 6) == 42)
    assert(calculate_subtotal(42, "/", 10) == 4.2)


def test_judgement_of_quitting():
    assert(judgement_of_quitting("Q") == False)
    assert(judgement_of_quitting("q") == False)
    assert(judgement_of_quitting("+ 2") == True)
    assert(judgement_of_quitting("- 5") == True)
    assert(judgement_of_quitting("* 6") == True)
    assert(judgement_of_quitting("/ 10") == True)
