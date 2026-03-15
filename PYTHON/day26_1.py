cart = []

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    
    item = {"name": name, "price": price}
    cart.append(item)
    
    print("Product added successfully!\n")

def view_cart():
    if len(cart) == 0:
        print("Cart is empty\n")
    else:
        print("\nYour Cart:")
        for item in cart:
            print(item["name"], "-", item["price"])
        print()

def total_price():
    total = 0
    for item in cart:
        total += item["price"]
    print("Total Price =", total, "\n")


while True:
    print("------ Shopping Cart ------")
    print("1. Add Product")
    print("2. View Cart")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_product()

    elif choice == "2":
        view_cart()

    elif choice == "3":
        total_price()

    elif choice == "4":
        print("Thank you for shopping!")
        break

    else:
        print("Invalid choice\n")