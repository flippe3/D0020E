import Constants
import NetworkHandler


class Principal:

    def test_template_poa(self):
        f = open("PoaTemplate.txt", "r")
        s = f.read().encode('utf-8')
        print(s)
        self.transmit_to_agent(s)

    def transmit_to_agent(self, poa):
        nh = NetworkHandler.NetworkHandler()
        nh.send_msg("PoA", poa, Constants.agent_port)


Principal().test_template_poa()
