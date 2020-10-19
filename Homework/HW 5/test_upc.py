from upc import is_valid_upc


def test_is_valid_upc():
    assert(is_valid_upc("9780128053904") is True)
    assert(is_valid_upc("96524") is False)
    assert(is_valid_upc("9780128053904ab") is False)
    assert(is_valid_upc("abcd") is False)
    assert(is_valid_upc("978 012 805 3904") is False)
    assert(is_valid_upc("96522") is True)
    assert(is_valid_upc("!96522") is False)
    assert(is_valid_upc("  ") is False)
    assert(is_valid_upc("000") is True)
    assert(is_valid_upc("") is False)
