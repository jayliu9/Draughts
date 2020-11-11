from vowelsearch import vowel_in_string, contains_vowel


def test_vowel_in_string():
    assert(vowel_in_string("") is False)
    assert(vowel_in_string("A") is True)
    assert(vowel_in_string("i") is True)
    assert(vowel_in_string("man") is True)
    assert(vowel_in_string("SUN") is True)
    assert(vowel_in_string("apple") is True)
    assert(vowel_in_string("ffff") is False)
    assert(vowel_in_string("1234") is False)
    assert(vowel_in_string("!!!") is False)


def test_contains_vowel():
    assert(contains_vowel([]) is False)
    assert(contains_vowel([""]) is False)
    assert(contains_vowel(["SUN"]) is True)
    assert(contains_vowel(["", "apple", "man"]) is False)
    assert(contains_vowel(["ffff", "apple", "man"]) is False)
    assert(contains_vowel(["man", "ffff", "apple"]) is False)
    assert(contains_vowel(["garage", "apple", "man"]) is True)
    assert(contains_vowel(["THIS", "MAN"]) is True)
    assert(contains_vowel(["THIS", "1234", "MAN", "!!!"]) is False)
