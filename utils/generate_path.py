import os


def generate_user_path(username):
    # add to account file
    file_name = username + '.json'
    # todo: add configuration for the accounts folder
    path = 'C:/Users/Tal/Desktop/Course/SpotipyProj/accounts'
    #complete_path = path+"/"+file_name
    complete_path = os.path.join(path, file_name)
    return complete_path
