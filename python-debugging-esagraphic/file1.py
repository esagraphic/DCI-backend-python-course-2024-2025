def get_total(lst):
    index = 0
    total = 0
    while index < len(lst):
        total += lst[index]
        index += 1

    print(total)

    return total

num_list = [10, 50, 20, 70, 30, 40]

print(get_total(num_list))