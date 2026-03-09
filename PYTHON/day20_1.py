# =========================================================
# PYTHON LOOP LEARNING (RUN THIS FILE IN VS CODE)
# Everything is explained using comments
# =========================================================


# ---------------------------------------------------------
# 1. WHAT IS A LOOP?
# A loop repeats a block of code multiple times.
# Python mainly has 2 loops:
# 1. for loop
# 2. while loop
# ---------------------------------------------------------



# ---------------------------------------------------------
# 2. FOR LOOP
# A for loop is used when we know how many times to repeat.
# range(start, stop) generates numbers from start to stop-1
# ---------------------------------------------------------

print("Example 1: Numbers from 1 to 5")

for i in range(1, 6):   # range(1,6) means numbers 1 to 5
    print(i)            # prints the value of i



# ---------------------------------------------------------
# Example 2: Print Hello 5 times
# ---------------------------------------------------------

print("\nExample 2: Print Hello 5 times")

for i in range(5):   # loop runs 5 times
    print("Hello")



# ---------------------------------------------------------
# Example 3: Loop through letters in a word
# ---------------------------------------------------------

print("\nExample 3: Print letters of a word")

name = "Sudip"

for letter in name:   # takes each character from the string
    print(letter)



# ---------------------------------------------------------
# 3. WHILE LOOP
# A while loop runs while the condition is True
# ---------------------------------------------------------

print("\nExample 4: While loop numbers 1 to 5")

i = 1

while i <= 5:   # condition
    print(i)
    i = i + 1   # increase i by 1 to avoid infinite loop



# ---------------------------------------------------------
# 4. BREAK STATEMENT
# break stops the loop immediately
# ---------------------------------------------------------

print("\nExample 5: Break example")

for i in range(1, 10):

    if i == 4:      # when i becomes 4
        break       # stop the loop

    print(i)



# ---------------------------------------------------------
# 5. CONTINUE STATEMENT
# continue skips one iteration
# ---------------------------------------------------------

print("\nExample 6: Continue example")

for i in range(1, 6):

    if i == 3:
        continue   # skip number 3

    print(i)