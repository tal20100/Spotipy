import json
import os
import logging
from read_json.read_account import read_user
from user_control.free_user import FreeUser
from user_control.premium_user import PremiumUser
from utils import generate_path

#loggers_path = config_read.config_read_path()
path = "C:/Users/Tal/Desktop/Course/SpotipyProj/loggers/saved_accounts.log"
logging.basicConfig(filename=path, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


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
    logging.info(f""":  User {username} has logged in """)


# create an account (user instance) and write it in the saved_accounts file
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
    if account_type == "free":
        new_user = FreeUser(username, password, account_type, playlists=[])
    else:  # premium
        new_user = PremiumUser(username, password, account_type, playlists=[])

    # create file
    with open(complete_path, 'w') as json_file:
        json.dump(new_user.__dict__, json_file, indent=4, separators=(',', ': '))
    print("User created successfully!")
    logging.info(f""":  New {new_user.account_type} user added |username: {username} password: {password}|""")


