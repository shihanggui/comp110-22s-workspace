"""Example of a function that searches through a list."""


def main() -> None:
    print(contain('a', ['a']))


def contain(needle: str, haystack: list[str]) -> bool:
    for i in haystack:
        if needle == i:
            return True
    return False


if __name__ == "__main__":
    main()