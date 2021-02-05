from datetime import datetime
            #server stuff
#------------------------------------#
ip = "localhost"
agent_port = 4573
principal_port = 4573
vendor_port = 4574


            #poa stuff
#------------------------------------#
principal_private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEoQIBAAKCAQBmotk9JSb/X/xZWYtYv1Tizsntwg0bEsJOVXdvWCA/6vmsmoCV
S6VQde1RXdV4i/EASssk4qTzSPCZvUZ2+CXS3veti18WXjpFwo/GjrQ81m/c3ole
8GhQ1Uc7Ufg99uGqbaEu9Y/MEQ1TeWC2jjy7V3VGSmg9CuGeECk5CEOr23qdAvwU
GwcJsyfTidgwjfQ5qSCrbYwNUSs/R/XNGyyXxu7ll4AK47iFXG0w11pFgAVnGEwA
zrmei+JnkNFisjnrKc9bI7MIfQQPTaV8d0DmuaQMWZK7aajV9VMx5a5KwTh+VD3p
A/US3FAdFXh/lcxPfXsrMxfVgOHhpMcdE8l/AgMBAAECggEAM0oB4UplmIxw4H2c
4vaKBuVrh0LHpdXT/606CAwz4X0c06JJy1GIBRNJSrXnbVwRTSITLhWMdH7orQsm
4WDUFfKSNslE9TqVSDMYAhNiAlzufaM/ZpAgsPRDqmMl+GEdGDu8pmjUORf0Xthy
+gdOVhg4ZK3eNVLwuDo/P17f4kshgcOAyWKresMlZlXA/Q7i1M7ooVVoRDLE6SqH
SOfXEVUZxp4w9H0KsN40L2E33XTY9WqLexHpvVouRuxkn7l/PiAvkkEeNUjX+7r6
8+AXmS2FB4J1UpP9XWoFFsMYaGvYy7YiSplN5GCx99XOCepbrhaZqqFZo5p1Cs8p
E6A+gQKBgQC+JZVWocD/1GlsPoa7JwppZU/ZZdJN/FnTv3GZSxpXNzxYpxGpciXB
hQLGX02Jyxk2gkigQydZ8FwHAwAjUITe2hA8jbRZ2tqYr9MVd5RQiNPiIWsJV03s
S2STFSr4nFXfQkgeu1+Ji6t3SiTJ4fsQSYwLTGikQseegR0S/4naHwKBgQCKLpFh
XwBk35huUy+Mo5V1kfh2x8157ixgvUQfCn3HACyy0xrMZfLUE56SZ4AYnzKOt0JC
D5AayffsRLrc6IdBxkwyhwQRKrPnS8HcrfSf6Aryu7zswAIJCoP5TzVwmavr4Y2J
XxwvY16ikkAKBwTDviLHTJ/dC6YTYz+uNyLkoQKBgHfs0FGBV26DE7KXhPZI20I6
CbB9jbRt8mGgnw8l1Qko50CqrnMGcVWqhGOE/CxqEg7VAOVDNXB+Liyl8dJUGFlN
g2wNm7AIXlJqomEpuDtK8QfwN8f+bkEYE+jIMv/16hsTfNUVLF5d3tkvxCAoDObq
3A7MNDtVev03RZUT4mfVAoGAKvoGz1D7z2PXheCrdkNedb2bmF3WI2kXNlNHP5xE
uELupAOSXyYKGzmq5P/50C6bS9XlbqRmfl54lGxf7dsITkW9Zy2k7y3n3DUsq1UT
MzS5Svtm6/9f4q35k+21wjqZRPjWy3XgT0DJqyhvcG70ZWjaakADrH01/uusX6PY
X2ECgYATxWgJRw59MUE00hg6aN67mI6bA1BcwKCjcehrZARBcMJZ6cEABc89sL/u
57IQ/Axj6rqeEimTR7aiTnls9GxRZtDb+/x4VhggQVP/Z0HsyhlolRcyP6PsO9mx
jSBD5u6fBvc/HZg/Lok2JbAnV2POK/9H0RiOMTOkXdoyJg+BTg==
-----END RSA PRIVATE KEY-----"""

principal_public_key = """-----BEGIN PUBLIC KEY-----
MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQBmotk9JSb/X/xZWYtYv1Ti
zsntwg0bEsJOVXdvWCA/6vmsmoCVS6VQde1RXdV4i/EASssk4qTzSPCZvUZ2+CXS
3veti18WXjpFwo/GjrQ81m/c3ole8GhQ1Uc7Ufg99uGqbaEu9Y/MEQ1TeWC2jjy7
V3VGSmg9CuGeECk5CEOr23qdAvwUGwcJsyfTidgwjfQ5qSCrbYwNUSs/R/XNGyyX
xu7ll4AK47iFXG0w11pFgAVnGEwAzrmei+JnkNFisjnrKc9bI7MIfQQPTaV8d0Dm
uaQMWZK7aajV9VMx5a5KwTh+VD3pA/US3FAdFXh/lcxPfXsrMxfVgOHhpMcdE8l/
AgMBAAE=
-----END PUBLIC KEY-----"""

agent_private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAnm4Eob0WzTQaxn2dLbkjVQRQpypJtdf7XI4ltuwb3ffPQXq7
k0s/ULpXGVpw5mbF3AuGIE5+77HiCB5o7QQHkV9anDjuEKOOGfxJTII/zzoceReW
OHWn+JtTDlLucwtfk61CyJoDaR67zU/TTBFWNspyox/RNMCgOcTIAsfLYj+rMsq6
znyPiB5KWoZIC9hA00EPTDgrDCDbubMpdVUm7+DDMVpfhyueR94W3wx0tF1MNaqs
TuWkWXcbev2gwb5E8TBymB0lCgNB3P6KS8RRLYat5TVDKjomcroxd+gKX9yT31eJ
c+FhjxHcByFQ8AjnlVA2tE35pyfO2YPv0V0pKwIDAQABAoIBAGviV10cOm66UJFh
8Kq2LA00xwdOkKs3zH+WfLA30DIzEftw7FK9Jvx+J9mn8MG0sn/JiShuy5nF9Dm7
G5Bq8gxYdodzbQn/lkCzv+ZNu84NsF31ZeJEnIF6o/BZIO9Oi2Mw1Q1tc20d9J03
ApgGJkNhUPcsL3ZQxcsQ6XKbQzA/O3SJ00XLOUsf1dRtW/StMJ4wPbL/X76m8hSI
DSd++u7cscI97sFDnNfNa0i3ePBOappesZKmId/SIR47y8ISFw/DtasjUq1imaMD
c9MS5eOXF39V2RJgEBByEWlrcsN/33jiR3XsoxCp/15tOlv9N6NgKggYfgabE7+2
cb4RDYECgYEA9Oy7ASC0wZU3QDnumccODJruhGruGMOXRu8oPNxbUd9Of3McNFa/
wl5CNk0nSrrS60dYPWV930WcrICQGPYGS0t2+WOpaTUXwD/IkRpUqTomb6NeFMJr
xtdL5HU2ZU7M3+yp+YqAJBjKNlWJvpJzSQlPv1zKE/cKCAK9UKmoyJsCgYEApZgD
s/2Xt20UU/atHAEMh/8jUmSq6FPs/6xPwwAdLU0x3j1QucaD9l8q1M9H40ghtW8J
jzvfSd+VgCmBmJqa8WY9+VZzhEzY7SBQTFrn0JKKmvcIB4MU3sRIupOz8DIEvbIC
HQYPkoM3AwJymjqSi/sUsiBFhRf7qqVuV9C/wrECgYEAn9I+MP0zlkKVXB6xeL0w
iL8st1HDbntrIol620P7fxBVe8sUc37MALxbPm3YHuaMLaVPijjJC0G0e8gkv3UD
JGzpBNGowZM4nWXBrhXdetQMMrsK8Ebx5z2kMz7dMPxbqh8Xx1M+TM+0XAIzMR0F
h3pBBKE66A5DCHkpKhKbpdMCgYBa36JgmzEwMwct0LhNHvI+i7BZne8AklYENQ6M
h7p7StqsCGANozh18uHxaVMdEk+VXrsTRJsT0kQb0itRkL6o7R/jfiLknruI3evT
CyweFN1Fj31ziebhHTyAT2A212wsocxxGwteru14lFZJ9wzHDuHbosQj9vZgPmrg
fClP8QKBgCIIsomgmIlfT9iYEiaH0lhsjuFpUaCfC4kVjbI3UlnnUzPMVdfgOrVr
ZaDQDuvIE2wGlVYBjFROXD4YHKh2kT8dtdvmGq3UIWWkdoS8RLFcMvg2PIA+Y2vP
Ou9tPaEl9vCHa+mwYt2fvdB4UVhskeSDufuuOw7ZD8DS01/zfdHY
-----END RSA PRIVATE KEY-----"""

agent_public_key = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAnm4Eob0WzTQaxn2dLbkj
VQRQpypJtdf7XI4ltuwb3ffPQXq7k0s/ULpXGVpw5mbF3AuGIE5+77HiCB5o7QQH
kV9anDjuEKOOGfxJTII/zzoceReWOHWn+JtTDlLucwtfk61CyJoDaR67zU/TTBFW
Nspyox/RNMCgOcTIAsfLYj+rMsq6znyPiB5KWoZIC9hA00EPTDgrDCDbubMpdVUm
7+DDMVpfhyueR94W3wx0tF1MNaqsTuWkWXcbev2gwb5E8TBymB0lCgNB3P6KS8RR
LYat5TVDKjomcroxd+gKX9yT31eJc+FhjxHcByFQ8AjnlVA2tE35pyfO2YPv0V0p
KwIDAQAB
-----END PUBLIC KEY-----"""

vendor_private_key = """-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAmVn08AULwdKSwqpWDRhPDbaR0xQNZYzphhZ59uK0ElGZcUr4
ybFPEYeC5qxp/ntEuoU0cFlsCAWt/dG4R1yaaN2okWVydDQWNh5q6rVg9XjFCq3Q
Rp4nQFlpgmxDbdRbN6CHbg2r0HBo2cl8IV4r7wpEOxYFQ6ZkwLaQ9Jwo05FZskmO
MhFqPIpC96AMftV3/3Usu9IORB8nlNhRxylqea3HFKMBAJo5otSWQ3zvUXYcYPZO
QqC5pu/GOSEuRa7g+uFX8DgJo4C0SaUwhBuPBr8rs9EbCHBxxT4TXpDUHzrJL0iY
RJ7vJgPwrV8dvbh1Mek4m7bimnWug8bdh5xD1wIDAQABAoIBAQCW2GgZ2bzQ8aOv
nQJ8axcINDiJW0Y6SDxFy8I5WpMrGd1IFilXrPRMF/JpmdvBmdvnZbRJd4zO71dR
P4R3nd29nZx9OT82ky3uGkmtirFPhXa9pHAlptiRceJZislhNexscZoGZahGpuxc
ntdds1agEoc/X8/Z1clxz6QTGbEHOoLX9KCg0u7sMwihPumQPnr8yAeCCxlNl/h+
PWEleC3uucjtcgrzIbK0Wx/QmoE0woqxMZawc/JteFDNIkHPV/pNGB8nFsGhITHF
DafkqXeFxNjKmIjXzwRliqLLOpvXfA067tTNc/vnzTopvo3ldR7AX75H9OVsupRh
dUirtxshAoGBAM4ZXsYK4x5z2qGh9WXSXF9IrJ6KjMZPpcGVJQ436lt44dlNlvU5
9o9kaiqpZF4+f+oPMxKm2mpjgtyRwgloXxbp0zcSmy2XwTywZioY120R40SYNENn
BxWLAPepIP7XL2AwRSJ/9SolNb1qAN9CtqyWK1KAzoT3fbN0aXeiRgiPAoGBAL57
IM1be1YKbG+nvilpxD2Ph3fb2aS3f0JovGhkWGua8Hrlpv8GKookLvLbsnBnJEuL
dh1ldKMEEVqyaDXQjrFWoH5hQzSZ/zMUnT1CKPY0wp7gQ3SVE/MH/g/cC84gCk+w
QDHiplE3D9epiIulhnsH/+NDVCKzAP+kev1zy+Q5AoGAPD6UQoWqMBuje/3QssvT
7pJayxkq30km5bhIFajom4ZxVkjk6Jfh57ZthjzvttDEKVH6FuipDdI6zWjZ9FAL
A7Kj6ARLUf97H9dcdc+/IQXKjiGDnXQ/UN/KD5rjpzqVgaN6ggQvUPuBgvW6fYiN
x1M6JKq8M4f4uX082xiXKicCgYAF7SDFIt6Ae8yJ4Mcq1K6VV7zYPs/Trx3XfBi4
ir6xgl2PBUwfzRpPt/Z5+dngY2UesJUZLwnk9IBxuPFDE10NKWvO4snLfisRdMe7
my5ZEqUnekS/ANBhFFOUPL1lSVvoxMwKgUm5ZyQoCo9EAP9hHouYj4Szm6whSAXH
ku26CQKBgQCM94l88H/x67BIkyog5Qgdyz3uXjiZqKl34wrBz5kQIt2sOFtw0ddR
Cp+IIifcunANUesqNm+yPEiJr22hoSnzYgzyzdo7A53jedC8Qrr1ZT75pgr/op0x
VXiWCBjq0W++ZLEuARU703TaBCMbKmIM6zv3OSvUyZDq8sLKjc4E9A==
-----END RSA PRIVATE KEY-----"""

vendor_public_key = """"-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAmVn08AULwdKSwqpWDRhP
DbaR0xQNZYzphhZ59uK0ElGZcUr4ybFPEYeC5qxp/ntEuoU0cFlsCAWt/dG4R1ya
aN2okWVydDQWNh5q6rVg9XjFCq3QRp4nQFlpgmxDbdRbN6CHbg2r0HBo2cl8IV4r
7wpEOxYFQ6ZkwLaQ9Jwo05FZskmOMhFqPIpC96AMftV3/3Usu9IORB8nlNhRxylq
ea3HFKMBAJo5otSWQ3zvUXYcYPZOQqC5pu/GOSEuRa7g+uFX8DgJo4C0SaUwhBuP
Br8rs9EbCHBxxT4TXpDUHzrJL0iYRJ7vJgPwrV8dvbh1Mek4m7bimnWug8bdh5xD
1wIDAQAB
-----END PUBLIC KEY-----"""

agent_name = "Agent-1"
principal_name = "Principal-1"
iat = datetime(2021, 1, 1, 18, 0, 0).timestamp()
exp = datetime(2021, 12, 30, 18, 0, 0).timestamp()

valid_poa_payload = {
    "agent_public_key": agent_public_key,           #required
    "principal_public_key": principal_public_key,   #required
    "resource_owner_id": vendor_public_key,         #required
    "exp": exp,                                     #required
    "iat": iat,                                         #optional
    "metadata": {                                       #optional
            "agent_name": agent_name,
            "principal_name": principal_name
    },
}

