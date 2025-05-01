users = [
    {
        "name": "Holly",
        "type": "Student",
        "password": "hunter"
    },
    {
        "name": "Peter",
        "type": "Student",
        "password": "pan"
    },
    {
        "name": "Janis",
        "type": "Teacher",
        "password": "joplin"
    }
]

username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")

def check_credentials(username, password, users):
    for user in users:
        if user['name'] == username and user['password'] == password and user['type'] == 'Teacher':
            return True  
    return False  


if check_credentials(username, password, users):
    pass
 
else:
    print("We have great courses to offer you!")