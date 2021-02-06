# This should probably be changed to a __init__.py
# but easiest way for Filip to make it this work in the terminal. 
import sys
sys.path.append("..")

import Constants
import random

import NetworkHandler as nh
from OauthDev.OAuth import OAuth

'''
class PrincipalServer(nh.Server):

    def do_GET(self):
        super(PrincipalServer, self).do_GET()
        content_length = int(self.headers.get('content-length', 0)) # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself

        #POA INPUT DATA
        data = self.parse_responce(post_data)
        self.wfile.write(Principal().test_template_poa())

    def do_POST(self):
        super(PrincipalServer, self).do_POST()
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
'''

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
