import requests
import development.Constants as c


class KeyRegHandler:
    def __init__(self, ip, port):
        self.target = ip + ":" + str(port)
        # private don't use

    def __send_request(self, ip_address, search_value, function=""):
        if ip_address is None:
            ip_address = self.target
        print(ip_address)
        print("searching for ", search_value)
        return requests.post(ip_address + function, json={"search_value": search_value}).text

    def __handle_response(self, response):
        return response

    # ip address = "ip:xxxx:
    def get_public_key(self, id_of_actor, ip_address=None):
        response = self.__handle_response(self.__send_request(ip_address, search_value=id_of_actor, function="/getPk/"))
        return response

    def get_public_key_testing(self, id_of_actor):
        id = id_of_actor
        if id == "agent":
            return c.agent_public_key
        elif id == "principal":
            return c.principal_public_key
        elif id == "vendor":
            return c.vendor_public_key

    def get_user_id(self, public_key, ip_address=None):
        # gets id related to specific key
        response = self.__handle_response(
            self.__send_request(ip_address, search_value=public_key, function="/getUserId/"))
        return response

    # gets a response from server saying if public key is related to id
    def verify_public_key(self, public_key, ip_address=None):
        response = self.__handle_response(
            self.__send_request(ip_address, search_value=public_key, function="/verifyPk/"))
        return True if response == "True" else False

    # gets a response from server saying if id is related to public key
    def verify_id(self, id_of_actor, ip_address=None):
        response = self.__handle_response(
            self.__send_request(ip_address, search_value=id_of_actor, function="/verifyUserId/"))
        return True if response == "True" else False
