

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
valid = {"username": "admin", "password": "admin"}
# Your code here

if username == valid.get('username') and password == valid.get('username'):
    print(f'Welcome ,{username}')
else:
    print('Credentials are invalid')


# note we can also use valid['username] to get the value of user name instead of valid.get('username')
# Summary
# valid['username']: Raises an error if the key does not exist, which can be useful for catching issues but requires handling of potential KeyError exceptions.
# valid_credentials.get('username'): Returns None if the key does not exist, which can be safer and cleaner, especially if you want to avoid handling exceptions for missing keys.
# In this case, using .get() is generally a good practice because it avoids potential runtime errors and allows for specifying a default value if needed.