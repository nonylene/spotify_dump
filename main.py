import argparse
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# https://developer.spotify.com/documentation/web-api/reference/#endpoint-save-albums-user
MAX_IDS_LENGTH = 50
REDIRECT_URI = "http://127.0.0.1:9090"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=["user-library-read"], redirect_uri=REDIRECT_URI))


def main():
    offset = 0
    items = []
    while True:
        response = sp.current_user_saved_tracks(limit=MAX_IDS_LENGTH, offset=offset)
        items += response['items']
        if response.get('next') is None:
            break
        offset += MAX_IDS_LENGTH

    print(json.dumps(items))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Dump spotify playlist')
    args = parser.parse_args()
    main()

