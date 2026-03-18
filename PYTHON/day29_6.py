##write a program that containing two list two lists by alternating elements.
#['A','B','C'],[1,2,3]->['A',1,'B',2,'C',3]
list1 = ['A', 'B', 'C']
list2 = [1, 2, 3]
result = []
for i in range(len(list1)):
    result.append(list1[i])
    result.append(list2[i])
print(result)