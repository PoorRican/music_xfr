apple_auth = ""
spotify_auth = ""

apple = AppleMusic(apple_auth)
spotify = SpotifyMusic(spotify_auth)

if __name__ == "__main__":
    # Liked Songs
    apple.like_songs(spotify.get_songs())

    # Playlists
    apple.create_playlist(spotify.get_playlists())

    # Artists
    apple.like_artists(spotify.get_artists())

    # Albums
    apple.like_albums(spotify.get_albums())
