import jwt

def generateJwt(payload, private_key):
    return jwt.encode(payload, private_key, algorithm="RS256")

def decodeJwt(token, public_key):
    return jwt.decode(token, public_key, algorithms=["RS256"])

def validatePoaPeriod(poa, now):
    valid_from = poa.get("Valid_from")
    valid_to = poa.get("Valid_to")
    return valid_from < now < valid_to

class Poa:
    def __init__(self, agent_mac, agent_name, agent_public_key,
                     principal_name, principal_public_key, valid_period, id, message):
        self.payload = {
                "Agent_MAC_Address": agent_mac,
                "Agent_Name": agent_name,
                "Agent_Public_Key": agent_public_key,
                "Principal_Name": principal_name,
                "Prinicpal_Public_Key": principal_public_key,
                "Valid_from": valid_period[0],
                "Valid_to": valid_period[1],
                "id": id,
                "Message": message
            }
    def setAgentMac(self, value):
        self.payload.update({"Agent_MAC_Address": value})

    def setAgentName(self, value):
        self.payload.update({"Agent_Name": value})

    def setAgentPublicKey(self, value):
        self.payload.update({"Agent_Public_Key": value})

    def setAgentPublicKey(self, value):
        self.payload.update({"Agent_Public_Key": value})

    def setPrincipalName(self, value):
        self.payload.update({"Principal_name": value})

    def setPrincipalPublicKey(self, value):
        self.payload.update({"Principal_Public_Key": value})

    def setValidPeriod(self, value):
        self.payload.update({"Valid_from": value[0]})
        self.payload.update({"Valid_to": value[1]})

    def setId(self, value):
        self.payload.update({"id": value})

    def setMessage(self, value):
        self.payload.update({"Message": value})

