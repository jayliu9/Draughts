from problem3 import logarithm, binary_to_decimal


def test_logarithm():
    assert(logarithm(1) == 0)
    assert(logarithm(2) == 1)
    assert(logarithm(8) == 3)
    assert(logarithm(256) == 8)


def test_binary_to_decimal():
    assert(binary_to_decimal("0") == 0)
    assert(binary_to_decimal("1") == 1)
    assert(binary_to_decimal("10010") == 18)
    assert(binary_to_decimal("11111111") == 255)
