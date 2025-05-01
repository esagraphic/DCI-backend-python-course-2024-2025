def get_sum(*list):
    '''Returns the maximum and minimum values from a list.'''

    toatll = 0
    for item in list:
        toatll += sum(item)
    return toatll
    

    return sum_num


test1 = [[0, 2, 4, 5]]
test2 = [
    [0, 2, 4, 5],
    [6],
    [0, 2, 4, 5, 1, 4, 3, 2]
]

result1 = get_sum(*test1)
result2 = get_sum(*test2)

print(f'Result 1 {result1}')
print(f'result 2 :{result2}')

