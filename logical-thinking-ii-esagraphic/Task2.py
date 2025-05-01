

from Task1_data import users

def show_registration(username, password, modulename):
    for details in users:
        if details.get("name") == username and details.get("password") == password:
            if details.get("type") != "Teacher":
                is_registered = False
                for module_details in details["modules"]:
                    if module_details["title"] == modulename:
                        print(f'You are registered to the module {modulename}.')
                        is_registered = True
                        break  # Stop the loop once a match is found
                if not is_registered:
                    print(f'You did not register to the module {modulename}.')
            else:
                print("You are a teacher.")
            return  # Return after processing the user
    print(f'You did not register to the module {modulename}..')


def has_completed_module(username, password, modulename):
    for details in users:
        if details.get("name") == username and details.get("password") == password:
            if details.get("type") != "Teacher":
                is_completed = False
                for module_details in details["modules"]:
                    if module_details["title"] == modulename:
                        if module_details["completed"]== True:
                         is_completed = True
                         print(f'You have completed the module {modulename}')
                        break  # Stop the loop once a match is found
                if not is_completed:
                    print(f'You did not completed to the module {modulename}.')
            else:
                print("You are a teacher.")
            return  # Return after processing the user
    print(f'You did not register to the module {modulename}..')     



username = input("What is your username? ")
password = input(f"Type the password for username {username}: ")
modulename = input("What module do you want to check? ")
show_registration(username, password, modulename)
has_completed_module(username, password, modulename)
