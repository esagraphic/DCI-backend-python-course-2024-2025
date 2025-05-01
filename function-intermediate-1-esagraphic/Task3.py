def person_details(name, **kwargs):
    
    print(f'Name:{name}')
    for key , value in kwargs.items():
        print(f'{key}: {value}')

person_details("Martin", age=30, job="Engineer")
