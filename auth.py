import os
import sys

list_users = [
    {
        "Username": "Fatih",
        "Password": "123"
    },
    {
        "Username": "Fatih1",
        "Password": "1234"
    },
    {
        "Username": "Fatih2",
        "Password": "12345"
    },
    {
        "Username": "Fatih3",
        "Password": "123456"
    }
]

def show_ui():
    print("================================================")
    print("Wellcome to Auth System! :)")
    print("Enter the number on choice below to start. ->")
    print("Example: 1")
    print("+--------------------+")
    print("|    1. Register     |")
    print("|    2. Login        |")
    print("|    3. List User    |")
    print("|    4. Exit         |")
    print("+--------------------+")
    print("================================================")

def register():
    user_name = input("Input your name: ")
    user_password = input("Input your password: ")
    list_users.append({
        "Username": user_name,
        "Password": user_password
    })

    print("Register succedd! You can login using this user.")

# output: 
# Input your name: Fatih67
# Input your password: 676767
# Register succedd! You can login using this user.

def login():
    user_name = input("Enter your name: ")
    user_password = input("Enter your password: ")

    login_succes = False

    for user in list_users:
        if user["Username"] == user_name and user["Password"] == user_password:
            login_succes = True
            break

    if login_succes:
        print(f"Login succeed. Hello, {user_name}!")
        
    else:
        print("Username or Password incorrect!")

# output true:
# Enter your name: Fatih
# Enter your password: 123
# Login succeed. Hello, Fatih!

# output false:
# Enter your name: Fatih
# Enter your password: 1
# Username or Password incorrect!

def list():
    print("This is a list of users: ")
    for user in list_users:
        print(user)

# ouput: 
# This is a list of users: 
# {'Username': 'Fatih', 'Password': '123'}
# {'Username': 'Fatih1', 'Password': '1234'}
# {'Username': 'Fatih2', 'Password': '12345'}
# {'Username': 'Fatih3', 'Password': '123456'}

def exit():
    print("Thank you for using this system!")
    sys.exit()

# output:
# Thank you for using this system!

def main():
    while True:
        show_ui()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            list()
        elif choice == "4":
            exit()
        else:
            print("Invalid choice!")
main()

# output:
# ================================================
# Wellcome to Auth System! :)
# Enter the number on choice below to start. ->
# Example: 1
# +--------------------+
# |    1. Register     |
# |    2. Login        |
# |    3. List User    |
# |    4. Exit         |
# +--------------------+
# ================================================
# Enter your choice: 