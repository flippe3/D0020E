import NetworkHandler as nh
import Constants


class AgentServer(nh.Server):

    def do_GET(self):
        super(AgentServer, self).do_GET()

    def do_POST(self):
        super(AgentServer, self).do_POST()
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        nc = nh.NetworkHandler()
        nc.send_msg("PoA", post_data, Constants.vendor_port)


class Agent:
    poa_store = []

    def setup_server(self):
        nw = nh.NetworkHandler()
        nw.setup_server(Constants.agent_port, AgentServer)


Agent().setup_server()
