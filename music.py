#!/usr/bin/env python

from gmusicapi import Mobileclient
import sys

collection = Mobileclient()

# collection.perform_oauth()
collection.oauth_login(collection.FROM_MAC_ADDRESS)

allplaylist = collection.get_all_user_playlist_contents()
allplaylist.sort(key=lambda e: e['name'], reverse=True)

for playlist in allplaylist:
    i = 0
    name = playlist['name'].encode('utf-8').strip()
    for track in playlist['tracks']:
        i = i + 1
    print("Playlist name: {} Count: {}".format(name, i))
