from http.server import BaseHTTPRequestHandler, HTTPServer
from http.client import HTTPConnection, HTTPResponse
import time


class NetworkHandler:

    def setup_server(self, port, method):
        server = HTTPServer(("localhost", port), method)
        server.serve_forever(1)

    def request_msg(self, keyword, port, ip='localhost'):
        conn = HTTPConnection(ip + ':' + str(port))
        conn.request("GET", keyword)
        res = conn.getresponse().read()
        return res

    def send_msg(self, keyword, msg, port, ip='localhost'):
        conn = HTTPConnection(ip + ':' + str(port))
        conn.request("POST", keyword, msg)
        res = conn.getresponse().read()
        print(res)
        return res

class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        print("GET")
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print(self.path)

        #content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        #post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        #print(post_data.decode("utf-8"))
        #self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        #self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        #self.wfile.write(bytes("<body>", "utf-8"))
        #self.wfile.write(bytes("<form method=\"post\" action=\"/action_page.php\">\n<label for=\"fname\">First name:</label><br>\n<input type=\"text\" id=\"fname\" value=\"John\"><br><br><input type=\"submit\" value=\"Submit\"></form> ", "utf-8"))
        #self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        #self.wfile.write(bytes("</body></html>", "utf-8"))

    def do_POST(self):
        print("POST")
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
    # self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

    # content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
    # post_data = self.rfile.read(content_length)  # <--- Gets the data itself
    # print("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
    #              str(self.path), str(self.headers), post_data.decode('utf-8'))
    # print("POST request",post_data.decode('utf-8'))
