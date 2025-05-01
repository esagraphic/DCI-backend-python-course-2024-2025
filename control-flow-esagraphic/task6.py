number = int(input("Enter a number: "))
if number > 0 and number % 2 != 0 and number % 7 == 0:
    print(f"The number {number} is positive, odd, and divisible by 7.")
else:
    print(f"The number {number} is not positive, odd, and divisible by 7.")
