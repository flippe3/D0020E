from datetime import datetime
import jwt


def get_now():
    return datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")  # <--- Visst ville vi använda utcnow() istället för now()?


def generate_jwt(payload, private_key):
    return jwt.encode(payload, private_key, algorithm="RS256")


def decode_jwt(token, public_key):
    return jwt.decode(token, public_key, algorithms=["RS256"])
