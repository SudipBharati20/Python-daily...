#write a program that prints all the elements of a list that are divisible by both 4 and 5. use the following list;
#a=[10,20,25,30,40,45,50,60,70,80,90,100]
a=[10,20,25,30,40,45,50,60,70,80,90,100]
for i in a:
    if i % 4 == 0 and i % 5 == 0:
        print(i)