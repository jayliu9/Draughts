from password import secure_password


def test_secure_password():
    assert(secure_password("") is False)
    assert(secure_password("AB123!") is False)
    assert(secure_password("ABCDEFGHIJ123!") is False)
    assert(secure_password("ABCDEFG123!") is True)
    assert(secure_password("ABCDEFGHI") is False)
    assert(secure_password("1234567890") is False)
    assert(secure_password("abcdefghij") is False)
    assert(secure_password("!!!@@@###$$") is False)
    assert(secure_password("EeFfGgHhJjKk") is False)
    assert(secure_password("1234567890#!") is False)
    assert(secure_password("AAAAABBBBB#!") is False)
    assert(secure_password("aaaaabbbbb#!") is False)
    assert(secure_password("aaaaabbbbbAB") is False)
    assert(secure_password("AAAaaBBBbb!#") is True)
    assert(secure_password("AA123BB123!#") is True)
    assert(secure_password("Aa12Bb12!#") is True)
    assert(secure_password("A1bB1!2a#b") is True)
    assert(secure_password("A1bB1^2a&b") is False)
    assert(secure_password("  Aa123!@") is False)
    assert(secure_password("AaBb !12@#") is False)
