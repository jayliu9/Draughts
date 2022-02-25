from upc import contain_only_digits, is_valid_upc


def test_contain_only_digits():
    assert(contain_only_digits("96524") is True)
    assert(contain_only_digits("2") is True)
    assert(contain_only_digits("") is False)
    assert(contain_only_digits(" ") is False)
    assert(contain_only_digits("978 012 805 3904") is False)
    assert(contain_only_digits("9780128053904") is True)
    assert(contain_only_digits("!96522") is False)
    assert(contain_only_digits("aabbcc") is False)
    assert(contain_only_digits("96524aabbcc") is False)
    assert(contain_only_digits("002") is True)
    assert(contain_only_digits("00000") is True)
    assert(contain_only_digits("2.0") is False)


def test_is_valid_upc():
    assert(is_valid_upc("9780128053904") is True)
    assert(is_valid_upc("96524") is False)
    assert(is_valid_upc("9780128053904ab") is False)
    assert(is_valid_upc("abcd") is False)
    assert(is_valid_upc("978 012 805 3904") is False)
    assert(is_valid_upc("96522") is True)
    assert(is_valid_upc("!96522") is False)
    assert(is_valid_upc("  ") is False)
    assert(is_valid_upc("") is False)
    assert(is_valid_upc("0") is True)
    assert(is_valid_upc("0096522") is True)
    assert(is_valid_upc("0.96522") is False)
