

#write a program on cow stable management system. the program should have the following features:
#1. add a cow to the stable
#2. remove a cow from the stable
#3. display the cows in the stable
#4. exit the program
cows = []
def add_cow(name):
    cows.append(name)
    print(f"{name} has been added to the stable.")
def remove_cow(name):
    if name in cows:
        cows.remove(name)
        print(f"{name} has been removed from the stable.")
    else:
        print(f"{name} is not in the stable.")
def display_cows():
    if cows:
        print("Cows in the stable:")
        for cow in cows:
            print(cow)
    else:
        print("The stable is empty.")
while True:
    print("1. Add a cow")
    print("2. Remove a cow")
    print("3. Display cows")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        name = input("Enter the name of the cow: ")
        add_cow(name)
    elif choice == '2':
        name = input("Enter the name of the cow: ")
        remove_cow(name)
    elif choice == '3':
        display_cows()
    elif choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")

