__author__ = 'Raiaku'

from spotiwise.object_classes import (
    SpotiwiseArtist, 
    SpotiwiseAlbum, 
    SpotiwiseTrack, 
    SpotiwisePlayback, 
    SpotiwisePlaylist, 
    SpotiwiseItem, 
    SpotiwiseUser
)

contributers = {spotify_username:[tracks]}
# contributers = {SpotiwiseUser:[SpotiwiseTrack]}
# contributers = {SpotiwiseUser:[SpotiwiseItem]}
# contributers = {spotify_username:[SpotiwiseItem]}

def fairify_duplication(playlist, method = None):
    for tracks in playlist:
        return contributers 

# alternatly(better option)
def fairify_duplication(playlist_name, method=None):
    contributers_dict = {}
    playlist = get_playlist(playlist_name)
	for item in playlist:
		try:
			contributers_dict[item.contributer].append(item)
		except KeyError:
			contributers_dict[item.contributer] = [item]