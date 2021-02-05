import Util, development.Constants as const


class Poa:
    def __init__(self, agent_public_key, principal_public_key, resource_owner_id, exp):
        self.agent_public_key = agent_public_key
        self.principal_public_key = principal_public_key
        self.resource_owned_id = resource_owner_id
        self.exp = exp
        self.metadata = {

        }

    def setIat(self, iat):
        self.payload["iat"] = iat

    def setMetadata(self, metadata_key, value):
        self.metadata = {
            metadata_key: value
        }

