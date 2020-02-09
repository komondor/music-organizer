from gmusicapi import Mobileclient
from tabulate import tabulate
import sys
import re

collection = Mobileclient()


def main():

    try:
        sys.argv[1]
    except:
        print("please provide an argument: login, count, find")
        sys.exit()

    if sys.argv[1] == "login":
        collection.perform_oauth()

    try:
        collection.oauth_login(collection.FROM_MAC_ADDRESS)
    except:
        print("Not loggin. Try the following command: music login")
    else:

        allplaylist = collection.get_all_user_playlist_contents()
        allplaylist.sort(key=lambda e: e['name'], reverse=False)
        allplaylist.pop(0)

        def encode_utf(text):
            return text.encode('utf-8').strip()

        if sys.argv[1] == "count":

            list = []
            for playlist in allplaylist:
                tagsText = filterTags(playlist['description'])
                list.append([playlist['name'], len(
                    playlist['tracks']), tagsText])

            print(tabulate(list, headers=[
                "Playist Name", "Number of tracks", "Tags"]))

        if sys.argv[1] == "find":

            search_query = sys.argv[2]
            allplaylist.pop(0)
            result = []

            for playlist in allplaylist:

                playlist_name = playlist['name'].encode('utf-8').strip()
                song_list = []

                for track in playlist['tracks']:
                    if 'track' in track:
                        album = encode_utf(track["track"]["album"])
                        artist = encode_utf(track["track"]["artist"])
                        title = encode_utf(track["track"]["title"])
                        verification_query = album + artist + title

                        if search_query in verification_query.decode("utf-8"):
                            song_list.append([playlist_name, title, artist])

                if len(song_list) != 0:
                    for song in song_list:
                        result.append(song)

            print(tabulate(result, headers=["playlist", "title", "artist"]))


def filterTags(rawData):
    tags = rawData.replace(" ", "")
    tags = tags.replace("\"", "")
    tags = re.search("(?<=Tags:\[)(.*?)(?=\])", tags)
    tags = re.split(",", tags.group(0))
    return tags


if __name__ == '__main__':
    main()
