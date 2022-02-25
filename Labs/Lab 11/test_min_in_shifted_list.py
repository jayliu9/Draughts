from min_in_shifted_list import search_for_min


def test_find_min():
    assert(search_for_min([18, 25, 38, 1, 12, 13]) == 1)
    assert(search_for_min([18, 25, 38, 12, 13]) == 12)
    assert(search_for_min([12, 13, 25, 38]) == 12)
    assert(search_for_min([1]) == 1)
    assert(search_for_min([2, 1]) == 1)
