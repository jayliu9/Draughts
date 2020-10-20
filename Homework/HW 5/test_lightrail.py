from lightrail import (is_valid_station, get_direction, get_num_stops,
                       index_difference, good_start_end)


def test_is_valid_station():
    assert(is_valid_station("Angle Lake"))
    assert(not is_valid_station("Bellingham"))
    assert(is_valid_station("SeaTac/Airport"))


def test_get_direction():
    assert(get_direction("University of Washington", "Angle Lake")
           == "Southbound")
    assert(get_direction("Angle Lake", "University of Washington")
           == "Northbound")
    assert(get_direction("University Street", "University Street")
           == "No destination found")


def test_get_num_stops():
    assert(get_num_stops("University of Washington", "Angle Lake") == 15)
    assert(get_num_stops("Angle Lake", "University of Washington") == 15)
    assert(get_num_stops("University Street", "University Street") == 0)
    assert(get_num_stops("University Street", "Tacoma") == 0)


def test_index_difference():
    assert(index_difference("University of Washington", "Angle Lake") == -15)
    assert(index_difference("Angle Lake", "University of Washington") == 15)
    assert(index_difference("University Street", "Stadium") == -3)
    assert(index_difference("Columbia City", "Capitol Hill") == 9)
    assert(get_num_stops("University Street", "University Street") == 0)


def test_good_start_end():
    assert(good_start_end("University Street", "University Street") is False)
    assert(good_start_end("University Street", "Tacoma") is False)
    assert(good_start_end("University of Washington", "Angle Lake") is True)
    assert(good_start_end("Angle Lake", "University of Washington") is True)
    assert(good_start_end("Columbia City", "Capitol Hill") is True)
    assert(good_start_end("Bellingham", "Tacoma") is False)
