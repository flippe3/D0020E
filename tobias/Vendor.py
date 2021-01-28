import Constants
import NetworkHandler as nh


class VendorServer(nh.Server):

    def do_GET(self):
        super(VendorServer, self).do_GET()

    def do_POST(self):
        super(VendorServer, self).do_POST()
        print("Recived Request")
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        print(post_data.decode("utf-8"))
        self.wfile.write(bytes("POA USE GRANTED", "utf-8"))


class Vendor:

    def setup_server(self):
        print("vendorServer starting")
        nh.NetworkHandler().setup_server(Constants.vendor_port, VendorServer)



Vendor().setup_server()
