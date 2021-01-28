import NetworkHandler as nh

han = nh.NetworkHandler().requests_get("81","endpoint",{"name": "user", "passwd": "pass"})
print(han)
#nh.NetworkHandler().request_msg({"name": "user", "passwd": "pass"}, 81)
print(nh.NetworkHandler().requests_post("81","endpoint", {"name": "user", "passwd": "pass"}))