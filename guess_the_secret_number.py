"""
Author: Md Arifur Rahman
Date: 31.03.2023
"""

from random import randint

# variables
secret_number = randint(1, 100)
number_of_attempts = 0
maximum_number_of_attempts = 8
guessed_number = 0

# Asking user to enter name
name = input("Enter your name: ")
print(f"Well {name}, I've thought of a number between 1 and 100 and you have only {maximum_number_of_attempts} tries to guess it.")

while number_of_attempts < maximum_number_of_attempts:
    # Guessed number from user
    guessed_number = int(input("Enter Number: "))
    number_of_attempts += 1

    match guessed_number:
        case guessed_number if guessed_number < secret_number:
            print("Wrong answer! Secret number is greater then your number.")
        case guessed_number if guessed_number > secret_number:
            print("Wrong answer! Secret number is lower then your number.")
        case _:
            print(f"Congratulations! You guessed it right in {number_of_attempts} attempts!")
            break

    # Calculation remaining attempts
    number_of_attempts_left = maximum_number_of_attempts - number_of_attempts
    if number_of_attempts_left == 0:
        break
    print(f"You have {number_of_attempts_left} attempts left!")

# If the user can't guess right number within given number of attempts
if secret_number != guessed_number:
    print(f"Sorry! You have run out of attempts. The secret number was {secret_number}")
