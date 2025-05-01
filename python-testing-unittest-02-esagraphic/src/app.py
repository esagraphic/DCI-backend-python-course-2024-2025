# src/app.py

from random import randrange

# Function that returns a random number between start and end (inclusive)
def rnd(start, end):
    return randrange(start, end + 1)

# Function that returns the greatest number in a list
def max_num_in_list(numbers):
    if not numbers:
        raise ValueError("The list is empty")
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
