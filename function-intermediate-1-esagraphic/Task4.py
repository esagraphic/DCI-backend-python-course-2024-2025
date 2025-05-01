def combine(*args, **kwargs):
    print(f'Positional arguments (args):{args}')
    print(f'keyword arguments (kwargs):{kwargs}')

combine(1, 2, 3, a=10, b=20, c=30)
