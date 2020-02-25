from gmusicapi import Mobileclient
from tabulate import tabulate
import sys
import re
from lib import Oath_Client
from lib import Utilities


def main():

    client = Oath_Client()

    try:
        sys.argv[1]
    except:
        print("please provide an argument: login, count, find")
        sys.exit()

    if sys.argv[1] == "register":
        client.register()
        sys.exit()
    if sys.argv[1] == "logout":
        client.logout()
        sys.exit()

    if client.login():
        collection = client.collection
    else:
        print("Not loggin. Try the following command: music login")
        sys.exit()

    api = Utilities(collection)

    if sys.argv[1] == "count":
        api.countTrackPerPlaylist()

    if sys.argv[1] == "find":
        api.queryPlaylist(sys.argv[2])


if __name__ == '__main__':
    main()
