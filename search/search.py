import json
import os
import pprint


pp = pprint.PrettyPrinter(depth=6)


def get_all_artists():
    with open('../load_metadata/all_artists.json', encoding='utf-8', mode='r') as artists_file:
        artists_list = json.loads(artists_file.read())
        for artist in artists_list:
            print(artist["name"])
    artists_file.close()


def get_albums_by_artist(artist_id):
    with open('../load_metadata/all_artists.json', encoding='utf-8', mode='r') as artists_file:
        artists_list = json.loads(artists_file.read())
        for artist in artists_list:
            if artist_id == artist["id"]:
                print(artist["albums"])
    artists_file.close()


# todo
def get_most_popular(artist_id):
    # open artist file, save all albums id's in a list and then open all_albums and search for albums with id that is on
    # the list, store them in all_artist_songs list, sort it and print top 10
    artist_albums = []
    with open('../load_metadata/all_artists.json', encoding='utf-8', mode='r') as artists_file:
        artists_list = json.loads(artists_file.read())
        for artist in artists_list:
            if artist_id == artist["id"]:
                for album in artist["albums"]:
                    artist_albums.append(album)
        pp.pprint(artist_albums)

    artists_file.close()


def get_tracks_from_album(album_id):
    with open('../load_metadata/all_albums.json', encoding='utf-8', mode='r') as albums_file:
        albums_list = json.loads(albums_file.read())
        for album in albums_list:
            if album["id"] == album_id:
                print(f"""Tracks in album {album["id"]} :""")
                tracks = album["tracks"]
                for track in tracks:
                    pp.pprint(track["name"])
    albums_file.close()


def main():
    print(" ------- all artists ------- ")
    get_all_artists()
    print(" ------- albums by artist ------- ")
    get_albums_by_artist('0zFvzQ4P6i9vu7Q2Kmmi3m')
    print(" ------- most popular ------- ")
    get_most_popular('3MZsBdqDrRTJihTHQrO6Dq')
    print(" ------- tracks from album ------- ")
    get_tracks_from_album('34GQP3dILpyCN018y2k61L')


if __name__ == '__main__':
    main()
