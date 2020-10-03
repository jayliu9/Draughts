from bill_split import calculate_tip, total, split


def test_calculate_tip():
    assert(calculate_tip(60, 0) == 0)
    assert(calculate_tip(0, 0.5) == 0)
    assert(calculate_tip(60, 1) == 60)
    assert(calculate_tip(100, 0.3) == 30)

def test_total():
    assert(total(60, 0.2) == 72)
    assert(total(100, 0) == 100)
    assert(total(0, 0.5) == 0)
    assert(total(60, 1) == 120)

def test_split():
    assert(split(120, 5) == 24)
    assert(split(0, 5) == 0)
    assert(split(100, 4) == 25)