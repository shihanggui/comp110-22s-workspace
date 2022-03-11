"""Dictionary function tests."""

__author__ = "730431294"

from dictionary import invert, favorite_color, count
import pytest


def test_keyerror_invert() -> None:
    """The edge case that returns keyerror."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_empty_invert() -> None:
    """The case of empty dictionary."""
    assert invert({}) == {}


def test_regular_invert() -> None:
    """The regular case."""
    a_dict: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(a_dict) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_regular_favorite_color() -> None:
    """The regular case with a max."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_empty_favorite_color() -> None:
    """The case with empty dictionary input."""
    assert favorite_color({}) == ""


def test_two_max_favorite_color() -> None:
    """The regular case with 2 equal maxes."""
    assert favorite_color({"Mac": "yellow", "Din": "blue"}) == "yellow"


def test_empty_count() -> None:
    """The case with empty list input."""
    assert count([]) == {}


def test_regular_count() -> None:
    """The regular case."""
    assert count(['a', 'b', 'c', 'a']) == {'a': 2, 'b': 1, 'c': 1}


def test_another_count() -> None:
    """Another regular case."""
    assert count(['ab', 'abc', 'abcd', 'abc', 'ab']) == {'ab': 2, 'abc': 2, 'abcd': 1}