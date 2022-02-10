from abc import ABC, abstractmethod


class User(ABC):
    @abstractmethod
    def __init__(self, username, password, account_type, playlists: []):
        pass
