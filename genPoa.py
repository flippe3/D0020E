import jwt

private_key = """-----BEGIN PRIVATE KEY-----
MIIBUwIBADANBgkqhkiG9w0BAQEFAASCAT0wggE5AgEAAkEAnyiYHOeVxqKTTC2D
MUmt7q6N6QC8GB6zqcXXr/+kKASocFb3MBwrcOga/vASQRj1PEcvvkgSlxjKcM+5
njSrjQIDAQABAkAn38C0RSTV/fcPN7vNhlsIGD0/acq19EMovoM5+b8DszkZ6a+w
YQZuHmcIdNT/C5Eo25+so4mxbRr8+JiPcL4VAiEA5PHRNtunhHPbq1mqH1VtwTQ0
1QG3nd/x1xBf27G806MCIQCx95BoGHKc3gIUs5KrJ2hHz44g6yIjt5eEKPPfm2b3
DwIgVTBtyt3c7Xo26QGKPfKJznRgnEnxSvuDf6UGJjdyrcUCIH1iOxZr6wwEChlF
rxbwy7KUU8Fzh/j8Fz7gj3lCBpgXAiABaWfZjOJTfEmPFgL/+4DZv6Ay+KMvVGIz
s28MHws7Bg==
-----END PRIVATE KEY-----"""

public_key = """-----BEGIN PUBLIC KEY-----
MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJ8omBznlcaik0wtgzFJre6ujekAvBge
s6nF16//pCgEqHBW9zAcK3DoGv7wEkEY9TxHL75IEpcYynDPuZ40q40CAwEAAQ==
-----END PUBLIC KEY-----"""


payload = {"poa": [{"Agent_MAC_Address": "00:0a...", "Agent_Name": "Truck device", "Agent_Public_key": "truckdevice123", "Message": "sadwd"}]}


encoded = jwt.encode(payload, private_key, algorithm="RS256")
decoded = jwt.decode(encoded, public_key, algorithms=["RS256"])


print(encoded)
print(decoded)
