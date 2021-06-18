import spotify.models as models
from typing import List


class Artist(object):
    def __init__(self, name: str):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    @staticmethod
    def from_spotify(artist: models.Artist):
        return Artist(artist.name)


class Album(object):
    def __init__(self, name: str, artist: Artist):
        self.name = name
        self.artist = artist

    def __repr__(self):
        return f"{self.name} by {self.artist}"

    def from_spotify(album: models.Album):
        name = album.name
        artist = Artist.from_spotify(album.artists[0])

        return Album(name, artist)


class Track(object):
    def __init__(self, name: str, album: Album):
        self.name = name
        self.album = album

    def __repr__(self):
        return f"'{self.name}' in {self.album} by {self.album.artist}"

    @staticmethod
    def from_spotify(track: models.Track):
        name = track.name
        album = Album.from_spotify(track.album)

        return Track(name, album)


class Playlist(object):
    def __init__(self, name, tracks: List[Track]):
        self.name = name
        self.tracks = tracks

    def __repr__(self):
        return f"Playlist: '{self.name}' with {len(self.tracks)} tracks"

    @staticmethod
    def from_spotify(playlist: models.Playlist):
        name = playlist.name
        tracks = [Track.from_spotify(i) for i in playlist.get_all_tracks()]

        return Playlist(name, tracks)
