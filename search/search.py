import json
import os


def get_all_artists():
    with open('C:/Users/Tal/Desktop/Course/SpotipyProj/storage/all_artists.json', encoding='utf-8', mode='r') as artists_file:
        artists = json.loads(artists_file.read())
        print(artists)
    artists_file.close()


def main():
    get_all_artists()


if __name__ == '__main__':
    main()
