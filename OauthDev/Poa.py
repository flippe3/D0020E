import Util, development.Constants as const
import jwt
from datetime import datetime


class Poa:
    def __init__(self, agent_public_key, principal_public_key, resource_owner_id, exp):
        self.agent_public_key = agent_public_key
        self.principal_public_key = principal_public_key
        self.resource_owner_id = resource_owner_id
        self.exp = exp
        self.metadata = {

        }

    def set_iat(self, iat):
        self.payload["iat"] = iat

    def set_metadata(self, metadata_key, value):
        self.metadata = {
            metadata_key: value
        }

    def generate_payload(self):
        return {
            "agent_public_key": self.agent_public_key,
            "principal_public_key": self.principal_public_key,
            "resource_owner_id": self.resource_owner_id,
            "metadata": self.metadata,
            "iat": datetime.now().timestamp(),
            "exp": self.exp
        }

    def generate_poa_web_token(self, private_key, payload=None):
        if payload is None:
            payload = self.generate_payload()
        else:
            payload = payload
        return jwt.encode(payload, private_key, algorithm="RS256")


poa = Poa(const.agent_public_key, const.principal_public_key, const.vendor_public_key, const.exp)

print(poa.generate_payload())
print(poa.generate_poa_web_token(const.principal_private_key))