import socket
import Constants
class Principal:

    def test_template_poa(self):
        f = open("PoaTemplate.txt", "r")
        s = f.read().encode('utf-8')
        print(s)
        self.transmit_to_agent(s)

    def transmit_to_agent(self, poa):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((Constants.ip, Constants.agent_port))
        client_socket.send(poa)
        client_socket.close()


Principal().test_template_poa()

