
import random

number = random.randint(1, 100)
attempts = 0

print("===== NUMBER GUESSING GAME =====")
print("I have selected a number between 1 and 100.")
print("Try to guess the number!")

while True:
    try:
        guess = int(input("\nEnter your guess: "))
        attempts += 1

        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print(f"\nCongratulations! You guessed the number!")
            print(f"The number was {number}.")
            print(f"Total attempts: {attempts}")
            break

    except ValueError:
        print("Invalid input! Please enter a whole number.")
