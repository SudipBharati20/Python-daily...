numbers = [1,1,2,3,3,4,4,5,6,5,6]

unique_list = []

for num in numbers:
    if num not in unique_list:
        unique_list.append(num)

print("Original list:", numbers)
print("Unique list:", unique_list)