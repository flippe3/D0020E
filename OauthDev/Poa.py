import jwt
from datetime import datetime


class Poa:
    def __init__(self, agent_public_key=None, principal_public_key=None, resource_owner_id=None, exp=datetime.utcnow().timestamp()+360000, metadata=None, iat=datetime.utcnow().timestamp()-36000, nbf = None):
        self.agent_public_key = agent_public_key
        self.principal_public_key = principal_public_key
        self.resource_owner_id = resource_owner_id
        self.exp = datetime.utcnow().timestamp()+360000
        self.metadata = metadata
        self.iat = iat
        self.nbf = nbf

    def set_metadata_value(self, metadata_key, value):
        self.metadata = {
            metadata_key: value
        }

    def set_metadata(self, metadata):
        if isinstance(metadata, dict):
            self.metadata = metadata

    def set_agent_public_key(self, agent_public_key):
        self.agent_public_key = agent_public_key

    def set_principal_public_key(self, principal_public_key):
        self.principal_public_key = principal_public_key

    def set_resource_owner_id(self, resource_owner_id):
        self.resource_owner_id = resource_owner_id

    def set_expiration_date(self, expiration_date):
        self.exp = expiration_date

    def set_start_date(self, start_date):
        self.iat = start_date

    def generate_payload(self):
        payload = {
                "agent_public_key": self.agent_public_key,
                "principal_public_key": self.principal_public_key,
                "resource_owner_id": self.resource_owner_id,
                "iat": self.iat,
                "exp": self.exp
            }
        if self.metadata is not None:
            payload["metadata"] = self.metadata
            
        return payload

    def generate_poa_web_token(self, private_key, payload=None):
        if payload is None:
            payload = self.generate_payload()

        return jwt.encode(payload, private_key, algorithm="RS256")


