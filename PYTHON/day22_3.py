#write a program thhat creates and prints out a list containing
# only the unique elements from an exixting list.
#[1,1,2,3,3,4,4,5,6,5,6]-> [1,2,3,4,5,6]
input_list=[1,1,2,3,3,4,4,5,6,5,6]
unique_list=[]
for element in input_list:
    if element not in unique_list:
        unique_list.append(element)
print(unique_list)