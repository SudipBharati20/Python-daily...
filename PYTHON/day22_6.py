#write a python program that:
#in the given list:
#[1,2,6,4,5,7,1,4,5]
#counts how many times each number appears
#displays only the number that are repeated  and how many times they appear.
input_list=[1,2,6,4,5,7,1,4,5]
count_dict={}
for number in input_list:
    if number in count_dict:
        count_dict[number]+=1
    else:
        count_dict[number]=1

for number, count in count_dict.items():
    if count > 1:
        print(f"{number}: {count}")
        