from gmusicapi import Mobileclient
import sys

collection = Mobileclient()

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

    # if sys.argv[1] == "logout":
    #     try: 
    #         collection.deauthorize_device(collection.FROM_MAC_ADDRESS)
    #     finally:     
    #         sys.exit()

    if sys.argv[1] == "count":
        for playlist in allplaylist:
            # name = encode_utf(playlist['name'])
            print("Playlist name: {} Count: {} Description: {}".format(
                playlist['name'], len(playlist['tracks']), playlist["description"]))


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
