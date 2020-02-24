from gmusicapi import Mobileclient
import os
from appdirs import AppDirs

my_appdirs = AppDirs('gmusicapi', 'Simon Weber')
credentials_path = os.path.join(my_appdirs.user_data_dir, 'mobileclient.cred')


class Oath_Client():

    def __init__(self):

        self.collection = Mobileclient()

    def register(self):
        return self.collection.perform_oauth()

    def login(self):
        if os.path.exists(credentials_path):
            try:
                self.collection.oauth_login(self.collection.FROM_MAC_ADDRESS)
                return True
            except Exception:
                return False
        else:
            return False

    def logout(self):
        os.remove(credentials_path)
