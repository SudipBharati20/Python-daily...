#write a program that creates a new list containing all elements placed on odd positions of the original list
#a=[12,22,32,42,52,62]->[22,42,62]
a=[12,22,32,42,52,62]
new_list=[]
for i in range(1,len(a),2):
    new_list.append(a[i])
print(new_list)