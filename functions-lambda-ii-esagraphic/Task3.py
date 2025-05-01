def protected(func):
    return lambda: (
        func() if input("Username: ") == "admin" and input("Password: ") == "admin"
        else print("You are not authorized")
    )

def public():
    print("Hello World!")

@protected
def private():
    print("Welcome, admin!")

# Test the functions
public()
private()
