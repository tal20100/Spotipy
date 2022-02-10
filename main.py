import json

from user_control import sign_in_up
from utils import generate_path
import utils


def main():
    logged_username = sign_in_up.login()
    username_file_path = utils.generate_path.generate_user_path(logged_username)
    with open(username_file_path, 'r') as user_file:
        user_dict = json.load(user_file)
    user_type = user_dict["account_type"]

    def sampleDecorator(func):
        def addingFunction():
            # some new statments or flow control
            print("This is the added text to the actual function.")
            # calling the function
            func()

        return addingFunction

    @sampleDecorator
    def actualFunction():
        print("This is the actual function.")


if __name__ == '__main__':
    main()
