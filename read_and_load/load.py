import json
import os
import glob
import pprint

from album import Album
from artist import Artist
from track import Track

# Reading the files from the folder and loading the json object into my costum python objects.

trackList = []
loaded_albums = []  # list of albums
loaded_artists = []  # list of artists
# todo: config path
path = 'C:/Users/Tal/Desktop/Course/Spotipy/songs'
for filename in glob.glob(os.path.join(path, '*.json')):  # only process .JSON files in folder.
    with open(filename, encoding='utf-8', mode='r') as currentFile:
        data = currentFile.read().replace('\n', '')
        single_track = json.loads(data)['track']
        if single_track not in trackList:
            trackList.append(single_track)
currentFile.close()


# These functions gets an id and returns the album/artist that has this id
def album_in_loaded(album_id):
    for current_album in loaded_albums:
        if current_album.id == album_id:
            return current_album
    return -1


def artist_in_loaded(artist_id):
    for current_artist in loaded_artists:
        if current_artist.id == artist_id:
            return current_artist
    return -1


# all the tracks loaded as objects
track_obj_list = []
for track in trackList:
    artists = []
    album_id = track["album"]["id"]
    for artist in track["artists"]:
        current_artist = Artist(artist["id"], artist["name"])
        artists.append(current_artist)
        loaded_artists.append(current_artist)
        if album_in_loaded(album_id) != -1:
            track_obj_list.append(
                Track(track["id"], album_in_loaded(album_id), artists, track["popularity"]))
            album_in_loaded(album_id).tracks.append(track)
            album_in_loaded(album_id).num_of_songs = album_in_loaded(album_id).num_of_songs + 1
        else:  # album is unknown
            loaded_albums.append(Album(album_id, track["album"]["name"], tracks=[], num_of_songs=1))
            album_in_loaded(album_id).tracks.append(track)

    with open('all_artists','w') as file:
        for artist in loaded_artists:
            json.dump(artist.__dict__, file, indent=4, separators=(',', ': '))
    file.close()

    # save loaded albums in file
    with open('all_albums.json', 'w') as file:
        for album in loaded_albums:
            json.dump(album.__dict__, file, indent=4, separators=(',', ': '))
    file.close()


# loaded_albums is a list of albums that each album is an object and can be transformed into dict
def main():
    pp = pprint.PrettyPrinter(depth=6)
    # pp.pprint(trackList[:4])
    for artist in loaded_artists:
        pp.pprint(artist.__dict__)
    # for album in loaded_albums:
    # pp = pprint.PrettyPrinter(depth=6)
    # pp.pprint(loaded_albums[6].__dict__)


# print(trackList)


if __name__ == '__main__':
    main()
