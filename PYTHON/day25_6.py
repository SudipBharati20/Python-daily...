numbers = [1,2,6,4,5,7,6,7,8,1,4,5]

count_dict = {}

for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

print("Repeated numbers:")

for num in count_dict:
    if count_dict[num] > 1:
        print(num, "appears", count_dict[num], "times")