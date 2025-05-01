users = [
    {
        "name": "Holly",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "password": "pan"
    },
    {
        "name": "Janis",
        "password": "joplin"
    }
]

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")

def check_credentials(username, password, users):
    for user in users:
        if user['name'] == username and user['password'] == password:
            return True  
    return False  


if check_credentials(username, password, users):
    pass
 
else:
    print("An error occurred. You are not authorized.")