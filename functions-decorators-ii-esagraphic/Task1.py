from functools import wraps

def validate_numeric(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                return "The input arguments must be numeric"
        
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                return "The input arguments must be numeric"
        
        return func(*args, **kwargs)
    
    return wrapper

@validate_numeric
def sum(a, b):
    """Return the sum of two numbers."""
    return a + b

print(sum(1, 2))        
print(sum(1, "2"))      
print(sum(a=1, b="a"))  
print(sum(a=1, b=3.4))  
