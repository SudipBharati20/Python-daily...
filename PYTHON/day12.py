# FIFA PLAYER RATING GUESSER
print("Welcome to FIFA Rating Guesser")

print("\nChoose a player:")
print("1. Lionel Messi")
print("2. Cristiano Ronaldo")
print("3. Kylian Mbappe")
print("4. Kevin De Bruyne")
print("5. Erling Haaland")
print("6. Neymar Jr")
print("7. Mohamed Salah")
print("8. Virgil van Dijk")
print("9. Luka Modric")
print("10. Harry Kane")

choice = int(input("\nEnter player number: "))
guess = int(input("Enter your rating guess: "))

# Ratings
if choice == 1:
    rating = 90
    name = "Lionel Messi"
elif choice == 2:
    rating = 88
    name = "Cristiano Ronaldo"
elif choice == 3:
    rating = 91
    name = "Kylian Mbappe"
elif choice == 4:
    rating = 91
    name = "Kevin De Bruyne"
elif choice == 5:
    rating = 91
    name = "Erling Haaland"
elif choice == 6:
    rating = 89
    name = "Neymar Jr"
elif choice == 7:
    rating = 89
    name = "Mohamed Salah"
elif choice == 8:
    rating = 89
    name = "Virgil van Dijk"
elif choice == 9:
    rating = 87
    name = "Luka Modric"
elif choice == 10:
    rating = 90
    name = "Harry Kane"
else:
    print("Invalid choice")
    exit()

# Result
if guess == rating:
    print(" Correct! You are a FIFA expert.")
elif guess < rating:
    print("⬇Too low!")
else:
    print("Too high!")

print("The actual rating of", name, "is", rating)
print("Thanks for playing!")