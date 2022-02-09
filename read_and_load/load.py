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
# todo: config path
path = 'C:/Users/Tal/Desktop/Course/Spotipy/songs'
for filename in glob.glob(os.path.join(path, '*.json')):  # only process .JSON files in folder.
    with open(filename, encoding='utf-8', mode='r') as currentFile:
        data = currentFile.read().replace('\n', '')
        single_track = json.loads(data)['track']
        if single_track not in trackList:
            trackList.append(single_track)


def album_in_loaded(id):
    for album in loaded_albums:
        if (album.id == id):
            return album
    return -1


# all the tracks loaded as objects
track_obj_list = []
for track in trackList:
    artists = []
    for artist in track["artists"]:
        artists.append(Artist(artist["id"], artist["name"]))
        if album_in_loaded(track["album"]["id"]) != -1:
            track_obj_list.append(
                Track(track["id"], album_in_loaded(track["album"]["id"]), artists, track["popularity"]))
            album_in_loaded(track["album"]["id"]).tracks.append(track)
            album_in_loaded(track["album"]["id"]).num_of_songs = album_in_loaded(track["album"]["id"]).num_of_songs + 1
        else:  # album is unknown
            loaded_albums.append(Album(track["album"]["id"], track["album"]["name"], tracks=[], num_of_songs=1))
            album_in_loaded(track["album"]["id"]).tracks.append(track)

    # save loaded albums in file
    with open('data.json', 'w') as file:
        for album in loaded_albums:
            json.dump(json.dumps(album.__dict__), file)


def main():
    #pp = pprint.PrettyPrinter(depth=6)
    #pp.pprint(trackList[:4])
    for album in loaded_albums:
         pp = pprint.PrettyPrinter(depth=6)
         pp.pprint(album.__dict__)
        #print(album.__dict__)


if __name__ == '__main__':
    main()
