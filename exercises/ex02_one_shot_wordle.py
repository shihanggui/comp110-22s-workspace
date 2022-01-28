"""Exercise 02 one shot wordle."""

__author__ = "730431294"

secret: str = "python"

guess: str = input("What is your 6-letter guess? ")
while len(guess) != len(secret):
    guess: str = input("That was not 6 letters! Try again: ")

word_index: int = 0
emoji: str = ""
white_box: str = "\U00002B1C"
green_box: str = "\U0001F7E9"
yellow_box: str = "\U0001F7E8"

while word_index < len(secret):
    if guess[word_index] == secret[word_index]:
        emoji += green_box
    else:
        Boolean: bool = False
        alternate_index: int = 0
        while not Boolean and alternate_index < len(secret):
            if secret[alternate_index] == guess[word_index]:
                Boolean = True
            else:
                alternate_index += 1
        if Boolean:
            emoji += yellow_box
        else:
            emoji += white_box
    word_index += 1


print(emoji)

if guess == secret:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")