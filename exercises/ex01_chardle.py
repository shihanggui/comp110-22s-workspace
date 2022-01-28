"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730431294"

word: str = input("Enter a 5-character word: ")

if len(word) != 5:
    print("Error: Word must contain 5 characters")
    exit()

character: str = input("Enter a single character: ")

if len(character) != 1:
    print("Error: Character must be a single character.")
    exit()

print("Searching for", character, "in", word)
index: int = 0

if word[0] == character:
    print(character, "found at index 0")
    index = index + 1

if word[1] == character:
    print(character, "found at index 1")
    index = index + 1

if word[2] == character:
    print(character, "found at index 2")
    index = index + 1

if word[3] == character:
    print(character, "found at index 3")
    index = index + 1

if word[4] == character:
    print(character, "found at index 4")
    index = index + 1

if index == 0:
    print("No instances of {} found in {}".format(character, word))
elif index == 1:
    print("{} instance of {} found in {}".format(index, character, word))
else:
    print("{} instances of {} found in {}".format(index, character, word))
