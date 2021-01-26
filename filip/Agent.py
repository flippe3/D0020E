import socket
import select
import Constants
import jwt
import random

class Agent:
    poa_store = []
    agent_id = None
    public_key = None
    
    def __init__(self):
        random.seed = 1
        self.agent_id = random.randint(0,999)
        self.public_key = random.randint(999,999999)
        #self.setup_server()

    def setup_server(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((Constants.ip, Constants.agent_port))
        serversocket.listen(5)

        self.con_manager(serversocket)
        print("AGENT : server setup")
        
    def con_manager(self,serversocket):
        while True:
            (clientsocket, address) = serversocket.accept()
            print("AGENT : watiting for recieving PoA")
            readable, _, _ = select.select([clientsocket], [], [], 60)
            if(readable):
                data = clientsocket.recv(4096)
                self.receive_poa(data)
                clientsocket.close()

    def receive_poa(self,data):
        self.poa_store.append(data)
        self.transmit_to_vendor()

        
    def transmit_to_vendor(self):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((Constants.ip,Constants.vendor_port))
        client_socket.send(self.poa_store[len(self.poa_store) -1 ])
        client_socket.close()

    def request_poa(self):
        request = str(self.agent_id) + ',' + str(self.public_key) 

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((Constants.ip,Constants.principal_port))
        client_socket.send(request.encode())
        client_socket.close()
        print("AGENT : PoA request sent")

#Agent()


