
# ---------------------------------------------------------
# QUESTION 1
# Write a loop to print numbers 1 to 10
# ---------------------------------------------------------

print("\nQuestion 1 Answer:")

for i in range(1, 11):
    print(i)



# ---------------------------------------------------------
# QUESTION 2
# Print even numbers from 1 to 20
# ---------------------------------------------------------

print("\nQuestion 2 Answer:")

for i in range(1, 21):

    if i % 2 == 0:   # % means remainder
        print(i)



# ---------------------------------------------------------
# QUESTION 3
# Ask the user for a name and print each letter
# ---------------------------------------------------------

print("\nQuestion 3 Answer:")

name = input("Enter your name: ")

for letter in name:
    print(letter)



# ---------------------------------------------------------
# QUESTION 4
# Find sum of numbers from 1 to 100
# ---------------------------------------------------------

print("\nQuestion 4 Answer:")

total = 0

for i in range(1, 101):
    total = total + i

print("Sum =", total)



# ---------------------------------------------------------
# QUESTION 5
# Print pattern
#
# *
# **
# ***
# ****
# *****
# ---------------------------------------------------------

print("\nQuestion 5 Answer:")

for i in range(1, 6):

    for j in range(i):   # nested loop
        print("*", end="")

    print()   # move to next line