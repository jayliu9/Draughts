from hangman import (hide_word, letter_guess, word_guess, is_repetition,
                     guessed_so_far)


def test_hide_word():
    assert(hide_word("") == "")
    assert(hide_word("APPLE") == "_____")
    assert(hide_word("OBVIOUS") == "_______")
    assert(hide_word("XYLOPHONE") == "_________")
    assert(hide_word("  ") == "__")


def test_letter_guess():
    assert(letter_guess("A", "APPLE", "_____") == "A____")
    assert(letter_guess("P", "APPLE", "_____") == "_PP__")
    assert(letter_guess("!", "COOL!", "_____") == "____!")
    assert(letter_guess("G", "APPLE", "_____") == "_____")
    assert(letter_guess("1", "1234567", "_______") == "1______")


def test_word_guess():
    assert(word_guess("APPLE", "APPLE") == True)
    assert(word_guess("GRAPE", "APPLE") == False)
    assert(word_guess("APP", "APPLE") == False)
    assert(word_guess("", "APPLE") == False)
    assert(word_guess("  ", "APPLE") == False)


def test_is_repetition():
    assert(is_repetition("A", "AFG") == True)
    assert(is_repetition("G", "AFG") == True)
    assert(is_repetition("C", "AFG") == False)
    assert(is_repetition("!", "AFG") == False)
    assert(is_repetition(" ", "AFG") == False)


def test_guessed_so_far():
    assert(guessed_so_far("AFG", "C") == "AFGC")
    assert(guessed_so_far("AFGC", "!") == "AFGC!")
    assert(guessed_so_far("AFGC", " ") == "AFGC ")
