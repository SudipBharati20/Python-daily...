# automatically skip any product with a negative price. add up all the valid
# positive prices to get a subtotal. calculate a 13% tax on the subtotal and include
# it in the total amount. Finally, it will ask if the user wants the products delivered . if the answer is yes , an extra
# delivery fee of 100 will be added to the total.
total = 0
while True:
    product = input("Enter name of the product: ")
    if product == "no":
        break
    price = float(input("Enter the price of the product: "))
    if price < 0:
        print("Invalid price. Skipping this product.")
        continue
    total += price

    choice = input("do you wanna continue shopping? ")
    if choice == "no":
        break