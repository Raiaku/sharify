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


def get_playlist_uri(playlist_name, sp):
    playlists = sp.current_user_playlists()
    playlist_name_uri_map = {playlist.name: playlist.uri for playlist in playlists}
    return playlist_name_uri_map.get(playlist_name)
    

def get_playlist(playlist_name, sp):
    """Get instantiated playlist object using provided playlist name
    
    :param playlist_name: Name of playlist to locate
    :type playlist_name: str
    :returns: Playlist object with items
    :rtype: SpotiwisePlaylist
    """
    playlist_uri = get_playlist_uri(playlist_name, sp).split(':')
    return sp.user_playlist(playlist_uri[2], playlist_uri[-1], precache=True)


def create_contributor_dict(playlist_name, sp):
    """Generates dictionary with contributers as keys for all items in playlist
    
    :param playlist_name: Name of Playlist object to generate dict from
    :type playlist_name: string
    :returns: Dictionary of items partitioned by user that added them
    :rtype: Dict[SpotiwiseUser, List[SpotiwiseItem]]
    """
    contributors_dict = {}
    playlist = get_playlist(playlist_name, sp)
    for item in playlist.items:
        try:
             contributors_dict[item.added_by].append(item)
        except KeyError:
            contributors_dict[item.added_by] = [item]
    return contributors_dict


def get_highest_contributor(contributor_dict):
    """Gets highest contributor from grouped dictionary and number of items they contributed
    
    :param contributor_dict: Dictionary of items grouped by user that added them
    :type playlist: Dictionary
    :returns: SpotiwiseUser object for highest contributor and number of items they contributed as a tuple
    :rtype: Tuple[SpotiwiseUser, int]
    """
    highest_contributor = None
    most_songs_added = 0

    for contributor, playlist_items in contributor_dict.items():
        if len(playlist_items) > most_songs_added:
            highest_contributor = contributor
            most_songs_added = len(playlist_items)
    return highest_contributor, most_songs_added


def fairify_duplication(contributors_dict):
    """duplicate tracks so that each contributor has the same amount of items
    
    :param contributors_dict: dictionary of playlist items separated by contributors
    :type contributors_dict: dict
    :returns: a dictionary of tracks equally provided from each contributor 
    :rtype: dict
    """
    
    for contributor, playlist_items in contributor_dict.items():


def fairify_round_robin(contributors_dict):
    """round robin sort track items using one track form each contributor, this will be
    repeated until all track items have been added to the list
    
    :param contributors_dict: dictionary of tracks equally provided from each contributor
    :type contributors_dict: dict
    :returns: list of songs fairly shuffled by contributors
    :rtype: list
    """


def fairify_create_playlist(name, track_list):
    """create a playlist using a list of tracks
    
    :param name: name of playlist to create
    :type name: string
    :param track_list: tracks to be added playlist
    :type track_list: list
    :returns: named playlist with tracks added 
    :rtype: SpotiwisePlaylist
    """
