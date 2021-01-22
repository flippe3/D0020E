import socket
import socketserver
import select
import Constants


class Vendor:
    def __init__(self):
        self.setup_server()

    def setup_server(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((Constants.ip, Constants.vendor_port))
        serversocket.listen(5)
        self.con_manager(serversocket)

    def con_manager(self, server_socket):

        while True:
            (client_socket, address) = server_socket.accept()
            readable, _, _ = select.select([client_socket], [], [], 60)
            if (readable):
                data = client_socket.recv(4096)
                self.receive_from_agent(data)
                client_socket.close()

    def receive_from_agent(self, data):
        print(data.decode('utf-8'))



Vendor()
