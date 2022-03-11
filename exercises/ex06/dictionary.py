"""Dictionary functions."""

__author__ = "730431294"


def invert(a_dict: dict[str, str]) -> dict[str, str]:
    """A function inverts keys and values of a dictionary."""
    new_dict: dict[str, str] = {}
    new_list: list[str] = []
    for key in a_dict:
        new_list.append(a_dict[key])
    for i in range(0, len(new_list)):
        for j in range(i + 1, len(new_list)):
            if new_list[i] == new_list[j]:
                raise KeyError

    for key in a_dict:
        new_dict[a_dict[key]] = key
    return new_dict


def favorite_color(a_dict: dict[str, str]) -> str:
    """A function returns the favorite color among a group of people."""
    a_list: list[str] = []
    for key in a_dict:
        a_list.append(a_dict[key])
    if len(a_list) == 0:
        return ""
    else:
        counter: int = 0   
        item: str = a_list[0]
        for i in a_list:
            current_counter: int = a_list.count(i)
            if current_counter > counter:
                counter = current_counter
                item = i
        return item


def count(a_list: list[str]) -> dict[str, int]:
    """A function counts the the number of times an element appears in the list."""
    a_dict: dict[str, int] = {}
    for i in a_list:
        if i in a_dict:
            a_dict[i] += 1
        else:
            a_dict[i] = 1
    return a_dict