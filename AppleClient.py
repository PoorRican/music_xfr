import json
import urllib
from typing import List

from music import Track, Album, Artist, Playlist


class AppleMusic(object):
    def AppleMusic(self, auth: str):
        auth = auth

    def add_to_playlist(self, playlist: Playlist, songs: List[Track]):
        return NotImplemented

    def create_playlists(self, playlists: List[Playlist]):
        return NotImplemented

    def add_artists(self, artists: List[Playlist]):
        return NotImplemented

    def add_albums(self, albums: List[Album]):
        return NotImplemented

    def add_tracks(self, tracks: List[Track]):
        return NotImplemented


def init_apple_client():
    return NotImplemented
