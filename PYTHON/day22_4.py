#WAP that creates and prints a new list with the lemets of an existing list in reverse order
# [1,2,3,4,5]-> [5,4,3,2,1]
input_list=[1,2,3,4,5]
reversed_list=[]
for i in range(len(input_list)-1,-1,-1):
    reversed_list.append(input_list[i])
print(reversed_list)