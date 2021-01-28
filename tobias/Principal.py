import Constants
import NetworkHandler as nh
import random


class PrincipalServer(nh.Server):

    def do_GET(self):
        super(PrincipalServer, self).do_GET()
        content_length = int(self.headers.get('content-length', 0)) # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        #POA IMPUT DATA
        data = self.parse_responce(post_data)
        self.wfile.write(Principal().test_template_poa())

    def do_POST(self):
        super(PrincipalServer, self).do_POST()
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself


class Principal:
    def test_template_poa(self):
        f = open("../tests/PoaTemplate.txt", "r")
        s = f.read().encode('utf-8')
        print(s)
        return s

    poa_store = []
    principal_id = None

    def __init__(self):
        random.seed = 1
        self.principal_id = random.randint(0, 999999)

    # TODO: NEEDS IMPLEMENTATION
    def setup_server(self):
        print("PRINCIPAL : server starting")
        nh.NetworkHandler().setup_server(Constants.principal_port,PrincipalServer)


    def transmit_to_agent(self, poa):
        handler = nh.NetworkHandler()
        handler.send_msg("PoA", poa, Constants.agent_port)


#Principal().test_template_poa()
Principal().setup_server()