import random

print("Welcome to the Number Guessing Game!")
print("You have 5 chances to guess a number between 1 and 100.")

# Initialize guess count and target number
guess_chance = 0
guess_no = random.randint(1, 100)

# Loop for maximum 5 attempts
while guess_chance < 5:
    try:
        num = int(input(f"Attempt {guess_chance + 1}: Enter a number (1-100): "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if num < 1 or num > 100:
        print(" Number must be between 1 and 100.")
        continue

    guess_chance += 1

    if num == guess_no:
        print(f" Good guess! You won in {guess_chance} attempts!")
        break
    elif num < guess_no:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
else:
    print(f"Out of guesses! The number was {guess_no}. Better luck next time!")
