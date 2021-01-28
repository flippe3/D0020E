import NetworkHandler as nh
import Constants
import random


class AgentServer(nh.Server):

    def do_GET(self):
        super(AgentServer, self).do_GET()

    def do_POST(self):
        super(AgentServer, self).do_POST()
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        nc = nh.NetworkHandler()
        nc.requests_get(Constants.vendor_port,"UsePoa","",data=post_data)
        #nc.send_msg("PoA", post_data, Constants.vendor_port)


class Agent:
    poa_store = []

    def __init__(self):
        random.seed = 1
        self.agent_id = random.randint(0, 999)
        self.public_key = random.randint(999, 999999)


    def request_poa(self):
        request = str(self.agent_id) + ',' + str(self.public_key)
        PoA =nh.NetworkHandler().requests_get(Constants.principal_port, "poaRequest", request)
        print("AGENT : PoA request sent")
        self.poa_store.append(PoA)
        self.transmit_to_vendor()


    # WONT RUN DUE TO SERVER IMPLEMENTATION
    def receive_poa(self, data):
        self.poa_store.append(data)
        self.transmit_to_vendor()

    def transmit_to_vendor(self):
        print("Transmitting PoA")
        nh.NetworkHandler().requests_post(Constants.vendor_port, "usePoA",
                                          self.poa_store[len(self.poa_store) - 1])

    def setup_server(self):
        nw = nh.NetworkHandler()
        nw.setup_server(Constants.agent_port, AgentServer)

a = Agent()
a.request_poa()
