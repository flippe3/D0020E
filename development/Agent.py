# This should probably be changed to a __init__.py
# but easiest way for Filip to make it this work in the terminal. 
import sys
sys.path.append("..")

import NetworkHandler as nh
from OauthDev.OAuth import OAuth
from OauthDev.Util import input_form
import Constants as CONSTS
import random
import requests
import json

class Agent:
    poa_store = []
    ids = []
    auths = []

    # Retries the ID that oauth assigns to it and stores it.
    def discovery(self):
        msg = requests.get("http://localhost:81/discovery").content.decode("utf-8")
        print("cid: ", msg)
        self.ids.append(msg)

    
    # For now authorize takes the latests id and tries to authorize, should be generalized in the future.
    def authorize(self):
        msg = requests.get("http://localhost:81/authorize",
                 params={'response_type': 'code', 'client_id': self.ids[-1], 'state': OAuth().generate_state()})

        self.auths.append(msg)
        print("Response: ", msg)

    # Also only uses most recent id which won't generalize.
    def retrieve_poa(self):
        # We should probably rewrite this bjson thingy to something better but this works for now.
        bjson = dict(self.auths[-1].json())
        poa = requests.post("http://localhost:81/token",
                            params={'grant_type': 'authorization_code', 'client_id': self.ids[-1], 'code': bjson.get("code"), 'metadata': input_form()}).content.decode("utf-8")
        self.poa_store.append(poa)
        print("Agent recieved POA")
        print("POA:", poa)


    def transmit_to_vendor(self):
        print("Starting transmission from Agent to Vendor")
        print(nh.NetworkHandler().requests_post(CONSTS.vendor_port, "usePoA",
                                         self.poa_store[-1]))


# This should probably be moved to a test file instead.
a = Agent()
a.discovery()
a.authorize()
a.retrieve_poa()
a.transmit_to_vendor()
