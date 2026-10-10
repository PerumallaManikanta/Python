# 1. Set Up the Game:
# ★ Generate a random number between 1 and 10 that the user has to guess.
# Import random and use randint function.

import random
secret_number = random.randint(1, 10)
print(secret_number)

# 2. Prompt the User:
# ★ Ask the user to guess the number.
# ★ Set a variable attempts to 3, which represents the maximum number of
# guesses allowed.

guess = int(input("guess a number between 1 and 10: "))
attempts = 3

#3. Implement the Guessing Logic:
#★ Use a while loop to allow the user to keep guessing until they get the
#correct number or run out of attempts.
#★ Provide feedback to the user for each guess:
#➢ If the guess is out of the valid range (1 to 10), inform the user.
# ➢ If the guess is greater than the secret number.
# ➢ If the guess is lower than the secret number.
# ➢ If the guess is correct, congratulate the user and end the game.



while attempts > 0:
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
    elif guess > secret_number:
        print("Your guess is too high.")
    elif guess < secret_number:
        print("Your guess is too low.")
    else:
        print("Congratulations! You've guessed the correct number!")
        break

    attempts -= 1
    if attempts > 0:
        guess = int(input(f"You have {attempts} attempts left. Guess again: "))
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

# 4. Control Statements:
#★ Use continue to skip the rest of the loop after informing the user if the
# guess is out of range.

# ★ Use break to exit the loop when the guess is correct.
# ★ Use else with the while loop to provide a message like "Better luck next
# time!" if the user runs out of attempts without guessing the correct number.


secret_number = 7
attempts = 3

while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))

    # Continue: Skip the rest of the loop if out of range
    if guess < 1 or guess > 10:
        print("Please enter a number between 1 and 10.")
        continue

    # Break: Exit the loop if the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed correctly.")
        break

    attempts -= 1
    print("Wrong guess! Attempts left:", attempts)

# Else: Runs if the loop finishes without break
else:
    print("Better luck next time!")




# For Loop:

# Multiplication Table Generator

# Problem Statement: Create a Python program that generates and prints a
# multiplication table (from 1 to 10) for a given number using a for loop and the range
# function.
# Step wise Instructions:
# 1. Prompt user for Input. Ask the user to enter a number for which they want to
# generate a multiplication table.
# 2. Generate the Multiplication Table: Use a for loop to iterate through the numbers
# 1 to 10. In each iteration, calculate the product of the user's number and the
# current number from the loop.
# 3. Display the Multiplication Table:
# Print each line of the multiplication table in the format: "number x i = result".


a=4
b=1
for i in range(1, 11):
    print(f"{a} * {i} = {a*i}")
    b=b+1


# Function:

# BMI Calculator

# Problem Statement: Create a Python program that calculates the Body Mass Index
# (BMI).
# Hint: BMI = weight (kg) / [height (m)]2
# Instructions:
# 1. Define a function calculate_bmi(weight, height) that returns the BMI.
# 2. Prompt the user for their weight (in kg) and height (in meters).
# 3. Use the function to calculate and display the BMI




def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi, 2)

# Function call
result = calculate_bmi(70, 1.74)

print(f"Your BMI is {result}")