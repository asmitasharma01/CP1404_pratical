"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""
from unittest import result

is_finished = False
while not is_finished:
    try:
        user_input = input("Enter a valid integer: ")
        is_finished = True
        print("Success")
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)
