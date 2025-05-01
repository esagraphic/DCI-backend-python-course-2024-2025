numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

check_even = lambda x : x % 2 == 0

even_number = filter(check_even,numbers)

print(list(even_number))
