from gmusicapi import Mobileclient
from tabulate import tabulate
import sys
import re


class _Base:
    def __init__(self, collection):
        self.collection = collection

    def getAllplaylists(self):
        allplaylist = self.collection.get_all_user_playlist_contents()
        allplaylist.sort(key=lambda e: e['name'], reverse=False)
        return allplaylist


class Utilities(_Base):
    def countTrackPerPlaylist(self):

        def filterTags(rawData):
            tags = rawData.replace(" ", "")
            tags = tags.replace("\"", "")
            tags = re.search(r"(?<=Tags:\[)(.*?)(?=\])", tags)
            tags = re.split(",", tags.group(0))
            return tags

        def renameBagsPlaylists(playlist):

            if playlist['name'].startswith("("):
                playlist_count = 1000 - len(playlist['tracks'])
                playlist_name = '{:04d}'.format(playlist_count)
                playlist_id = playlist['id']
                new_name = "("+str(playlist_name)+")"
                self.collection.edit_playlist(playlist_id, new_name)

        allplaylist = super().getAllplaylists()
        list = []
        for playlist in allplaylist:
            renameBagsPlaylists(playlist)
            tagsText = filterTags(playlist['description'])
            list.append([playlist['name'], len(
                playlist['tracks']), tagsText])

        print(tabulate(list, headers=["playlist", "count", "tags"]))

    def queryPlaylist(self, query):

        def removePlaylistWithParantheses():
            count = 0
            allplaylist = super().getAllplaylists()
            for playlist in allplaylist:
                if playlist['name'].startswith("("):
                    count = count + 1
            if count > 0:
                allplaylist.pop(count-1)

            return allplaylist

        result = []
        allplaylist = removePlaylistWithParantheses()

        for playlist in allplaylist:

            playlist_name = playlist['name'].encode('utf-8').strip()
            song_list = []

            for track in playlist['tracks']:
                if 'track' in track:
                    album = track["track"]["album"]
                    artist = track["track"]["artist"]
                    title = track["track"]["title"]
                    verification_query = album + artist + title

                    if query in verification_query:
                        song_list.append([playlist_name, title, artist])

            if len(song_list) != 0:
                for song in song_list:
                    result.append(song)

        print(tabulate(result, headers=["playlist", "title", "artist"]))
