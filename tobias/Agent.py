import socket
import select
import Constants
class Agent:
    poa_store = []

    def __init__(self):
       self.setup_server()

    def setup_server(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((Constants.ip, Constants.agent_port))
        serversocket.listen(5)
        self.con_manager(serversocket)

    def con_manager(self,serversocket):
        while True:
            (clientsocket, address) = serversocket.accept()
            readable, _, _ = select.select([clientsocket], [], [], 60)
            if(readable):
                data = clientsocket.recv(4096)
                self.receive_poa(data)
                clientsocket.close()

    def receive_poa(self,data):
        self.poa_store.append(data)
        self.transmit_to_vendor()


   # def request_poa(self):

    def transmit_to_vendor(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((Constants.ip,Constants.vendor_port))
        client_socket.send(self.poa_store[len(self.poa_store) -1 ])
        client_socket.close()


Agent()


