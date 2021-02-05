import Util, development.Constants as const


class Poa:
    def __init__(self, agent_public_key, principal_public_key, resource_owner_id, exp):
        self.payload = {
            "agent_public_key": agent_public_key,
            "principal_public_key": principal_public_key,
            "resource_owner_id": resource_owner_id,
            "exp": exp
        }

    def setIat(self, iat):
        self.payload["iat"] = iat
    def setMetadata(self, metadata_key, value):
        self.payload["metadata"] = {
            metadata_key: value
        }

poa = Poa(const.agent_public_key, const.principal_public_key, const.vendor_public_key, const.exp)

print(poa.payload)
poa.setIat(41414141)
print(poa.payload)
poa.setMetadata("agent_name", const.agent_name)
print(poa.payload)

print(Util.generate_jwt(poa.payload, const.agent_private_key))