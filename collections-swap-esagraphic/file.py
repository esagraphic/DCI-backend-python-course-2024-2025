def swap(lst, index1, index2):
    if (0 <= index1 < len(lst)) and (0 <= index2 < len(lst)):
        lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst

swap_list = [23, 65, 19, 90]
result = swap(swap_list, 1, 3)
print(result)
