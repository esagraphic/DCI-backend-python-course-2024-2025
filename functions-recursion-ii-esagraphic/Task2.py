
def recursive_sum(data):
    total = 0
    for element in data:
        if isinstance(element, list):  
            total += recursive_sum(element)
        else:
            total += element  
    return total


test_data1 = [
    1,
    [1, 2],
    [1, [2, 3]],
    [1, [2, [3, 4]]],
    [1, [2, [3, [4, 5]]]],
]
test_data2 = [
    [1, [[2, 6], [3, 4]]],
    [[5, 6, [7, 8]], [2, [3, [4, 5]]]],
    [1, [2, 3]],
    [1, 2],
    1,
]
print(recursive_sum(test_data1))
print(recursive_sum(test_data2))