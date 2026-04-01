#write a function that takes  a number N as parameter and return the sum of all the odd numbers from 1 to N
def sum_of_odd_numbers(N):
    sum = 0
    for i in range(1, N+1):
        if i % 2 != 0:
            sum += i
    return sum