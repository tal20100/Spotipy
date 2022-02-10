import json
import os

os.chdir('..')
os.chdir(os.getcwd() + '/storage')


def get_all_artists():
    with open('all_artists.json', encoding='utf-8', mode='r') as artists_file:
        artists_list = json.loads(artists_file.read())
        for artist in artists_list:
            print(artist["name"], artist["albums"])
    artists_file.close()


def main():
    get_all_artists()


if __name__ == '__main__':
    main()
