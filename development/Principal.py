# This should probably be changed to a __init__.py
# but easiest way for Filip to make it this work in the terminal. 
import sys
sys.path.append("..")

import Constants
import random

import NetworkHandler as nh
from OauthDev.OAuth import OAuth

class Principal:
    poa_store = []
    principal_id = None

    # Sets up an oauth server.
    def setup_server(self):
        oauth_server = nh.NetworkHandler()
        oauth_server.setup_server(81, OAuth.OAuthServer)


# This should probably be moved to a test file.
p = Principal()
p.setup_server()
