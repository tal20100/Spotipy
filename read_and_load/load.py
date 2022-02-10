import json
import os
import glob
import pprint

from music_objects.album import Album
from music_objects.artist import Artist
from music_objects.track import Track

# Reading the files from the folder and loading the json object into my custom python music_objects.

trackList = []
loaded_albums = []  # list of albums
loaded_artists = []  # list of artists
# todo: path config
path = 'songs_for _load'
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


# all the tracks loaded as music_objects
track_obj_list = []
for track in trackList:
    artists = []
    album_id = track["album"]["id"]
    for artist in track["artists"]:
        current_artist = Artist(artist["id"], artist["name"], [])
        if artist_in_loaded(artist["id"]) == -1:
            loaded_artists.append(current_artist)
            artist_in_loaded(artist["id"]).albums.append(track)
        else:
            artist_in_loaded(artist["id"]).albums.append(track)
        artists.append(current_artist)
        if album_in_loaded(album_id) != -1:  # album is already loaded
            track_obj_list.append(
                Track(track["id"], album_in_loaded(album_id), artists, track["popularity"]))
            album_in_loaded(album_id).tracks.append(track)  # add track to the album
            album_in_loaded(album_id).num_of_songs = album_in_loaded(album_id).num_of_songs + 1
        else:  # album is unknown
            new_album = Album(album_id, tracks=[], num_of_songs=1)
            new_album.tracks.append(track)
            loaded_albums.append(new_album)


os.chdir('..')
os.chdir(os.getcwd() + '/load_metadata')

with open('all_artists.json', 'w') as file:
    file.write('[')
    for artist in loaded_artists:
        json.dump(artist.__dict__, file, indent=4, separators=(',', ': '))
        file.write(',')
    file.write(']')
file.close()

# save loaded albums in file
with open('all_albums.json', 'w') as file:
    file.write('[')
    for album in loaded_albums:
        json.dump(album.__dict__, file, indent=4, separators=(',', ': '))
        file.write(',')
    file.write(']')
file.close()

