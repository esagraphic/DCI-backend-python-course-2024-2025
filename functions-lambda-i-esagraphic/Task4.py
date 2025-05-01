numbers = [2, 4, 5, 7, 9, 14]
factor = 2

num = lambda a, b: a * b
result = [num(factor, n) for n in numbers]
print(result)  # Output: [4, 8, 10, 14, 18, 28]
