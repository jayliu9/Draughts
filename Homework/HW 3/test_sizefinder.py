from sizefinder import size_rank, size_finder


def test_size_rank():
    assert(size_rank(32.5, 2, 30) == 1.25)
    assert(size_rank(32.5, 3, 34) == -0.5)
    assert(size_rank(56, 3, 26) == 10)


def test_size_finder():
    assert(size_finder(0) == "S")
    assert(size_finder(1.25) == "M")
    assert(size_finder(-0.5) == "not available")
    assert(size_finder(6) == "not available")