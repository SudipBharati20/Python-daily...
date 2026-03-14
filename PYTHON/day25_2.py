n = int(input("How many numbers? "))

numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

maximum = numbers[0]
minimum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

    if num < minimum:
        minimum = num

print("Full list:", numbers)
print("Maximum number:", maximum)
print("Minimum number:", minimum)