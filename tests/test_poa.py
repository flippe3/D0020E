import pytest, os, sys
from pprint import pprint
from OauthDev.Poa import Poa
import OauthDev.Util as Util
import development.Constants as const
from datetime import datetime
import jwt

poa = Poa(const.agent_public_key, const.principal_public_key, const.vendor_public_key, const.exp)

poa.set_metadata(123)
payload = poa.generate_payload()
pprint(payload)

poa.set_metadata({"agent_name": "name123", "principal_name": "name321"})
payload = poa.generate_payload()
pprint(payload)

token = poa.generate_poa_web_token(const.principal_private_key)

#print(Util.get_current_time(Util.UTC), '\n', Util.get_current_time(Util.UTC))

expired_poa = Poa(const.agent_public_key, const.principal_public_key,
                  const.vendor_public_key, datetime(2021, 1, 30, 18, 0, 0).timestamp())
expired = expired_poa.generate_poa_web_token(const.principal_private_key)
try:
    Util.decode_jwt(expired, const.principal_public_key)
except jwt.ExpiredSignatureError:
    print("error")