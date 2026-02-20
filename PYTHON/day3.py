#SWAR CONCERT DAY
import random

secret_number = random.randint(1, 10)
guess = 0
attempts = 0

print("Guess the number between 1 and 10")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low")
    elif guess > secret_number:
        print("Too high")

print("Correct")
print("You guessed it in", attempts, "attempts")