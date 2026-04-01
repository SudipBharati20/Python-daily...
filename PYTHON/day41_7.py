#write a program that takes input from the user a string of numbers (eg-""24453") then all the numbers from the sri g must be put
#in a list and theiri sum should be orinter out.
def sum_of_numbers_in_string(s):
    numbers = []
    total_sum = 0
    
    for char in s:
        if char.isdigit():
            num = int(char)
            numbers.append(num)
            total_sum += num
            
    return numbers, total_sum