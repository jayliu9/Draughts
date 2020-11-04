from sizefinder import size_rank, find_size


def test_size_rank():
    assert(size_rank(32.5, 2, 30) == 1.25)
    assert(size_rank(32.5, 3, 34) == -0.5)
    assert(size_rank(56, 3, 26) == 10)


def test_find_size():
    assert(find_size(0) == "S")
    assert(find_size(0.76) == "S")
    assert(find_size(1.25) == "M")
    assert(find_size(-0.5) == "not available")
    assert(find_size(-4.8) == "not available")
    assert(find_size(9.8) == "not available")
    assert(find_size(6) == "not available")
    assert(find_size(5.85) == "XXXL")
    assert(find_size(3.25) == "XL")
    assert(find_size(4) == "XXL")
    assert(find_size(2.1) == "L")
