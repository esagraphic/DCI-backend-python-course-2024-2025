def recursive_factorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        return n * recursive_factorial(n -1)
    

print(recursive_factorial(0))
print(recursive_factorial(1))
print(recursive_factorial(10))