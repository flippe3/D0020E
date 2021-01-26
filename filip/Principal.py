import socket
import Constants
import jwt
import random
import select as something

class Principal:
    poa_store = []
    principal_id = None

    def __init__(self):
        random.seed = 1
        self.principal_id = random.randint(0,999999)
    
    def setup_server(self):
        serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serversocket.bind((Constants.ip, Constants.principal_port))
        serversocket.listen(5)
        self.con_manager(serversocket)
        print("PRINCIPAL : server setup")

    def con_manager(self,serversocket):
        while True:
            (clientsocket, address) = serversocket.accept()
            readable, _, _ = something.select([clientsocket], [], [], 60)
            if(readable):
                data = clientsocket.recv(4096)
                self.recieve_request(data)
                clientsocket.close()

        
    def test_template_poa(self):
        f = open("PoaTemplate.txt", "r")
        s = f.read().encode('utf-8')
        print(s)
        self.transmit_to_agent(s)

    def transmit_to_agent(self, poa):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((Constants.ip, Constants.agent_port))
        client_socket.send(poa.encode())
        client_socket.close()
        print("PRINCIPAL : transmitted to agent")
        
        
    def generate_poa(self, agent_id, agent_public_key):
        encoded_poa = jwt.encode({"Agent_MAC_Address": "00:0a...",
		                  "AgeOAnt_Name": "Truck device", 
		                  "Agent_Public_key": str(agent_public_key), 
		                  "Message": "sadwd", 
		                  "Principal_ID": str(self.principal_id),
                                  "Client_ID": str(agent_id)}, "secret", algorithm="HS256")

        self.poa_store.append(encoded_poa)
        print("PRINCIPAL : generated poa")
        print("PRINCIPAL : " + encoded_poa)        
        transmit_to_agent(encoded_poa)
        
    def recieve_request(self, data):
        agent_id = data.decode("utf-8").split(',')[0]
        agent_public_key = data.decode("utf-8").split(',')[1]
        
        self.generate_poa(agent_id, agent_public_key)
        print("PRINCIPAL : recieved poa request")

#Principal().test_template_poa()
