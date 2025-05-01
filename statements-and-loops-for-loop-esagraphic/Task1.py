# # Task 1 Your task is to write a Python program to create the multiplication table (from 1 to 10) of a number. Number is prompted by the user.
# Print results.
number = input('Input a number:')
print(f'Result of multiplication by {number}:')

counter = 1

for i in range (1,11):
    result = i * int(number)
    print(f'{i} X {number} = {result}')


#Task2

