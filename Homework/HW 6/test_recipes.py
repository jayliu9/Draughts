from recipes import (ingredient_validator, ingredient_processor,
                     not_empty_string, time_validator, create_filename,
                     removal, filename_validator, create_content_lst)
from pytest import raises


def test_ingredient_validator():
    with raises(ValueError):
        ingredient_validator([""])
    with raises(ValueError):
        ingredient_validator(["", "", ""])


def test_ingredient_processor():
    assert(ingredient_processor("") == [""])
    assert(ingredient_processor(",")) == ["", ""]
    assert(ingredient_processor("  slices of bread  ") == ["slices of bread"])
    assert(ingredient_processor("   2 slices of bread,  2 tbsp peanut butter ")
           == ["2 slices of bread", "2 tbsp peanut butter"])


def test_not_empty_string():
    assert(not_empty_string("") is False)
    assert(not_empty_string("potatoes") is True)
    assert(not_empty_string("a") is True)


def test_time_validator():
    with raises(ValueError):
        time_validator(-5)
    with raises(ValueError):
        time_validator(-50)


def test_removal():
    assert(removal("") == "")
    assert(removal("!!!") == "")
    assert(removal("tomato!!_soup!_1") == "tomato_soup_1")
    assert(removal("soup") == "soup")


def test_create_filename():
    assert(create_filename("") == ".txt")
    assert(create_filename("   ") == ".txt")
    assert(create_filename("tomato soup 1") == "tomato_soup_1.txt")
    assert(create_filename("   Tomato   ") == "tomato.txt")
    assert(create_filename("   Tomato@# ^&1    ") == "tomato_1.txt")
    assert(create_filename("_tomato_soup_") == "_tomato_soup_.txt")


def filename_validator():
    with raises(ValueError):
        filename_validator(".txt")


def test_create_content_lst():
    assert(create_content_lst("soup", ["Water"], "30", "") == [
        "soup\n", "\n", "Ingredients:\n", "Water\n", "\n",
        "Time: 30 minutes\n", "\n", "Directions:\n", ""])
    assert(create_content_lst(
        "tomato soup", ["2 tomatoes", "water"], "45",
        "Heat the contents of the can until it's warm.") == [
            "tomato soup\n", "\n", "Ingredients:\n", "2 tomatoes\n", "water\n",
            "\n", "Time: 45 minutes\n", "\n", "Directions:\n",
            "Heat the contents of the can until it's warm."])
