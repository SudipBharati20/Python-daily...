# ==========================================
# Q1: Write a program to check if a number is even or odd.
# ==========================================

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")


# ==========================================
# Q2: Write a program to find the factorial of a number.
# ==========================================

num = int(input("Enter a number for factorial: "))
fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial is:", fact)


# ==========================================
# Q3: Write a program to reverse a string.
# ==========================================

text = input("Enter a string: ")

reversed_text = text[::-1]

print("Reversed string:", reversed_text)


# ==========================================
# Q4: Write a program to find the largest number in a list.
# ==========================================

numbers = [10, 45, 7, 89, 23]

largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n

print("Largest number is:", largest)


# ==========================================
# Q5: Write a program to count vowels in a string.
# ==========================================

text = input("Enter a string to count vowels: ").lower()
vowels = "aeiou"
count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels:", count)