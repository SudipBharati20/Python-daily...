#the file "lab8.txt" contains 16 numbers seperated by commas and divided into  4 lines. write a program that reads the numbers from the 
#file and finds out the sum of all the numbers, and the max and min number.

#open the file in read mode
file = open("lab8.txt", "r")
#read the content of the file and split it into a list of numbers
numbers = file.read().split(",")
#convert the list of strings to a list of integers
numbers = [int(num) for num in numbers]
#find the sum of all the numbers
total_sum = sum(numbers)
#find the max and min number
max_num = max(numbers)
min_num = min(numbers)
#print the results
print("The sum of all the numbers is:", total_sum)
print("The maximum number is:", max_num)
print("The minimum number is:", min_num)
#close the filefile.close()