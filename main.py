from utils.spotify_auth import authenticate
from utils.playlist_manager import create_or_update_playlist

def main():
    # Authenticate with Spotify API
    sp = authenticate()
    
    # Generate or update playlists
    create_or_update_playlist(sp)

if __name__ == "__main__":
    main()
