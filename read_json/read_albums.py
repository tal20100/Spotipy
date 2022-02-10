import json
import os

os.chdir('..')
os.chdir(os.getcwd() + '/storage')


# this function returns list of albums from all_artists
def read_albums(artist_id):
    with open('all_artists.json', encoding='utf-8') as artists_file:
        artists = json.loads(artists_file.read())
    artists_file.close()
    for artist in artists:
        if artist["id"] == artist_id:
            print(artist["albums"])
    # the read_json data is stored as string, ill use the info to create an object
    #print(artists)


def main():
    read_albums("3MZsBdqDrRTJihTHQrO6Dq")


if __name__ == '__main__':
    main()
