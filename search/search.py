import json
import os

os.chdir('..')
os.chdir(os.getcwd() + '/storage')


def get_all_artists():
    with open('all_artists.json', encoding='utf-8', mode='r') as artists_file:
        artists_list = json.loads(artists_file.read())
        for artist in artists_list:
            print(artist["name"])
    artists_file.close()


def get_artist_by_id(artist_id):
    with open('all_albums.json', encoding='utf-8', mode='r') as albums_file:
        albums_list = json.loads(albums_file.read())
        for album in albums_list:
            print(album["name"])
    albums_file.close()


def main():
    get_all_artists()


if __name__ == '__main__':
    main()
