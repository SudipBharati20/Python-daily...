
n = int(input("How many numbers do you want to enter? "))
numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

even_sum = 0
odd_sum = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_sum += num

print("Numbers in list:", numbers)
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)