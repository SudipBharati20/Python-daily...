# Take user's name as input
name = input("Enter your name: ")

# Letter slicing
first_letter = name[0]
last_letter = name[-1]
first_three = name[:3]
last_three = name[-3:]

# Count total letters
length = len(name)

# Simple arithmetic with length
double_length = length * 2
square_length = length ** 2

# Output results
print("\n--- Name Analysis ---")
print("Your name:", name)
print("First letter:", first_letter)
print("Last letter:", last_letter)
print("First three letters:", first_three)
print("Last three letters:", last_three)

print("\n--- Letter Count ---")
print("Total letters:", length)
print("Double of letters:", double_length)
print("Square of letters:", square_length)