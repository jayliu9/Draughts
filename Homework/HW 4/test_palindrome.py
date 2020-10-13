from palindrome import is_palindrome


def test_is_palindrome():
    assert(is_palindrome("madam  Im adam") is True)
    assert(is_palindrome("a") is False)
    assert(is_palindrome("RAdar") is True)
    assert(is_palindrome("madam  Im adam") is True)
    assert(is_palindrome("!radar!") is True)
    assert(is_palindrome("1Tenet,tEnEt1") is True)
    assert(is_palindrome("1234567654321") is True)
    assert(is_palindrome("01234321") is False)
    assert(is_palindrome("") is False)
    assert(is_palindrome("       ") is False)
    assert(is_palindrome("a     A") is True)
    assert(is_palindrome("      B") is False)
