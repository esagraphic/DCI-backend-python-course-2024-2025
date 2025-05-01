def sum_numbers(*args):
    total = []
    for arg in args:
        total.append(arg)
    print(sum(total))
        
    

sum_numbers(1, 2, 3)
sum_numbers(10, 20, 30, 40)
sum_numbers()

# second method 
print('second method we don’t need to use a list to accumulate the values since sum() can directly operate on the tuple of arguments that *args provides.')
def sum_numbers1(*args):
    print(sum(args))
        
    

sum_numbers1(1, 2, 3)
sum_numbers1(10, 20, 30, 40)
sum_numbers1()