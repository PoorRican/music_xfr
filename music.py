from typing import List


def Artist(object):
    def __init__(self, name: str):
        name = name


def Album(object):
    def __init__(self, name: str, artist: Artist):
        name = name
        artist = artist


def Track(object):
    def __init__(self, name: str, album: Album):
        name = name
        album = album


def Playlist(object):
    def __init__(self, name, tracks: List[Track]):
        name = name
        tracks = tracks
