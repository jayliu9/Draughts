from logarithm import log_base_2


def test_log_base_2():
    assert(log_base_2(1) == 0)
    assert(log_base_2(2) == 1)
    assert(log_base_2(4) == 2)
    assert(log_base_2(1024) == 10)
