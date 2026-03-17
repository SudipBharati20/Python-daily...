# Simple & Clean List-Based Database

database = []

def show_menu():
    print("\n" + "="*30)
    print("      MINI DATABASE SYSTEM")
    print("="*30)
    print("1. Add Data")
    print("2. Remove Data")
    print("3. View Data")
    print("4. Exit")
    print("="*30)

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        data = input("Enter data to add: ")
        database.append(data)
        print(f"'{data}' added successfully!")

    elif choice == "2":
        data = input("Enter data to remove: ")
        if data in database:
            database.remove(data)
            print(f"'{data}' removed successfully!")
        else:
            print("Data not found!")

    elif choice == "3":
        print("\nCurrent Database:")
        if not database:
            print("No data available.")
        else:
            for i, item in enumerate(database, start=1):
                print(f"{i}. {item}")

    elif choice == "4":
        print("Exiting... Goodbye!")
        break

    else:
        print("Invalid choice! Try again.")