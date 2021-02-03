from typing import re

import development.NetworkHandler as networkHandler
import os, binascii, random, time,json
from http.server import BaseHTTPRequestHandler, HTTPServer
from http.client import HTTPConnection
from urllib.parse import parse_qs, urlparse

# assumptions: Adding a discovery giving out ClientID and setting clienttype to confidential
# Authorization response: responces instead of redirectiong
# 1 year expiery på accsess token
sessions = []
tokens = []


class OAuth:

    def generate_session(self):
        cid = self.generate_client_ID()
        s = OAuth.Session(cid)
        sessions.append(s)
        return s

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

    def generate_state(self):
        cid = binascii.b2a_base64(os.urandom(32))
        cid = cid.decode("ascii").replace('=\n','')
        return cid

    class Session:
        def __init__(self, cid):
            self.clientID = cid
            self.state = ""
            self.code = ""
            self.expire = 0

        def generate_code(self):
            self.expire = time.time() + 10 * 1000 * 60
            code = binascii.b2a_base64(os.urandom(128)).decode('ascii').replace('=\n', '')
            print("code: " + code)
            self.code = code
            return code

        def verify_valid_code(self, code):
            return self.expire > time.time() and code == self.code

    class OAuthServer(networkHandler.Server):
        def do_GET(self):
            super().do_GET()
            o = urlparse(self.path)
            query = parse_qs(o.query)
            if self.path.startswith("/authorize"):
                self.authorize(query)
            elif self.path.startswith("/discovery"):
                self.discovery(query)



        def do_POST(self):
            super().do_POST()
            o = urlparse(self.path)
            query = parse_qs(o.query)
            if self.path.startswith("/token"):
                self.token(query)



        def discovery(self, query):
            self.response()
            s = OAuth().generate_session()
            print("cid:" + s.clientID)
            self.wfile.write(bytes(s.clientID, "utf-8"))

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

        def authorize_response(self, session):
            self.response()

            print(session.state)
            print(session.clientID)
            code = session.generate_code()
            resJson = {"state": session.state, "code": code}
            encoded =json.JSONEncoder().encode(resJson)
            self.wfile.write(bytes(encoded, "utf-8"))
            # self.wfile.write(bytes("code:" + code, "utf-8"))

        def find_session(self, cid):
            print("findning client id")
            for x in sessions:
                if cid == x.clientID:
                    return x
            return None

        def token(self, query):
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
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            token = Token(query.get("client_id")[0])
            tokens.append(token)
            self.wfile.write(bytes(token.toJson(), "utf-8"))


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
