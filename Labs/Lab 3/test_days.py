from days import num_of_current_day, before_or_on_friday, after_friday


def test_num_of_current_day():
    assert(num_of_current_day("TH") == 4)
    assert(num_of_current_day("F") == 5)
    assert(num_of_current_day("M") ==1)


def test_before_or_on_friday():
    assert(before_or_on_friday("W") == 2)
    assert(before_or_on_friday("TU") == 3)
    assert(before_or_on_friday("F") == 0)


def test_after_friday():
    assert(after_friday("SA") == 6)
    assert(after_friday("SU") == 5)