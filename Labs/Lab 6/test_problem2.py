from problem2 import get_gcd, get_n_gcd


def test_get_gcd():
    assert(get_gcd(0, 12) == 12)
    assert(get_gcd(12, 0) == 12)
    assert(get_gcd(12, 8) == 4)
    assert(get_gcd(8, 12) == 4)
    assert(get_gcd(0, 0) == 0)
    assert(get_gcd(12, 12) == 12)


def test_get_n_gcd():
    assert(get_n_gcd([0, 12, 20, 28]) == 4)
    assert(get_n_gcd([0]) == 0)
    assert(get_n_gcd([12, 8]) == 4)
    assert(get_n_gcd([12, 0, 28, 20]) == 4)
    assert(get_n_gcd([12]) == 12)
    assert(get_n_gcd([6, 27, 18, 30, 15, 96]) == 3)
