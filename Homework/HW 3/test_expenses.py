from expenses import (calculate_mileage, get_reimbursement_amount,
                      get_actual_mileage_rate, get_actual_trip_cost)


def test_calculate_mileage():
    assert(calculate_mileage(-500, 1000) == 0)
    assert(calculate_mileage(0, 1000) == 0)
    assert(calculate_mileage(1000, 500) == 0)
    assert(calculate_mileage(-1000, -500) == 0)
    assert(calculate_mileage(0, 0) == 0)
    assert(calculate_mileage(1000, -500) == 0)
    assert(calculate_mileage(1000, 1010) == 10)
    assert(calculate_mileage(750, 1250) == 500)
    assert(calculate_mileage(646, 793) == 147)


def test_get_reimbursement_amount():
    assert(get_reimbursement_amount(10) == 5.75)
    assert(get_reimbursement_amount(0) == 0)
    assert(get_reimbursement_amount(25) == 14.38)
    assert(get_reimbursement_amount(100) == 57.5)


def test_get_actual_mileage_rate():
    assert(get_actual_mileage_rate(36.5, 3.09) == 0)
    assert(get_actual_mileage_rate(36, 2) == 0)
    assert(get_actual_mileage_rate(36, -3.09) == 0)
    assert(get_actual_mileage_rate(-36, 3.09) == 0)
    assert(get_actual_mileage_rate(-36, -3.09) == 0)
    assert(get_actual_mileage_rate(36, 3.09) == 0.0858)
    assert(get_actual_mileage_rate(36, 0) == 0)
    assert(get_actual_mileage_rate(46, 2.854) == 0.062)
    assert(get_actual_mileage_rate(57, 4.76) == 0.0835)


def test_get_actual_trip_cost():
    assert(get_actual_trip_cost(-500, 1000, 36, 3.09) == 0)
    assert(get_actual_trip_cost(0, 1000, 36, 3.09) == 0)
    assert(get_actual_trip_cost(1000, 500, 36, 3.09) == 0)
    assert(get_actual_trip_cost(1000, -500, 36, 3.09) == 0)
    assert(get_actual_trip_cost(1000, 1010, 36, 3.09) == 0.86)
    assert(get_actual_trip_cost(850, 1025, 45, 2.86) == 11.13)
    assert(get_actual_trip_cost(1355, 1400, 20, 1.55) == 3.49)
    assert(get_actual_trip_cost(1355, 1400, 20.5, 1.55) == 0)
    assert(get_actual_trip_cost(1355, 1400, 20, 2) == 0)
    assert(get_actual_trip_cost(1355, 1400, 20, -1.55) == 0)
    assert(get_actual_trip_cost(1355, 1400, -20, 1.55) == 0)
