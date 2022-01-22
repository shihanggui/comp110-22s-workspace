"""An example of conditional (if-else) statements."""

SECRET: int = 3

guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guess correctly!")
else:
    print("Guess again.")
print("Game over.")

