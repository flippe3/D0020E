# This should probably be changed to a __init__.py
# but easiest way for Filip to make it this work in the terminal. 
import sys
sys.path.append("..")

import NetworkHandler as nh
import OauthDev.Util as Util
import Constants as CONSTS
import OauthDev.PublicKey as pb

class Verifier:

    def verify_poa(self, payload):
        try:
            return Verifier.verify_keys(self, payload["agent_public_key"], payload["principal_public_key"])
        except KeyError:
            print("Payload is missing mandatory data")
            return False

    def verify_keys(self, agent_public_key, principal_public_key):
        # Check keys
        return pb.verify_public_key(agent_public_key) and pb.verify_public_key(principal_public_key)


class VendorServer(nh.Server):

    def do_GET(self):
        super(VendorServer, self).do_GET()

    def do_POST(self):
        super(VendorServer, self).do_POST()
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself

        # splits the header data and the payload and returns the poa.
        poa = post_data.decode("utf-8").split('\n')[-1]
        print("Vendor received POA")
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

class Vendor:

    def setup_server(self):
        print("Vendor server starting")
        nh.NetworkHandler().setup_server(CONSTS.vendor_port, VendorServer)

Vendor().setup_server()



