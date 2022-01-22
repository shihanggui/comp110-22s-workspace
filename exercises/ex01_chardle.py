"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730431294"

word: str = input("Enter a 5-character word: ")
character: str = input("Enter a single character: ")
print("Searching for", character, "in", word)
index: int = 0

if len(word) != 5:
    print("Word must contain 5 characters")
    exit()

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
else:
    print("{} instance of {} found in {}".format(index, character, word))
