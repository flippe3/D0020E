import Constants, jwt, json, OauthDev.PublicKey as pc
import NetworkHandler as nh
import OauthDev.Util as Util

data_string = '{ "poa" :"' + Constants.valid_token + '"}'


def verify_incoming_poa(poa):
    # code to check public keys etc
    return True


class VendorServer(nh.Server):

    def do_GET(self):
        super(VendorServer, self).do_GET()

    def do_POST(self):
        super(VendorServer, self).do_POST()
        print("Recived Request")
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        data = json.loads(data_string)
        print(data)
        poa = data["poa"]
        print(poa)
        try:
            poa = Util.decode_jwt(poa, pc.get_public_key("principal"))
        except jwt.ExpiredSignatureError:
            # Send back error
            print("error")
            return
        if verify_incoming_poa(poa):
            self.wfile.write(bytes("POA USE GRANTED", "utf-8"))


class Vendor:

    def setup_server(self):
        print("vendorServer starting")
        nh.NetworkHandler().setup_server(Constants.vendor_port, VendorServer)


Vendor().setup_server()
