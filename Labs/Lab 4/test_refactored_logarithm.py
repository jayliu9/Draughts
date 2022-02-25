from refactored_logarithm import calculate_log


def test_calculate_log():
    assert(calculate_log(1, 9) == 0)
    assert(calculate_log(1024, 2) == 10)
    assert(calculate_log(16, 4) == 2)
    assert(calculate_log(125, 5) == 3)
    