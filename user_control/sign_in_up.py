import json
import os

from users.read_account import read_user
from utils import generate_path
from user_control.user import User


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    complete_path = generate_path.generate_user_path(username)
    if not os.path.exists(complete_path):
        print("There is no such username! Try again")
    user = read_user(username)
    if user.password != password:
        print(f"""Wrong password for username {username}""")
    print("Logged in successfully")


# create an account (user instance) and write it in the accounts file
def register():
    username = input("Enter username: ")
    complete_path = generate_path.generate_user_path(username)
    if os.path.exists(complete_path):
        print("user already exists")
        register()

    password = input("Enter password: ")
    password_rep = input("repeat password ")
    if password != password_rep:
        print("passwords are not the same, try again")
        register()
    print("Enter: "
          "1 - for free account"
          "2 - for premium account")
    account_type = input()
    if account_type != '1' and account_type != '2':
        print("Invalid account type, try again")
        register()
    if account_type == '1':
        account_type = "free"
    else:
        account_type = "premium"
    new_user = User(username, password, account_type, playlists=[])

    # create file
    with open(complete_path, 'w') as json_file:
        json.dump(new_user.__dict__, json_file, indent=4, separators=(',', ': '))


def main():
    register()
    #login()


if __name__ == '__main__':
    main()
