from http.server import BaseHTTPRequestHandler, HTTPServer
from http.client import HTTPConnection
from urllib.parse import parse_qs, urlparse
import requests


class NetworkHandler:

    def setup_server(self, port, method):
        server = HTTPServer(("localhost", port), method)
        server.serve_forever(1)

    #DONT USE
    def send_msg(self, keyword, msg, port, ip='localhost'):
        conn = HTTPConnection(ip + ':' + str(port))
        conn.request("POST", keyword, msg)
        res = conn.getresponse().read()
        print(res)
        return res
    #DONT USE
    def request_msg(self, payload, port, ip='localhost'):
        conn = HTTPConnection(ip + ':' + str(port))
        conn.request("GET", str(str(payload).encode("utf-8")))
        res = conn.getresponse().read()
        return res

    def requests_get(self, port, keyword, payload,data=""):
        r = requests.get("http://localhost:" + str(port) + "/" + str(keyword), params=payload, data=data)
        print(r.status_code)
        return r.text

    def requests_post(self, port, keyword, payload):
        r = requests.post("http://localhost:" + str(port) + "/" + str(keyword), data=payload)
        print(r.status_code)
        return r.text


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET")
        self.response()
        o = urlparse(self.path)
        query = parse_qs(o.query)
        print(query)
        self.wfile.write(bytes(str(query), "utf-8"))


    def do_POST(self):
        print("POST")
        self.response()
        content_length = int(self.headers.get('content-length', 0))  # <--- Gets the size of data
        #post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        #data = post_data.decode('utf-8')
        #print(data)
        #self.parse_responce(data)

    def response(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def parse_responce(self,data):
        parse = parse_qs(data)
        print(parse)
        return parse
        #self.wfile.write(bytes(str(parse), "utf-8"))
        # self.wfile.write(bytes("<html><head><title>Test</title></head>", "utf-8"))
        # self.wfile.write(bytes("<body>", "utf-8"))
        # self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
