# This should probably be changed to a __init__.py
# but easiest way for Filip to make it this work in the terminal.
import socketserver
import sys
from typing import Tuple

sys.path.append("..")

import NetworkHandler as nh
import OauthDev.Util as Util
import Constants as CONSTS
from OauthDev.KeyRegHandler import KeyRegHandler
from urllib.parse import parse_qs, urlparse


class Verifier:
    def __init__(self, kr):
        self.kr = kr

    def verify_poa(self, payload):
        try:
            return Verifier.verify_keys(self, payload["agent_public_key"], payload["principal_public_key"])
        except KeyError:
            print("Payload is missing mandatory data")
        return False

    def verify_keys(self, agent_public_key, principal_public_key):
        # Check keys
        a = self.kr.verify_public_key(principal_public_key)
        print("Vefifying one key ", a)
        b = self.kr.verify_public_key(agent_public_key)
        print("Verifying second key", b)
        return a and b



class VendorServer(nh.Server):

    def __init__(self, request: bytes, client_address: Tuple[str, int], server: socketserver.BaseServer):
        super().__init__(request, client_address, server)
        self.verifier = Verifier
        self.kr = KeyRegHandler


    def set_keyreg_and_verifier(self, kr: KeyRegHandler):
        self.kr = kr
        self.verifier = Verifier(kr)


    def do_GET(self):
        super(VendorServer, self).do_GET()


    def do_POST(self):
        super(VendorServer, self).do_POST()
        
        o = urlparse(self.path)
        payload = parse_qs(o.query)
        print("PAYLOAD \n", payload)

        poa          = payload.get("poa")[0]
        agent_id     = payload.get("agent_id")[0]
        principal_id = payload.get("principal_id")[0]

        try:
            decoded_poa = Util.decode_jwt( poa, public_key=self.kr.get_public_key( id_of_actor = principal_id))
            print("Successfully decoded PoA:\n", decoded_poa)

        except:
            print("Vendor failed to decode the PoA")  # This will happen if poa is expired
            self.wfile.write("PoA NOT DECODED And therefore can not be used".encode("utf-8"))
            return

        print("Vendor verifying PoA")
        if self.verifier.verify_poa(decoded_poa):
            print("PoA Verified And Used.")
            self.wfile.write("PoA Use Granted And Verified for use".encode("utf-8"))
        else:
            print("Vendor unsuccessfully verified the PoA.")
            self.wfile.write("PoA Use NOT ALLOWED".encode("utf-8"))



class Vendor:

    def setup_server(self, keyreghandler):
        print("Vendor server starting")
        vs = VendorServer
        vs.set_keyreg_and_verifier(kr=keyreghandler, self=vs)
        nh.NetworkHandler().setup_server(CONSTS.vendor_port, vs)


keyreghandler = KeyRegHandler("http://fnilsson.com", 80)
Vendor().setup_server(keyreghandler)
