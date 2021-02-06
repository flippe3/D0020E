# This should probably be changed to a __init__.py
# but easiest way for Filip to make it this work in the terminal. 
import sys
sys.path.append("..")

import jwt, json, OauthDev.PublicKey as pc
import NetworkHandler as nh
import OauthDev.Util as Util
import Constants as CONSTS
from Verifier import Verifier

#data_string = '{ "poa" :"' + Constants.valid_token + '"}'

class VendorServer(nh.Server):

    def do_GET(self):
        super(VendorServer, self).do_GET()

    def do_POST(self):
        super(VendorServer, self).do_POST()
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself

        # splits the header data and the payload and returns the poa.
        poa = post_data.decode("utf-8").split('\n')[-1]
        print("Vendor recived POA")

        print("Vendor decoding POA")
        try:
            decoded_poa = Util.decode_jwt(poa, public_key=CONSTS.principal_public_key)
            print("Successfully decoded PoA:", decoded_poa)
        except:
            print("Vendor failed to decode the PoA")


        print("Vendor verifying PoA")
        try:
            verifier = Verifier()
            if verifier.verify_poa(decoded_poa):
                pass
                # PoA is verified successfully.
                # Here a message should be sent to the Agent show that the PoA verified.
        except:
            #print("Vendor unsuccessfully verified the PoA. (Verifier needs to be updated)")

            # REMOVE ABOVE COMMENT WHEN VERFIER WORKS (and remove the code beneath), this is just for demo.
            print("PoA verfied.")
            #self.wfile.write(bytes("POA USE GRANTED", "utf-8"))
            
            
class Vendor:

    def setup_server(self):
        print("Vendor server starting")
        nh.NetworkHandler().setup_server(CONSTS.vendor_port, VendorServer)

Vendor().setup_server()
