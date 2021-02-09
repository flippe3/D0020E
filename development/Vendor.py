# This should probably be changed to a __init__.py
# but easiest way for Filip to make it this work in the terminal. 
import sys
sys.path.append("..")

import jwt, json, OauthDev.PublicKey as pc
import NetworkHandler as nh
import OauthDev.Util as Util
import Constants as CONSTS
#from Verifier import Verifier

#data_string = '{ "poa" :"' + Constants.valid_token + '"}'

import datetime  # Only used to check 'exp', but 'exp' is already checked during the decoding so
import Register  # Behövs inte än. Ska fixa register


class Verifier:

    def verify_poa(self, payload):
        try:
            agent_public_key = payload["agent_public_key"]
            principal_public_key = payload["principal_public_key"]
            resource_owner_id = payload["resource_owner_id"]
            exp = payload["exp"]

            return Verifier.verify_payload(self, agent_public_key, principal_public_key, resource_owner_id, exp)

        except KeyError:
            print("Payload is missing mandatory data")
            return False

    def verify_payload(self, agent_public_key, principal_public_key, resource_owner_id, exp):

        # Check keys
        if (agent_public_key != CONSTS.agent_public_key):
            print("Incorrect agent_public_key")
            return False
        if (principal_public_key != CONSTS.principal_public_key):
            print("Incorrect principal_public_key")
            return False
        if (resource_owner_id != CONSTS.vendor_public_key):
            print("Incorrect vendor_public_key")
            return False

        if (exp < datetime.datetime.utcnow().timestamp()):  # This is automatically checked when POA gets decoded
            print("POA has expired")
            return False

        return True


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
            print("Vendor failed to decode the PoA") # This will happen if poa is expired btw
            self.wfile.write("PoA NOT DECODED And therefore can not be used".encode("utf-8"))
            return


        print("Vendor verifying PoA")
        

        if (Verifier().verify_poa(decoded_poa)):
            print("PoA Verified And Used.")
            self.wfile.write("PoA Use Granted And Verified for use".encode("utf-8"))
            # PoA is verified successfully.
            # Here a message should be sent to the Agent show that the PoA verified.
        else:
            print("Vendor unsuccessfully verified the PoA.")
            self.wfile.write("PoA Use NOT ALLOWED".encode("utf-8"))

    
        # REMOVE ABOVE COMMENT WHEN VERFIER WORKS (and remove the code beneath), this is just for demo.
        
        #self.wfile.write(bytes("POA USE GRANTED", "utf-8"))



class Vendor:

    def setup_server(self):
        print("Vendor server starting")
        nh.NetworkHandler().setup_server(CONSTS.vendor_port, VendorServer)

Vendor().setup_server()



