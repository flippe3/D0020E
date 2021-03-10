# This should probably be changed to a __init__.py
# but easiest way for Filip to make it this work in the terminal.
import sys
from urllib.parse import parse_qs, urlparse

sys.path.append("..")

from WebbPages import WebbPageScripts


import NetworkHandler as nh
from OauthDev.OAuth import OAuth
from OauthDev.Util import input_form
from datetime import datetime
import Constants as CONSTS
import random
import requests
import json

poa_store = []
agentID = 0
agentIDs = []

class Connection:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    def setCid(self, cid):
        self.cid = cid

    def setAuth(self, auth):
        self.auth = auth


class AgentGui:
    ids = []
    auths = []

    def __init__(self, agentIDt, princid):
        self.agentID = agentIDt
        self.princID = princid

    # Retries the ID that oauth assigns to it and stores it.
    def discovery(self, ip="localhost", port="81"):
        msg = requests.get("http://" + ip + ":" + port + "/discovery").content.decode("utf-8")
        print("cid: ", msg)
        self.ids.append(msg)

    # For now authorize takes the latests id and tries to authorize, should be generalized in the future.
    def authorize(self, ip="localhost", port="81"):
        msg = requests.get("http://" + ip + ":" + port + "/authorize",
                           params={'response_type': 'code', 'client_id': self.ids[-1],
                                   'state': OAuth().generate_state()})

        self.auths.append(msg)
        print("Response: ", msg)

    # Also only uses most recent id which won't generalize.
    def retrieve_poa(self, data, ip="localhost", port="81"):
        # We should probably rewrite this bjson thingy to something better but this works for now.
        bjson = dict(self.auths[-1].json())
        responce = requests.post("http://" + ip + ":" + port + "/token",
                                 data={'grant_type': 'authorization_code', 'client_id': self.ids[-1],
                                       "agentID": self.agentID,
                                       'code': bjson.get("code"), 'metadata': data})
        poa = responce.content.decode("utf-8")
        poa_store.append(poa)
        if(len(agentIDs) == 0):
            agentIDs.append(self.agentID)
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
        f = open("../WebbPages/" + self.path[1:], "r")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(f.read().encode("utf-8"))
        if self.path == "/project.html":
            self.wfile.write(WebbPageScripts.project(poa_store, agentIDs[0], -23).encode("utf-8"))

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
            print(len(a))
            if len(a) > 10:
                for items in range(9, len(a), 2):
                    metadata.setdefault(a[items].split("=")[1], a[items + 1].split("=")[1])

            payload = {#"exp": a[7].split("=")[1],
                       #"iat": a[8].split("=")[1],
                       "exp": datetime.utcnow().timestamp()+36000,
                       "iat": datetime.utcnow().timestamp()-36000,
                       "meta": metadata,
                       "agentID": a[2].split("=")[1]
                       }

            enc = json.JSONEncoder().encode(payload)
            # metadata.setdefault()
            agent = AgentGui(a[2].split("=")[1], 1)
            ip = str(a[0].split("=")[1])
            port = str(a[1].split("=")[1])

            agent.discovery(ip, port)
            agent.authorize(ip, port)
            agent.retrieve_poa(enc, ip, port)

            #     data = post_data.decode('utf-8')
            # print(data)
            self.send_response(307)
            self.send_header("Location", "/project.html")

            # self.headers.get("Host") +
            self.end_headers()
        else:
            print("ERROR: Fel")


nh.NetworkHandler().setup_server(82, WebbHostServer)
# This should probably be moved to a test file instead.
# a = AgentGui()
# a.discovery()
# a.authorize()
# a.retrieve_poa()
# a.transmit_to_vendor()
