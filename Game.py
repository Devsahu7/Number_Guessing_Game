import random

print("🎲 Welcome to Dice Guessing Game!")
print("You have only 3 attempts to guess the number (1 to 6)\n")

guess_number = random.randint(1, 6)
attempts = 3

for i in range(1,attempts+1):
    user = int(input(f"Attempt {i}: Enter your guess: "))

    if user == guess_number:
        print("🎉 Correct! You guessed the right number!")
        break
    else:
        if i < attempts:
            if user < guess_number:
                print("Too low! Try again.\n")
            else:
                print("Too high! Try again.\n")
        else:
            print(f" Game Over! The correct number was {guess_number}")
