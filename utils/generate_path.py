import os


# this function generated a path with a given username
def generate_user_path(username):
    file_name = username + '.json'
    path = '../saved_accounts'
    complete_path = path+"/"+file_name
    return complete_path
