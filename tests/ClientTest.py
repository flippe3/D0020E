import development.NetworkHandler as nh
import requests
from OauthDev.OAuth import OAuth
import json

# han = nh.NetworkHandler().requests_get("81","endpoint",{"name": "user", "passwd": "pass"})
# print(han)
##nh.NetworkHandler().request_msg({"name": "user", "passwd": "pass"}, 81)
# print(nh.NetworkHandler().requests_post("81","endpoint", {"name": "user", "passwd": "pass"}))


# discover
a = requests.get("http://localhost:81/discovery").content.decode("utf-8")
print(a)
b = requests.get("http://localhost:81/authorize",
                 params={'response_type': 'code', 'client_id': a, 'state': OAuth().generate_state()})
# b = requests.get("http://localhost:81/authorize?response_type=code&client_id="+a+"&state="+).content.decode("utf-8")
bjson = dict(b.json())

print(bjson)
c = requests.post("http://localhost:81/token", params={'grant_type': 'authorization_code', 'client_id': a, 'code': bjson.get("code")}).content.decode("utf-8")
print("c: "+c)