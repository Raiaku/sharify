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


def get_playlist_uri(playlist_name):
    playlists = sp.current_user_playlists()
    playlist_name_uri_map = {playlist.name: playlist.uri for playlist in playlists}
    return playlist_name_uri_map.get(playlist_name)
    
def get_playlist(playlist_name):
    """Get instantiated playlist object using provided playlist name
    
    :param playlist_name: Name of playlist to locate
    :type playlist_name: str
    :returns: Playlist object with items
    :rtype: SpotiwisePlaylist
    """
    playlist_uri = get_playlist_uri(playlist_name).split(':')
    return sp.user_playlist(playlist_uri[2], playlist_uri[-1], precache=True)


def create_contributer_dict(playlist_name):
    """Generates dictionary with contributers as keys for all items in playlist
    
    :param playlist_name: Name of Playlist object to generate dict from
    :type playlist_name: string
    :returns: Dictionary of items partitioned by user that added them
    :rtype: Dict[SpotiwiseUser, List[SpotiwiseItem]]
    """
    contributers_dict = {}
    playlist = get_playlist(playlist_name)
	for item in playlist.items:
		try:
			contributers_dict[item.added_by].append(item)
		except KeyError:
			contributers_dict[item.added_by] = [item]
    return contributers_dict

def get_highest_contributer(contributer_dict):
    """Gets highest contributer from grouped dictionary and number of items they contributed
    
    :param contributer_dict: Dictionary of items grouped by user that added them
    :type playlist: Dictionary
    :returns: SpotiwiseUser object for highest contributer and number of items they contributed as a tuple
    :rtype: Tuple[SpotiwiseUser, int]
    """
    