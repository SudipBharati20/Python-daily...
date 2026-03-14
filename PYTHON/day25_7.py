items = []
prices = []
quantities = []

while True:
    item = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    items.append(item)
    prices.append(price)
    quantities.append(quantity)

    choice = input("Add another item? (yes/no): ")

    if choice.lower() == "no":
        break

subtotal = 0
for i in range(len(items)):
    total_cost = prices[i] * quantities[i]
    subtotal += total_cost

vat = subtotal * 0.13
final_total = subtotal + vat

print("Subtotal:", subtotal)
print("VAT (13%):", vat)
print("Final Total:", final_total)