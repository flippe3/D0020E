ip = "localhost"
agent_port = 4573
principal_port = 4573
vendor_port = 4574

import jwt

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

request_poa_body = {
    "response_type": "token",
    "client_id": "agent123",
    "public_key": agent_public_key
}

valid_poa = {
    "Agent_MAC_Address": "00:0a:95:9d:68:16",
    "Agent_Name": "Truck device",
    "Agent_Public_Key": agent_public_key,
    "Message": "This PoA authorizes Agent (Truck device) to make decisions on behalf of the Principal and valid for a short period",
    "Mining_Station_ID": "121",
    "Principal_Name": "Entrepreneur",
    "Prinicpal_Public_Key": principal_public_key,
    "Valid_from": "2021-01-01 12:00:00",
    "Valid_to": "2021-12-30 12:00:00",
    "id": "3"
}

invalid_poa = {
    "Agent_MAC_Address": "00:0a:95:9d:68:16",
    "Agent_Name": "Truck device",
    "Agent_Public_Key": agent_public_key,
    "Message": "This PoA authorizes Agent (Truck device) to make decisions on behalf of the Principal and valid for a short period",
    "Mining_Station_ID": "121",
    "Principal_Name": "Entrepreneur",
    "Prinicpal_Public_Key": principal_public_key,
    "Valid_from": "2020-01-01 12:00:00",
    "Valid_to": "2020-12-30 12:00:00",
    "id": "3"
}

valid_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJBZ2VudF9NQUNfQWRkcmVzcyI6IjAwOjBhOjk1OjlkOjY4OjE2IiwiQWdlbnRfTmFtZSI6IlRydWNrIGRldmljZSIsIkFnZW50X1B1YmxpY19LZXkiOiItLS0tLUJFR0lOIFBVQkxJQyBLRVktLS0tLVxuTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUFubTRFb2IwV3pUUWF4bjJkTGJralxuVlFSUXB5cEp0ZGY3WEk0bHR1d2IzZmZQUVhxN2swcy9VTHBYR1ZwdzVtYkYzQXVHSUU1Kzc3SGlDQjVvN1FRSFxua1Y5YW5EanVFS09PR2Z4SlRJSS96em9jZVJlV09IV24rSnRURGxMdWN3dGZrNjFDeUpvRGFSNjd6VS9UVEJGV1xuTnNweW94L1JOTUNnT2NUSUFzZkxZaityTXNxNnpueVBpQjVLV29aSUM5aEEwMEVQVERnckRDRGJ1Yk1wZFZVbVxuNytERE1WcGZoeXVlUjk0VzN3eDB0RjFNTmFxc1R1V2tXWGNiZXYyZ3diNUU4VEJ5bUIwbENnTkIzUDZLUzhSUlxuTFlhdDVUVkRLam9tY3JveGQrZ0tYOXlUMzFlSmMrRmhqeEhjQnlGUThBam5sVkEydEUzNXB5Zk8yWVB2MFYwcFxuS3dJREFRQUJcbi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLSIsIk1lc3NhZ2UiOiJUaGlzIFBvQSBhdXRob3JpemVzIEFnZW50IChUcnVjayBkZXZpY2UpIHRvIG1ha2UgZGVjaXNpb25zIG9uIGJlaGFsZiBvZiB0aGUgUHJpbmNpcGFsIGFuZCB2YWxpZCBmb3IgYSBzaG9ydCBwZXJpb2QiLCJNaW5pbmdfU3RhdGlvbl9JRCI6IjEyMSIsIlByaW5jaXBhbF9OYW1lIjoiRW50cmVwcmVuZXVyIiwiUHJpbmljcGFsX1B1YmxpY19LZXkiOiItLS0tLUJFR0lOIFBVQkxJQyBLRVktLS0tLVxuTUlJQklUQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FRNEFNSUlCQ1FLQ0FRQm1vdGs5SlNiL1gveFpXWXRZdjFUaVxuenNudHdnMGJFc0pPVlhkdldDQS82dm1zbW9DVlM2VlFkZTFSWGRWNGkvRUFTc3NrNHFUelNQQ1p2VVoyK0NYU1xuM3ZldGkxOFdYanBGd28vR2pyUTgxbS9jM29sZThHaFExVWM3VWZnOTl1R3FiYUV1OVkvTUVRMVRlV0Myamp5N1xuVjNWR1NtZzlDdUdlRUNrNUNFT3IyM3FkQXZ3VUd3Y0pzeWZUaWRnd2pmUTVxU0NyYll3TlVTcy9SL1hOR3l5WFxueHU3bGw0QUs0N2lGWEcwdzExcEZnQVZuR0V3QXpybWVpK0pua05GaXNqbnJLYzliSTdNSWZRUVBUYVY4ZDBEbVxudWFRTVdaSzdhYWpWOVZNeDVhNUt3VGgrVkQzcEEvVVMzRkFkRlhoL2xjeFBmWHNyTXhmVmdPSGhwTWNkRThsL1xuQWdNQkFBRT1cbi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLSIsIlZhbGlkX2Zyb20iOiIyMDIxLTAxLTAxIDEyOjAwOjAwIiwiVmFsaWRfdG8iOiIyMDIxLTEyLTMwIDEyOjAwOjAwIiwiaWQiOiIzIn0.QJaYenhoP3cLKNLy2FSsI9-FTjkzhPtnEOs9DxH2EznOH-tppZn9kBEkOOgtvw-IcWyoXZrr5gyDybTdneLzj2s6m7vVuiBv7eiFE-S1W1L2ObvQixFbkfNrH4cHXxxvf10zY7n5ZDUZyrbJiZPhoSGzXNuBJ_9DFe3o4wSDkEfJxPrUm5SJwamTv1SbzIE_KGkTwtdiTMK4-xnMkI0FmBGzTadzGF8pxJGFPK_oKKzrQDdNn9ZXIltgOP-W52rdPB0RjA8vuMjDj2_rTw8OTX-HQjPsYnmEOqLQjh7av0O56AoVatGrfWYarcLEZLbr5B2XsogfvSh6UeXvnlTGEw"
invalid_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJBZ2VudF9NQUNfQWRkcmVzcyI6IjAwOjBhOjk1OjlkOjY4OjE2IiwiQWdlbnRfTmFtZSI6IlRydWNrIGRldmljZSIsIkFnZW50X1B1YmxpY19LZXkiOiItLS0tLUJFR0lOIFBVQkxJQyBLRVktLS0tLVxuTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUFubTRFb2IwV3pUUWF4bjJkTGJralxuVlFSUXB5cEp0ZGY3WEk0bHR1d2IzZmZQUVhxN2swcy9VTHBYR1ZwdzVtYkYzQXVHSUU1Kzc3SGlDQjVvN1FRSFxua1Y5YW5EanVFS09PR2Z4SlRJSS96em9jZVJlV09IV24rSnRURGxMdWN3dGZrNjFDeUpvRGFSNjd6VS9UVEJGV1xuTnNweW94L1JOTUNnT2NUSUFzZkxZaityTXNxNnpueVBpQjVLV29aSUM5aEEwMEVQVERnckRDRGJ1Yk1wZFZVbVxuNytERE1WcGZoeXVlUjk0VzN3eDB0RjFNTmFxc1R1V2tXWGNiZXYyZ3diNUU4VEJ5bUIwbENnTkIzUDZLUzhSUlxuTFlhdDVUVkRLam9tY3JveGQrZ0tYOXlUMzFlSmMrRmhqeEhjQnlGUThBam5sVkEydEUzNXB5Zk8yWVB2MFYwcFxuS3dJREFRQUJcbi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLSIsIk1lc3NhZ2UiOiJUaGlzIFBvQSBhdXRob3JpemVzIEFnZW50IChUcnVjayBkZXZpY2UpIHRvIG1ha2UgZGVjaXNpb25zIG9uIGJlaGFsZiBvZiB0aGUgUHJpbmNpcGFsIGFuZCB2YWxpZCBmb3IgYSBzaG9ydCBwZXJpb2QiLCJNaW5pbmdfU3RhdGlvbl9JRCI6IjEyMSIsIlByaW5jaXBhbF9OYW1lIjoiRW50cmVwcmVuZXVyIiwiUHJpbmljcGFsX1B1YmxpY19LZXkiOiItLS0tLUJFR0lOIFBVQkxJQyBLRVktLS0tLVxuTUlJQklUQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FRNEFNSUlCQ1FLQ0FRQm1vdGs5SlNiL1gveFpXWXRZdjFUaVxuenNudHdnMGJFc0pPVlhkdldDQS82dm1zbW9DVlM2VlFkZTFSWGRWNGkvRUFTc3NrNHFUelNQQ1p2VVoyK0NYU1xuM3ZldGkxOFdYanBGd28vR2pyUTgxbS9jM29sZThHaFExVWM3VWZnOTl1R3FiYUV1OVkvTUVRMVRlV0Myamp5N1xuVjNWR1NtZzlDdUdlRUNrNUNFT3IyM3FkQXZ3VUd3Y0pzeWZUaWRnd2pmUTVxU0NyYll3TlVTcy9SL1hOR3l5WFxueHU3bGw0QUs0N2lGWEcwdzExcEZnQVZuR0V3QXpybWVpK0pua05GaXNqbnJLYzliSTdNSWZRUVBUYVY4ZDBEbVxudWFRTVdaSzdhYWpWOVZNeDVhNUt3VGgrVkQzcEEvVVMzRkFkRlhoL2xjeFBmWHNyTXhmVmdPSGhwTWNkRThsL1xuQWdNQkFBRT1cbi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLSIsIlZhbGlkX2Zyb20iOiIyMDIwLTAxLTAxIDEyOjAwOjAwIiwiVmFsaWRfdG8iOiIyMDIwLTEyLTMwIDEyOjAwOjAwIiwiaWQiOiIzIn0.GUnVFL-N4ssh3DUA4vdlrk135Jp14EZQBlfLjJBewm53bvUc0sfv4h6jQuPjYPGV9gxEPPRj-07JPgWCqTS6J8PDRdvetPs0Lc5_NOb65W5uNSvyIuEtMfNGr86UsoYSG8-aX_hAX4Qs3JvEk521qeTl6Gch6ma2KH4fU22MbOqukEvN1FEsgNeWGvC8hJPKaUBoO7TUpVXBNMKIjab5pcufGKvlZd5A6arHptadwcFWNUzEUKiAn1JtgYlseorPfej6HWPbAH9uWYlrWtMK3cFhpiwnqmg4p5DFkF8wozzCnUoFeO5as3hZ6g65AdhrxAuQJB2VJ6KgOrARs9o_Tw"
request_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJyZXNwb25zZV90eXBlIjoidG9rZW4iLCJjbGllbnRfaWQiOiJhZ2VudDEyMyIsInB1YmxpY19rZXkiOiItLS0tLUJFR0lOIFBVQkxJQyBLRVktLS0tLVxuTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUFubTRFb2IwV3pUUWF4bjJkTGJralxuVlFSUXB5cEp0ZGY3WEk0bHR1d2IzZmZQUVhxN2swcy9VTHBYR1ZwdzVtYkYzQXVHSUU1Kzc3SGlDQjVvN1FRSFxua1Y5YW5EanVFS09PR2Z4SlRJSS96em9jZVJlV09IV24rSnRURGxMdWN3dGZrNjFDeUpvRGFSNjd6VS9UVEJGV1xuTnNweW94L1JOTUNnT2NUSUFzZkxZaityTXNxNnpueVBpQjVLV29aSUM5aEEwMEVQVERnckRDRGJ1Yk1wZFZVbVxuNytERE1WcGZoeXVlUjk0VzN3eDB0RjFNTmFxc1R1V2tXWGNiZXYyZ3diNUU4VEJ5bUIwbENnTkIzUDZLUzhSUlxuTFlhdDVUVkRLam9tY3JveGQrZ0tYOXlUMzFlSmMrRmhqeEhjQnlGUThBam5sVkEydEUzNXB5Zk8yWVB2MFYwcFxuS3dJREFRQUJcbi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLSJ9.SG-UzZHh_JrBuzhpfz10u_JJ6RlUPTvW_KSxWB28TaXk8RI5KwpxCO05EP4VKFYJ5SMIWuAU2uqEV5R3Uxj9yARvnP4CcPLKpSjQohLGmFWjlcbAdt43Mc6W3dILEKOMkXRNmusfiyp5gLQ4BQWHoCGuxRHfARwXaKHEvmvZOkB5fxdrDi4jWZ5LJdfDo4XiCQZbI3l2ekzCSf6Xa1NRmKDTeJKx2K_Do8G8jmF6ut4Oe1Y7ScxBH0lz1C1xFwDf7fvdSOujj2Nj-12an1p8YpeRFICacXQJuUJDiRo_54a6rr91JNrqQYDZAPgilGjwWFZ586Y64h1G4-si0ZVz8g"

