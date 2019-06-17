import os
from configparser import ConfigParser
import spotiwise
from spotiwise import util, oauth2
from spotiwise.object_classes import (
    SpotiwiseArtist, 
    SpotiwiseAlbum, 
    SpotiwiseTrack, 
    SpotiwisePlayback, 
    SpotiwisePlaylist, 
    SpotiwiseItem
)

config = ConfigParser()
config.read('settings.ini')
env_vars = config['Environment Vars']

# LASTFM_API_KEY = os.getenv('LASTFM_API_KEY') or env_vars['LASTFM_API_KEY']
# LASTFM_API_SECRET = os.getenv('LASTFM_API_SECRET') or env_vars['LASTFM_API_SECRET']
# lastfm_username = os.getenv('LASTFM_DEFAULT_USERNAME') or env_vars['LASTFM_DEFAULT_USERNAME']
# password_hash = os.getenv('LASTFM_DEFAULT_PWHASH') or env_vars['LASTFM_DEFAULT_PWHASH']
spotify_username = os.getenv('SPOTIFY_DEFAULT_USERNAME') or env_vars['SPOTIFY_DEFAULT_USERNAME']
SPOTIFY_APP_ID = os.getenv('SPOTIPY_CLIENT_ID') or env_vars['SPOTIPY_CLIENT_ID']
SPOTIFY_APP_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET') or env_vars['SPOTIPY_CLIENT_SECRET']

SCOPES = [
    'playlist-read-private',
    'playlist-read-collaborative',
    'playlist-modify-public',
    'playlist-modify-private',
    'streaming',
    'ugc-image-upload',
    'user-follow-modify',
    'user-follow-read',
    'user-library-read',
    'user-library-modify',
    'user-read-private',
    'user-read-birthdate',
    'user-read-email',
    'user-top-read',
    'user-read-playback-state',
    'user-modify-playback-state',
    'user-read-currently-playing',
    'user-read-recently-played'
]
username = 'Raiaku'
redirect_url = 'http://127.0.0.1:5001/login/authorized'
scopes = ' '.join(SCOPES)


oauth = util.prompt_for_user_token(
    username=username,
    scope=scopes,
    client_id=SPOTIFY_APP_ID,
    client_secret=SPOTIFY_APP_SECRET,
    redirect_uri=redirect_url,
)
sp = spotiwise.Spotify(oauth=oauth)
