"""Dictionary related utility functions."""

__author__ = "730431294"

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a table."""
    result: list[dict[str, str]] = []
    file_handle = open(filename, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Return a list of column values."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Form a table with name in first row and column values in the rest."""
    result: dict[str, list[str]] = {}
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
    return result


def head(table: dict[str, list[str]], head: int) -> dict[str, list[str]]:
    """Produce a new column-based table with first N rows."""
    result: dict[str, list[str]] = {}
    key_list: list[str] = list(table.keys())
    value_list: list[list[str]] = list(table.values())
    head_value_list: list[list[str]] = []
    for i in range(0, len(key_list)):
        j: int = 0
        inner_list: list[str] = []
        if head < len(key_list):
            while j < head:
                inner_list.append(value_list[i][j])
                j += 1
            head_value_list.append(inner_list)
        else:
            while j < len(key_list):
                inner_list.append(value_list[i][j])
                j += 1
            head_value_list.append(inner_list)
    k: int = 0
    while k < len(key_list):
        result[key_list[k]] = head_value_list[k]
        k += 1
    return result


def select(table: dict[str, list[str]], a_list: list[str]) -> dict[str, list[str]]:
    """Produce a new table with only selected comlumns."""
    result: dict[str, list[str]] = {}
    key_list: list[str] = list(table.keys())
    value_list: list[list[str]] = list(table.values())
    for i in range(0, len(key_list)):
        if key_list[i] in a_list:
            result[key_list[i]] = value_list[i]
    return result


def concat(table_a: dict[str, list[str]], table_b: dict[str, list[str]]) -> dict[str, list[str]]:
    """Combine two tables together."""
    result: dict[str, list[str]] = {}
    for key in table_a:
        result[key] = table_a[key] 
    for key in table_b:
        if key in result:
            for i in table_b[key]:
                result[key].append(i)
        else:
            result[key] = table_b[key]
    return result


def count(a_list: list[str]) -> dict[str, int]:
    """A function counts the the number of times an element appears in the list."""
    a_dict: dict[str, int] = {}
    for i in a_list:
        if i in a_dict:
            a_dict[i] += 1
        else:
            a_dict[i] = 1
    return a_dict