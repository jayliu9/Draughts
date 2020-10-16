from binary_to_decimal import convert_to_decimal


def test_convert_to_decimal():
    assert(convert_to_decimal("0") == 0)
    assert(convert_to_decimal("11") == 3)
    assert(convert_to_decimal("1101") == 13)
    assert(convert_to_decimal("101100") == 44)
    assert(convert_to_decimal("11111111") == 255)
    assert(convert_to_decimal("1101000110101010") == 53674)