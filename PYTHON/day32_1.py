import random

print("Welcome to Number Guessing Game!")

# Difficulty selection
print("\nSelect Difficulty:")
print("1. Easy (1–50, 10 attempts)")
print("2. Medium (1–100, 7 attempts)")
print("3. Hard (1–200, 5 attempts)")

choice = int(input("Enter choice (1/2/3): "))

# Setting based on difficulty
if choice == 1:
    number = random.randint(1, 50)
    attempts = 10
elif choice == 2:
    number = random.randint(1, 100)
    attempts = 7
elif choice == 3:
    number = random.randint(1, 200)
    attempts = 5
else:
    print("Invalid choice")
    exit()

print("\nGame Started! Guess the number.")

# Game loop
for i in range(attempts):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Correct! You win!")
        break
    elif guess > number:
        print("Too high!")
    else:
        print("Too low!")

    print("Attempts left:", attempts - i - 1)

else:
    print("\nGame Over! The number was:", number)