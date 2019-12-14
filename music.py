#! python

from gmusicapi import Mobileclient
import sys


collection = Mobileclient()

# collection.perform_oauth()
collection.oauth_login(collection.FROM_MAC_ADDRESS)

allplaylist = collection.get_all_user_playlist_contents()
allplaylist.sort(key=lambda e: e['name'], reverse=True)
allplaylist = allplaylist[:-2]


def encode_utf(text):
    return text.encode('utf-8').strip()


if sys.argv[1] == "count":
    for playlist in allplaylist:
        i = 0
        name = encode_utf(playlist['name'])
        for track in playlist['tracks']:
            i = i + 1
        print("Playlist name: {} Count: {}".format(name, i))


if sys.argv[1] == "find":

    search_query = sys.argv[2]
    result = {}

    for playlist in allplaylist:

        playlist_name = playlist['name'].encode('utf-8').strip()
        song_list = []

        for track in playlist['tracks']:
            if 'track' in track:
                album = encode_utf(track["track"]["album"])
                artist = encode_utf(track["track"]["artist"])
                title = encode_utf(track["track"]["title"])
                verification_query = album + artist + title

                if search_query in verification_query:
                    song_list.append("{} by {}".format(title, artist))

        if len(song_list) != 0:
            result[playlist_name] = song_list

    for name in result:
        print(name)
        for chanson in result[name]:
            print("\t - {}".format(chanson))
