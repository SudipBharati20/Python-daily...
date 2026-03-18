#write a program that contains two list of equal length and alternaingly taking eleements. eg
#['a','b','c'],[1,2,3]->['a',1,'b',2,'c',3]

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
result = []
for i in range(len(list1)):
    result.append(list1[i])
    result.append(list2[i])
print(result)