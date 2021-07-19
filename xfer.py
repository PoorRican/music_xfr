from SpotifyClient import SpotifyClient, init_spotify_client
from AppleClient import AppleClient, init_apple_client


if __name__ == "__main__":
    # Init clients
    apple = init_apple_client()
    spotify = init_spotify_client()

    # Liked Songs
    apple.like_songs(spotify.get_songs())

    # Playlists
    apple.create_playlist(spotify.get_playlists())

    # Artists
    apple.like_artists(spotify.get_artists())

    # Albums
    apple.like_albums(spotify.get_albums())
