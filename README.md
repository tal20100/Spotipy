# ma08-spotipy

packages explained: 

music object - contains the object classes : track, artist, album and playlist. playlist.py contains playlist-related

read_and_load - contains load.py that reads all the tracks (json files) and saves them into different objects 

read_json - json files to user/album objects

saved_accounts - when registering, each user is saved in a file [unique_username].json

search - all the search functions

user_control - abstract class user, premium user, free user and sign_in_up.py that contains login and register

loggerss - each login and new account creation, a log is written in saved_accounts.log


load_metadata - stores

utils - random functions all the albums and all the artists from the load so it can be used later when searching



*Exeption handeling and user interface is missing
