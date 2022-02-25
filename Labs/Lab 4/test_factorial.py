from factorial import calculate_factorial


def test_log_base_2():
    assert(calculate_factorial(1) == 1)
    assert(calculate_factorial(3) == 6)
    assert(calculate_factorial(4) == 24)
    assert(calculate_factorial(8) == 40320)
