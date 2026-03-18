#write a program that creates a new list containing all elemets placedon even positions of the original list
#a=[43,23,21,44,56,75]->[43,21,56]
a=[43,23,21,44,56,75]
new_list=[]
for i in range(0,len(a),2):
    new_list.append(a[i])
print(new_list)