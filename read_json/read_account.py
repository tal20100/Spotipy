import json


# this function gets a username and returns it as an object by reading it from its account file

def read_user(username):
    from utils.generate_path import generate_user_path
    user_file_location = generate_user_path(username)
    with open(user_file_location, encoding='utf-8') as user_file:
        user_dict = json.loads(user_file.read())
    user_file.close()
    # the read_json data is stored as string, ill use the info to create an object

    playlists = []
    for playlist in user_dict["playlists"]:
        from playlist import Playlist
        playlists.append(Playlist(playlist["name"], playlist["tracks"]))
    from user_control.user import User
    loaded_user = User(user_dict["username"], user_dict["password"], user_dict["account_type"], playlists)

    return loaded_user


def main():
    print(read_user('tal1').__dict__)


if __name__ == '__main__':
    main()
