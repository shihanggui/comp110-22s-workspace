"""List Utility Functions."""

__author__ = "730431294"


def only_evens(original_list: list[int]) -> list[int]:
    """The function that returns a list with all even numbers in the original list."""
    new_list: list[int] = []
    for i in original_list:
        if i % 2 == 0:
            new_list.append(i)
    return new_list


def sub(a_list: list[int], start: int, end: int) -> list[int]:
    """The function returns a subset of the list."""
    new_list: list[int] = []
    if len(a_list) == 0 or start > len(a_list) or end <= 0:
        return new_list
    else:
        if start < 0:
            start = 0
        if end > len(a_list):
            end = len(a_list)
        i: int = start
        while i < end:
            new_list.append(a_list[i])
            i += 1
        return new_list


def concat(list_a: list[int], list_b: list[int]) -> list[int]:
    """The function concatentates two lists together."""
    new_list: list[int] = []
    for i in list_a:
        new_list.append(i)
    for j in list_b:
        new_list.append(j)
    return new_list