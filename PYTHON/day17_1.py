# Simple Python Project: Name Analyzer
# This program asks the user for their name
# It uses letter slicing and arithmetic to analyze the name

name = input("Enter your name: ")

# length of the name
length = len(name)

print("\nYour name is:", name)
print("Total letters in your name:", length)

# letter slicing
print("First letter:", name[0])
print("Last letter:", name[-1])
print("First three letters:", name[:3])
print("Last three letters:", name[-3:])

# arithmetic with length
double_length = length * 2
half_length = length / 2
square_length = length ** 2

print("\nSome calculations using your name length:")
print("Length × 2 =", double_length)
print("Length ÷ 2 =", half_length)
print("Length squared =", square_length)

# fun message
print("\nFun fact:")
print("If each letter was worth 10 points, your name score would be:", length * 10)