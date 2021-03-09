
# This should probably be changed to an __init__.py
# but easiest way for Filip to make it this work in the terminal.
import sys, os
sys.path.append("..")

from urllib.parse import parse_qs, urlparse

import NetworkHandler as nh
import requests

class AccessServer(nh.Server):
    
    def do_GET(self):
        super(AccessServer, self).do_GET()
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

    def PdfPage(self):
        print(self.path)
        f = open("../WebbPages/" + self.path[1:], "rb")
        self.send_response(200)
        self.send_header("Content-type", "application/pdf")
        self.end_headers()
        self.wfile.write(f.read())

    def do_POST(self):
        print(self.path)
        if self.path.endswith(".html"):
            self.HtmlPage()

        elif self.path.endswith(".pdf"):
            self.PdfPage()

        elif self.path =="/access":
            content_length = int(self.headers.get('content-length', 0))  # <--- Gets the size of data
            post_data = str(self.rfile.read(content_length).decode('utf-8'))  # <--- Gets the data itself
            data = post_data.split("&")
            
            poa = data[0].split('=')[1]
            agent_id = data[1].split('=')[1]
            principal_id = data[2].split('=')[1]
            print(poa, agent_id, principal_id)

            send = requests.post("http://localhost:4574", params={'poa': poa, 'agent_id': agent_id, 'principal_id': principal_id}).content.decode("utf-8")

            print(send)
            if send == "PoA Use Granted And Verified for use":
                self.send_response(307)
                self.send_header("Location", "/top-secret.pdf")
                self.end_headers()
            else:
                self.send_response(307)
                self.send_header("Location", "/denied.html")
                self.end_headers()
        else:
            print("Error")
            
nh.NetworkHandler().setup_server(83, AccessServer)

    
