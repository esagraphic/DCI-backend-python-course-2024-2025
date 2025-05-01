def recursive_countdown(n):
    if n == 0:
        return 
    else:
        print( n)
        recursive_countdown(n-1)
    

recursive_countdown(5)