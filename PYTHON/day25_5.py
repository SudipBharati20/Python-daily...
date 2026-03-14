numbers = [1,2,3,4,5,6]

reverse_list = []

for i in range(len(numbers)-1, -1, -1):
    reverse_list.append(numbers[i])

print("Original list:", numbers)
print("Reversed list:", reverse_list)