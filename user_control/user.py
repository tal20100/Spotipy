class User(object):
    def __init__(self, username, password, account_type, playlists: []):
        self.username = username
        self.password = password
        self.account_type = account_type
        self.playlists = playlists