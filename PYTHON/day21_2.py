number1=int(input("Enter the first number"))
number2=int(input("Enter the second number"))
number3=int(input("Enter the third number"))
if number1>number2>number3:
    print(f"{number1} is greater number")
elif number2>number1>number3:
    print(f"{number2} is a greater number")
else:
    print(f"{number3} is a greater number")