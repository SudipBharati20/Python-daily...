# Simple Python Project: Letter Slicing Tool

word = input("Enter a word: ")

# first letter
print("First letter:", word[0])

# last letter
print("Last letter:", word[-1])

# first three letters
print("First three letters:", word[:3])

# last three letters
print("Last three letters:", word[-3:])

# middle letters
print("Middle part:", word[1:-1])

# reversed word
print("Reversed word:", word[::-1])