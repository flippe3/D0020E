from datetime import datetime
import jwt
import json

UTC = True
LOCAL = False

def get_current_date(utc=False):
    if utc:
        return datetime.utcnow().strftime(
            "%Y-%m-%d %H:%M:%S")  # <--- Visst ville vi använda utcnow() istället för now()?
    else:
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_current_time(utc=False):
    if utc:
        return datetime.utcnow().timestamp()
    else:
        return datetime.now().timestamp()


def generate_jwt(payload, private_key):
    return jwt.encode(payload, private_key, algorithm="RS256")


def decode_jwt(token, public_key):
    return jwt.decode(token, public_key, algorithms=["RS256"])


def verify_poa_expiration(poa_payload):
    now = get_current_time(True)
    if now < poa_payload.exp:
        return True
    else:
        return False

def input_form():
    print("This is a form to input the metadata for the PoA.")
    name = input("Full name: ")
    app = input("Application type: ")
    principal_name = input("Principal name: ")
    mac = input("MAC ID: ")
    # Choose between all principals/vendors
    metadata = {"Agent Name": name,
                "Application Type": app,
                "Principal Name": principal_name,
                "MAC Address": mac
                }
    return json.JSONEncoder().encode(metadata)
