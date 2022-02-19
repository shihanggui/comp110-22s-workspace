"""Unit test for list utility functions."""

__author__ = "730431294"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_empty() -> None:
    """only_even test for no element."""
    a_list: list[int] = []
    assert only_evens(a_list) == []


def test_only_evens_all_evens() -> None:
    """only_even test for elements all even."""
    a_list: list[int] = [2, 4, 6, 8]
    assert only_evens(a_list) == [2, 4, 6, 8]


def test_only_evens_all_odds() -> None:
    """only_even test for elements all odd."""
    a_list: list[int] = [1, 3, 5, 7]
    assert only_evens(a_list) == []


def test_sub_empty() -> None:
    """sub test with edge cases."""
    a_list: list[int] = []
    start: int = 1
    end: int = -1
    assert sub(a_list, start, end) == []


def test_sub_full_list() -> None:
    """sub test for full list."""
    a_list: list[int] = [1, 2, 4, 5]
    start: int = -1
    end: int = len(a_list) + 1
    assert sub(a_list, start, end) == [1, 2, 4, 5]


def test_sub_random() -> None:
    """sub test for a random subset."""
    a_list: list[int] = [21, 24, 16, 13]
    start: int = 1
    end: int = 3
    assert sub(a_list, start, end) == [24, 16]


def test_concat_one_empty() -> None:
    """concat test with one empty list."""
    list_a: list[int] = []
    list_b: list[int] = [2, 3, 5]
    assert concat(list_a, list_b) == [2, 3, 5]


def test_concat_random() -> None:
    """concat test with random lists."""
    list_a: list[int] = [3, 5, 7]
    list_b: list[int] = [2, 3, 5]
    assert concat(list_a, list_b) == [3, 5, 7, 2, 3, 5]


def test_concat_random_converse() -> None:
    """concat test with reversed random lists."""
    list_b: list[int] = [3, 5, 7]
    list_a: list[int] = [2, 3, 5]
    assert concat(list_a, list_b) == [2, 3, 5, 3, 5, 7]
