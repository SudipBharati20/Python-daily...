import random
import time

def slow_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def intro():
    slow_print("Welcome to Treasure Hunt Adventure!")
    slow_print("You are stranded on a mysterious island...")
    slow_print("Find the hidden treasure before your energy runs out!\n")

def choose_path():
    slow_print("You see two paths ahead:")
    slow_print("1. Dark Forest")
    slow_print("2. Rocky Cave")
    choice = input("Choose your path (1 or 2): ")
    return choice

def forest_path():
    slow_print("\nYou enter the dark forest...")
    event = random.choice(["treasure", "trap", "nothing"])
    
    if event == "treasure":
        slow_print("You found a hidden treasure chest! You win!")
    elif event == "trap":
        slow_print("A trap was hidden under leaves! You lose!")
    else:
        slow_print("Nothing here... just creepy sounds.")
        return False
    return True

def cave_path():
    slow_print("\nYou step into the rocky cave...")
    event = random.choice(["treasure", "monster", "nothing"])
    
    if event == "treasure":
        slow_print("You discovered sparkling treasure! You win!")
    elif event == "monster":
        slow_print("A monster appears and attacks! You lose!")
    else:
        slow_print("Empty cave... but echoes are scary.")
        return False
    return True

def play_game():
    intro()
    energy = 3
    
    while energy > 0:
        choice = choose_path()
        
        if choice == "1":
            result = forest_path()
        elif choice == "2":
            result = cave_path()
        else:
            slow_print("Invalid choice!")
            continue
        
        if result:
            break
        
        energy -= 1
        slow_print(f"Energy left: {energy}\n")
    
    if energy == 0:
        slow_print("You ran out of energy. Game Over!")

# Start the game
play_game()