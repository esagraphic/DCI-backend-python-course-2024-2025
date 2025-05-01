number = int(input("Enter a number: "))

divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print(f"The divisors of {number} are: {divisors}")
