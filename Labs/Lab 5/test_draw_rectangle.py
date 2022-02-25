from draw_rectangle import rows_top_bottom, rows_inside

def test_rows_top_bottom():
    assert(rows_top_bottom(5, "*") == "*****")
    assert(rows_top_bottom(8, "!") == "!!!!!!!!")
    assert(rows_top_bottom(1, "a") == "a")
    assert(rows_top_bottom(6, "3") == "333333")


def test_rows_inside():
    assert(rows_inside(1, "!") == "!")
    assert(rows_inside(2, "*") == "**")
    assert(rows_inside(5, "8") == "8   8")
    assert(rows_inside(8, "c") == "c      c")
