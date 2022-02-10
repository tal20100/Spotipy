import json
import os

os.chdir('../load_metadata')


# this function prints artist's albums
def read_albums(artist_id):
    with open('all_artists.json', encoding='utf-8') as artists_file:
        artists = json.loads(artists_file.read())
    artists_file.close()
    for artist in artists:
        if artist["id"] == artist_id:
            print(artist["albums"])


def main():
    read_albums("3MZsBdqDrRTJihTHQrO6Dq")


if __name__ == '__main__':
    main()
