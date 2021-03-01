import NetworkHandler as nh
import OauthDev.Util as Util
import Constants as CONSTS
import OauthDev.PublicKey as pb


class WebbHostServer(nh.Server):
    def do_GET(self):
        super(WebbHostServer, self).do_GET()
        s = self.path.split(".")
        if s[1] == "html":
            print(self.path)
            f = open(self.path[1:], "r")
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f.read().encode("utf-8"))
            #print(f.read())

    def do_POST(self):
        super(WebbHostServer, self).do_POST()


class WebbHost:
    def startServer(self):
        nh.NetworkHandler().setup_server(82, WebbHostServer)


WebbHost().startServer()
