import json

from track import Track
from user_control.user import User
from users.read_account import read_user
from utils import generate_path


class Playlist(object):
    def __init__(self, name, tracks: []):
        self.name = name
        self.tracks = tracks


def create_playlist(username, list_of_tracks: []):
    playlist_name = input("Enter new playlist name")
    if is_playlist_exist(playlist_name, username):
        print("Playlist already exists, try again")
        create_playlist(username)
    else:
        new_playlist = Playlist(playlist_name, list_of_tracks)
        update_user_file(username, new_playlist)


def is_playlist_exist(playlist_name, username):
    user = read_user(username)
    existing_playlists = user.playlists
    for playlist in existing_playlists:
        if playlist.name == playlist_name:
            return True
    return False


def update_user_file(username, playlist):
    password = read_user(username).password
    account_type = read_user(username).account_type
    playlists = read_user(username).playlists
    playlists.append(playlist)
    # rewrite the file
    updated_user = User(username, password, account_type, playlists)
    complete_path = generate_path.generate_user_path(username)
    with open(complete_path, 'w') as file:
        json.dumps(updated_user.__dict__, indent=4, separators=(',', ': '))
    file.close()


def main():
    t = Track("id24946830", "flower boy", None, 439546)
    create_playlist('tal', [t])


if __name__ == '__main__':
    main()
