"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Please enter an integer: "))  # TODO: this line
        finished = True  # TODO: this line
    except ValueError:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)
