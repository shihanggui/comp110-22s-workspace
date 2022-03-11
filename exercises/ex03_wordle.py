"""Wordle."""

__author__ = "730431294"

secret_word: str = "codes"
input_length: int = len(secret_word)


def contains_char(a: str, b: str) -> bool:
    """Find if a contains b."""
    assert len(b) == 1
    index: int = 0
    while index < len(a):
        if a[index] == b:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Compare the guess with the secret and return an emoji."""
    assert len(guess) == len(secret)
    emoji: str = ""
    word_index: int = 0
    white_box: str = "\U00002B1C"
    green_box: str = "\U0001F7E9"
    yellow_box: str = "\U0001F7E8"
    while word_index < len(guess):
        if guess[word_index] == secret[word_index]:
            emoji += green_box
        elif contains_char(secret, guess[word_index]):
            emoji += yellow_box
        else:
            emoji += white_box
        word_index += 1
    return emoji


def input_guess(length: int) -> str:
    """Give a input of the guess."""
    word_input: str = input(f"Enter a {length} character word: ")
    while len(word_input) != length:
        word_input = input(f"That wasn't {length} chars! Try again: ")
    return word_input


def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    win: bool = False
    while turn <= 6 and not win:
        print(f"===Turn {turn}/6 ===")
        guess_word: str = input_guess(input_length)
        print(emojified(guess_word, secret_word))
        if guess_word == secret_word:
            win = True
            print(f"You won in {turn}/6 turns!")
        else:
            turn += 1
        
    if turn == 7:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()