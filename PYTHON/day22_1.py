total = 0
while True:
    product = input("Enter name of the product: ")
    if product == "no":
        break
    price = float(input("Enter the price of the product: "))
    total += price

    choice = input("do you wanna continue shopping? ")
    if choice == "no":
        break
print(f"the total price of the products is {total}")
