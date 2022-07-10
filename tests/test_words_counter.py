import pytest

from words_counter.main import words_frequency


def test_words_frequency_input_type():
    """ Function is supposed to raise ValueError, when input is not List. """
    input_words = ('hello', 'puppy', 123, b'crazy')

    with pytest.raises(ValueError):
        words_frequency(words=input_words)


def test_words_frequency_empty_input():
    """ Function is supposed to return empty List, when input is empty. """
    input_words = []
    assert not words_frequency(words=input_words), 'words_frequency() returns not empty list,' \
                                                   ' even though input was empty.'


def test_words_frequency_input_contains_not_just_str():
    """ Function is supposed to raise ValueError, when input holds not just list of strings. """
    input_words = ['hello', 'puppy', 123, b'crazy']

    with pytest.raises(ValueError):
        words_frequency(words=input_words)


def test_words_frequency_correctness():
    """ Function's output is supposed to match with expected output. """
    input_words = ['hello', 'puppy']

    actual_output = words_frequency(words=input_words)
    expected_output = {'hello': 1, 'puppy': 1}

    assert actual_output == expected_output
