x = input("First number: ")
y = input("Second number: ")
z = input("Third number: ")

if x == y or y == z:
    result = 0
    print("Calculated sum is ", result)
else:
    sum = int(x) + int(y) + int(z)
    print("Calculated sum is ", sum)