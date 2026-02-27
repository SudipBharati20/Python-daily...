

# -------------------------------------------------
# Q1: Take a number and print its square.
# -------------------------------------------------
num = int(input("Enter a number: "))
print("Square is:", num * num)


# -------------------------------------------------
# Q2: Take two numbers and print their sum.
# -------------------------------------------------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)


# -------------------------------------------------
# Q3: Take a number and print table of that number.
# -------------------------------------------------
num = int(input("Enter number for table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)


# -------------------------------------------------
# Q4: Print numbers from 1 to 10.
# -------------------------------------------------
for i in range(1, 11):
    print(i)


# -------------------------------------------------
# Q5: Take a string and print it in uppercase.
# -------------------------------------------------
text = input("Enter a string: ")
print("Uppercase:", text.upper())


# -------------------------------------------------
# Q6: Count length of a string.
# -------------------------------------------------
text = input("Enter a string: ")
print("Length is:", len(text))


# -------------------------------------------------
# Q7: Take a number and print its cube.
# -------------------------------------------------
num = int(input("Enter a number: "))
print("Cube is:", num ** 3)


# -------------------------------------------------
# Q8: Print first 5 even numbers.
# -------------------------------------------------
for i in range(2, 11, 2):
    print(i)


# -------------------------------------------------
# Q9: Take a number and print its reverse.
# -------------------------------------------------
num = input("Enter a number: ")
print("Reverse is:", num[::-1])


# -------------------------------------------------
# Q10: Take 5 numbers and store them in a list, then print the list.
# -------------------------------------------------
numbers = []
for i in range(5):
    n = int(input("Enter number: "))
    numbers.append(n)

print("Your list is:", numbers)
