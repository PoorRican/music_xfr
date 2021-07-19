import yaml
import spotify.sync as spotify

from music import Track, Album, Artist, Playlist


class SpotifyClient(object):
    def __init__(self, user: spotify.User, client: spotify.Client):
        self.user = user
        self.client = client

    def get_tracks(self):
        # `http.saved_tracks
        return NotImplemented

    def get_albums(self):
        # `http.saved_albums`
        return NotImplemented

    def get_artists(self):
        # `http.followed_artists`
        return NotImplemented

    def get_playlists(self):
        playlists = self.user.get_all_playlists()
        return [Playlist.from_spotify(i) for i in playlists]


def init_spotify_client():
    with open('scrt.yml', 'r') as f:
        scrt = yaml.load(f)['spotify']

    client = spotify.Client(scrt['client_id'], scrt['client_secret'])

    user = client.get_user('mzo.sway')

    return SpotifyClient(user, client)
