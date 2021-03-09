import binascii
import json
import os
#import time
from urllib.parse import parse_qs, urlparse

import development.NetworkHandler as networkHandler
from OauthDev.Poa import Poa as POA 
from development import Constants as CONSTS
from datetime import datetime

#This file handles ServerSide Oauth authentication, to use it first send a get request to '/discovery' to get a userId
# as a responce . This gives you the required information to request a authenficaion token by GET requesting '/authorize'
# and sending 'response_type', 'client_id', 'state'(generated yourself) as parameters in the url.
# This will give u 10 minutes of a usable access token as a responce.

#This class also contains a basic example of server side Token handeling look at '/token' as a post Request

# assumptions: Adding a discovery giving out ClientID
# Authorization response: responces instead of redirectiong
# 1 year expiery på accsess token
sessions = []
tokens = []




class OAuth:

    #Generates a session key for a oauth session
    def generate_session(self):
        cid = self.generate_client_ID()
        s = OAuth.Session(cid)
        sessions.append(s)
        return s

    #generates a Unique Client id
    def generate_client_ID(self):
        cid = ''
        b = True
        while b:
            b = False
            cid = self.generate_state()
            for x in sessions:
                if cid == x.clientID:
                    b = True
        return cid

    #Generates a random base 64 string
    def generate_state(self):
        cid = binascii.b2a_base64(os.urandom(32))
        cid = cid.decode("ascii").replace('=\n','')
        return cid


    #Holds data around a Oauth Authentification event TODO: might want to save accross restars
    class Session:
        def __init__(self, cid):
            self.clientID = cid
            self.state = ""
            self.code = ""
            self.expire = 0

        #generates the code used for the 'Code' parameter in Oauth authentification
        def generate_code(self):
            self.expire = datetime.utcnow().timestamp() + 10 * 1000 * 60    # 10 minutes
            code = binascii.b2a_base64(os.urandom(128)).decode('ascii').replace('=\n', '')
            print("code: " + code)
            self.code = code
            return code

        #Verifys that a token request contains a valid key
        def verify_valid_code(self, code):
            return self.expire > datetime.utcnow().timestamp() and code == self.code

    #This is a Http Server configured for responding to Oauth requests
    class OAuthServer(networkHandler.Server):

        #All GET requests will go here
        def do_GET(self):
            super().do_GET()
            o = urlparse(self.path)
            query = parse_qs(o.query)
            if self.path.startswith("/authorize"):
                self.authorize(query)
            elif self.path.startswith("/discovery"):
                self.discovery(query)


        #All Post requests goes here
        def do_POST(self):
            super().do_POST()
            o = urlparse(self.path)
            query = parse_qs(o.query)
            if self.path.startswith("/token"):
                self.token(query)


        #handels the get discovery, and thereby gives the user its user ID #TODO does this want to be a siged message by Agent?
        def discovery(self, query):
            self.response()
            s = OAuth().generate_session()
            print("cid:" + s.clientID)
            self.wfile.write(bytes(s.clientID, "utf-8"))


        #once a client has its User id it can request its code, This code valides the userid
        def authorize(self, query):
            print("authorizing")
            if query.get("response_type")[0] == "code":
                cid = query.get("client_id")[0]
                session = self.find_session(cid)
                if session is None:
                    print("ID does not exist")
                    print(cid)
                else:
                    session.state = query.get("state")[0]
                    print("sending response")
                    self.authorize_response(session)


            else:
                print("invalid response type:")
                print(query.get("response_type"))

        #the responce the client will recive on a authorize request
        def authorize_response(self, session):
            self.response()

            print(session.state)
            print(session.clientID)
            
            code = session.generate_code()
            resJson = {"state": session.state, "code": code}
            encoded =json.JSONEncoder().encode(resJson)
            self.wfile.write(bytes(encoded, "utf-8"))
            # self.wfile.write(bytes("code:" + code, "utf-8"))


        #once a request containg a userid is sent this will find the relevant session for that data to be extraced
        def find_session(self, cid):
            print("findning client id")
            for x in sessions:
                if cid == x.clientID:
                    return x
            return None


        #this validates the code sent out in authorize
        def token(self, query):

            content_length = int(self.headers.get('content-length', 0))  # <--- Gets the size of data
            post_data = self.rfile.read(content_length)  # <--- Gets the data itself
            data = post_data.decode('utf-8')
            query = parse_qs(data)


            if query.get("grant_type")[0] == "authorization_code":
                cid = query.get("client_id")[0]
                if cid is None:
                    print("no Valid Client ID")
                session = self.find_session(cid)
                if session.verify_valid_code(query.get("code")[0]):
                    self.token_response(query)
                else:
                    print("code wrong or invalid")

            else:
                print("wrong grant type")
                print(query.get("grant_type")[0])

        def token_response(self, query):
            print("generating POA webtoken")
            # This generates the PoA, should be updated with real metadata in the future.
            metadata = json.loads(query.get("metadata")[0])
            if(metadata.__contains__("exp")):
                poa = POA(agent_public_key=CONSTS.agent_public_key, principal_public_key=CONSTS.principal_public_key,
                          resource_owner_id=CONSTS.vendor_public_key, exp=metadata["exp"], iat=metadata["iat"],
                          metadata=metadata["meta"])
            else: poa = POA(agent_public_key=CONSTS.agent_public_key, principal_public_key=CONSTS.principal_public_key,
                          resource_owner_id=CONSTS.vendor_public_key, metadata= metadata)


            poa_webtoken = poa.generate_poa_web_token(private_key=CONSTS.principal_private_key)            
            print("poa generation successful")

            # Sends the PoA to the Agent.
            #self.send_response(200)
            #self.send_header("Content-type", "application/jwt")
            #self.end_headers()
            tokens.append(poa_webtoken)

            self.wfile.write(bytes(poa_webtoken, "utf-8"))

'''
#Simple Accsess token example
class Token:
    def __init__(self, host):
        oauth = OAuth()
        self.host = host
        self.access_token = oauth.generate_state()
        self.token_type = ""
        # 1 year expiry
        # dont use
        self.expires_in = 1000 * 60 * 60 * 365
        self.expiry_time = time.time() + self.expires_in
        self.refresh_token = oauth.generate_state()
        # self.example_parameter = ""

    def still_valid(self):
        pass

    def toJson(self):
        js = {'access_token': self.access_token,
                'token_type': self.token_type,
                'expires_in': self.expires_in,
                'refresh_token': self.refresh_token}
        return json.JSONEncoder().encode(js)
'''
