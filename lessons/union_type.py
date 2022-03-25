"""An example of union types."""

from typing import Union


def log(info: Union[int, str]) -> None:
    """Log is a function that can be either an int or a str argument."""
    if isinstance(info, str):
        print(f"str: {info.lower()}")
    else:
        print(f"int: {info}")
