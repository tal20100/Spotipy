from user_control.user import User


class PremiumUser(User):
    def __init__(self, username, password, account_type, playlists: []):
        super().__init__(username, password, account_type, playlists)
        self.username = username
        self.password = password
        self.account_type = 'premium'
        self.playlists = playlists
