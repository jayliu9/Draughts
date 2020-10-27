from gcd import get_gcd


def test_get_gcd():
    assert(get_gcd(0, 12) == 12)
    assert(get_gcd(12, 0) == 12)
    assert(get_gcd(12, 8) == 4)
    assert(get_gcd(8, 12) == 4)
    assert(get_gcd(0, 0) == 0)
    assert(get_gcd(12, 12) == 12)
