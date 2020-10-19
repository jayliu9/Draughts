from password import secure_password


def test_secure_password():
    assert(secure_password("") is False)
    assert(secure_password("ABCDEFGHI") is False)
    assert(secure_password("EFG1234efg") is False)
    assert(secure_password("EeFfGgHhJjKk") is False)
    assert(secure_password("AaBbCc1234") is False)
    assert(secure_password("AaBbCc1234!") is True)
    assert(secure_password("EeFfGgHh12@!") is True)
    assert(secure_password("1234567890") is False)
    assert(secure_password("Aa123!") is False)
    assert(secure_password("AaBbCcDdEe12345!#@!") is False)
    assert(secure_password("sDfG@12!kK") is True)
    assert(secure_password("$#987ABCabc") is True)
    assert(secure_password("&^987ABCabc") is False)
    assert(secure_password("  Aa123654!@") is False)
    assert(secure_password("OoPp  Q12@#") is False)
