from scores import average, median, lowest, highest


def test_average():
    assert(average([94, 85, 73, 77, 86]) == 83)
    assert(average([94, 85, 73, 77, 86, 95]) == 85)
    assert(average([62, 88, 97, 94, 81]) == 84.4)
    assert(average([62, 81, 88, 94, 97]) == 84.4)
    assert(average([]) == 0)


def test_median():
    assert(median([94, 85, 73, 77, 86]) == 85)
    assert(median([94, 85, 73, 77, 86, 95]) == 85.5)
    assert(median([62, 88, 97, 94, 81]) == 88)
    assert(median([62, 81, 88, 94, 97]) == 88)
    assert(median([]) == 0)


def test_lowest():
    assert(lowest([94, 85, 73, 77, 86]) == 73)
    assert(lowest([94, 85, 73, 77, 86, 95]) == 73)
    assert(lowest([62, 88, 97, 94, 81]) == 62)
    assert(lowest([62, 81, 88, 94, 97]) == 62)
    assert(lowest([]) == 0)


def test_highest():
    assert(highest([94, 85, 73, 77, 86]) == 94)
    assert(highest([94, 85, 73, 77, 86, 95]) == 95)
    assert(highest([62, 88, 97, 94, 81]) == 97)
    assert(highest([62, 81, 88, 94, 97]) == 97)
    assert(highest([]) == 0)
