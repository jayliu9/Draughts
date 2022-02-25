from seven_dwarves import (create_network, line_processing, generate_line,
                           generate_text, unfriending, is_empty_list,
                           friending_validator)
from pytest import raises


def test_create_network():
    assert(create_network(["Happy Dopey Bashful"]) ==
           {"Happy": ["Dopey", "Bashful"]})
    assert(create_network(["Happy", "Dopey Bashful", "Bashful Dopey"]) ==
           {"Happy": [], "Dopey": ["Bashful"], "Bashful": ["Dopey"]})


def test_line_processing():
    assert(line_processing("Happy Dopey Bashful") ==
           ["Happy", "Dopey", "Bashful"])
    assert(line_processing("Happy") == ["Happy"])


def test_generate_line():
    dic = {"Happy": [], "Dopey": ["Bashful", "Doc"], "Bashful": ["Dopey"],
           "Doc": ["Dopey"]}
    assert(generate_line("Happy", dic) == "Happy ")
    assert(generate_line("Dopey", dic) == "Dopey Bashful Doc")
    assert(generate_line("Bashful", dic) == "Bashful Dopey")


def test_generate_text():
    dic = {"Happy": [], "Dopey": ["Bashful", "Doc"], "Bashful": ["Dopey"],
           "Doc": ["Dopey", "Sleepy"], "Sleepy": ["Doc"]}
    assert(generate_text(dic) == ["Happy ", "Dopey Bashful Doc",
                                  "Bashful Dopey", "Doc Dopey Sleepy",
                                  "Sleepy Doc"])


def test_unfriending():
    dic = {"Happy": ["Dopey", "Bashful"]}
    unfriending("Happy", "Bashful", dic)
    assert(dic["Happy"] == ["Dopey"])
    unfriending("Happy", "Dopey", dic)
    assert(dic["Happy"] == [])


def test_is_empty_list():
    assert(is_empty_list([]) is True)
    assert(is_empty_list(["Bashful", "Doc"]) is False)


def test_friending_validator():
    with raises(KeyError):
        friending_validator("Tom", ["Happy", "Doc", "Bashful"])
    with raises(ValueError):
        friending_validator("Doc", ["Happy", "Doc", "Bashful"])
