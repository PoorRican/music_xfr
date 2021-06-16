import json
import urllib

from music import Track, Album, Artist, Playlist


class SpotifyMusic(object):
    def __init__(self, auth):
        auth = auth

    def get_tracks(self):
        return NotImplemented

    def get_albums(self):
        return NotImplemented

    def get_artists(self):
        return NotImplemented

    def get_playlists(self):
        return NotImplemented
