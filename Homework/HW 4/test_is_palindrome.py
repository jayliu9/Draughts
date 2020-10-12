from palindrome import is_palindrome


def test_is_palindrome():
    assert(is_palindrome("madam  Im adam") == True)
    assert(is_palindrome("a") == False)
    assert(is_palindrome("RAdar") == True)
    assert(is_palindrome("madam  Im adam") == True)
    assert(is_palindrome("!radar!") == True)
    assert(is_palindrome("1Tenet,tEnEt1") == True)
    assert(is_palindrome("1234567654321") == True)
    assert(is_palindrome("01234321") == False)
    assert(is_palindrome("") == False)
    assert(is_palindrome("       ") == False)
    assert(is_palindrome("a     A") == True)
    assert(is_palindrome("      B") == False)
