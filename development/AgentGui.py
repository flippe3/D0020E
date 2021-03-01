# This should probably be changed to a __init__.py
# but easiest way for Filip to make it this work in the terminal.
import sys
from urllib.parse import parse_qs, urlparse

from WebbPages import WebbPageScripts

sys.path.append("..")

import NetworkHandler as nh
from OauthDev.OAuth import OAuth
from OauthDev.Util import input_form
import Constants as CONSTS
import random
import requests
import json


poa_store = []

class Connection:
    def __init__(self, ip,port):
        self.ip = ip
        self.port = port

    def setCid(self, cid):
        self.cid = cid

    def setAuth(self, auth):
        self.auth = auth


class AgentGui:


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
                           params={'response_type': 'code', 'client_id': self.ids[-1],
                                   'state': OAuth().generate_state()})

        self.auths.append(msg)
        print("Response: ", msg)

    # Also only uses most recent id which won't generalize.
    def retrieve_poa(self, data):
        # We should probably rewrite this bjson thingy to something better but this works for now.
        bjson = dict(self.auths[-1].json())
        responce = requests.post("http://localhost:81/token",
                            data={'grant_type': 'authorization_code', 'client_id': self.ids[-1],
                                    'code': bjson.get("code"), 'metadata': data})
        poa = responce.content.decode("utf-8")
        poa_store.append(poa)
        print("Agent recieved POA")
        print("POA:", poa)

    def transmit_to_vendor(self):
        print("Starting transmission from Agent to Vendor")
        print(nh.NetworkHandler().requests_post(CONSTS.vendor_port, "usePoA",
                                                poa_store[-1]))

class WebbHostServer(nh.Server):





    def do_GET(self):
        super(WebbHostServer, self).do_GET()
        s = self.path.split(".")
        if s[1] == "html":
            self.HtmlPage()

    def HtmlPage(self):
        print(self.path)
        f = open("WebbPages/" + self.path[1:], "r")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f.read().encode("utf-8"))
        if self.path == "/project.html":
            self.wfile.write(WebbPageScripts.project(poa_store).encode("utf-8"))


    def do_POST(self):
       # super(WebbHostServer, self).do_POST()
        print(self.path)

        if self.path.endswith(".html"):
            self.HtmlPage()

        elif self.path == "/CreatePoa":
            content_length = int(self.headers.get('content-length', 0))  # <--- Gets the size of data
            post_data = str(self.rfile.read(content_length))  # <--- Gets the data itself

            a = post_data.split("&")
            metadata = {"Agent Name": a[3].split("=")[1],
                        "Application Type": a[4].split("=")[1],
                        "Principal Name": a[5].split("=")[1],
                        "MAC Address": a[6].split("=")[1]
                        }
            enc = json.JSONEncoder().encode(metadata)
            #metadata.setdefault()
            agent = AgentGui()

            agent.discovery()
            agent.authorize()
            agent.retrieve_poa(enc)

       #     data = post_data.decode('utf-8')
            #print(data)
            self.send_response(307)
            self.send_header("Location","/project.html")

            #self.headers.get("Host") +
            self.end_headers()
        else:
            print("ERROR: Fel")



nh.NetworkHandler().setup_server(82, WebbHostServer)
# This should probably be moved to a test file instead.
#a = AgentGui()
#a.discovery()
#a.authorize()
#a.retrieve_poa()
#a.transmit_to_vendor()
