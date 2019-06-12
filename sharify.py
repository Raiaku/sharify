__author__ = 'Raiaku'

import os
from flask import Flask, render_template, url_for, flash, session, request, jsonify, redirect

from flask_oauthlib.client import OAuth, OAuthException
from flask_bootstrap import Bootstrap
from configparser import ConfigParser
import spotipy
import spotiwise 
from spotipy import oauth2
from spotipy.object_classes import SpotiwiseArtist, SpotiwiseAlbum, SpotiwiseTrack, SpotiwisePlayback, SpotiwisePlaylist, SpotiwiseItem

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


# Spotify
SPOTIFY_APP_ID = os.getenv('SPOTIPY_CLIENT_ID') or env_vars['spotipy_client_id']
SPOTIFY_APP_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET') or env_vars['spotipy_client_secret']

DEFAULT_ALBUM_ART = "http://upload.wikimedia.org/wikipedia/en/5/54/Public_image_ltd_album_cover.jpg"

app = Flask(__name__)


app.debug = True
app.secret_key = 'development'
oauth = OAuth(app)
Bootstrap(app)
# s = sched.scheduler(time.time, time.sleep)
playlist_is_initialized = False

spotify = oauth.remote_app(
    'spotify',
    consumer_key=SPOTIFY_APP_ID,
    consumer_secret=SPOTIFY_APP_SECRET,
    # Change the scope to match whatever it us you need
    # list of scopes can be found in the url below
    # https://developer.spotify.com/web-api/using-scopes/
    # request_token_params={'scope': 'playlist-modify-public user-read-playback-state'},
    request_token_params={'scope': ' '.join(SCOPES)},
    base_url='https://accounts.spotify.com',
    request_token_url=None,
    access_token_url='/api/token',
    authorize_url='https://accounts.spotify.com/authorize'
)



@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/login')
def login():
    callback = url_for(
        'spotify_authorized',
        next=request.args.get('next') or request.referrer or None,
        _external=True
    )
    return spotify.authorize(callback=callback)


@app.route('/login/authorized')
def spotify_authorized():
    global sp, spotify_username
    resp = spotify.authorized_response()
    if resp is None:
        return 'Access denied: reason={0} error={1}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )
    if isinstance(resp, OAuthException):
        return 'Access denied: {0}'.format(resp.message)

    session['oauth_token'] = (resp['access_token'], '')
    token = session['oauth_token'][0]
    # try:
    #     me = spotify.get('https://api.spotify.com/v1/me')
    # except AssertionError:
    #     breakpoint()
    # spotify_username = me.data['id']
    sp = spotipy.Spotify(auth=token)
    spotify_username = sp.me().get('id')
    print(f'token: {token}')
    with open('{}_token.dat'.format(spotify_username), 'w') as f:
        f.write(token)
    print('Token stored')
    playlists = sp.user_playlists(spotify_username)
    return display_playlists(playlists)
    # return 'Logged in as id={0} name={1} redirect={2}'.format(
    #     me.data['id'],
    #     me.data['display_name'],
    #     request.args.get('next')
    # )

def display_playlists(playlists):
    result = []
    result_link = []
    track_toals = []
    for playlist in playlists['items']:
        result.append(playlist['name'])
        # track_toals.append(playlist['tracks']['total'])
        # result_link.append(url_for('display_tracks', playlist_id=playlist['id']))

    return render_template('display_playlists.html', playlists=result)
