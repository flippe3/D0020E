import development.Constants as c

def get_public_key(id_of_actor):
    id = id_of_actor
    if id == "agent":
        return c.agent_public_key
    elif id == "principal":
        return c.principal_public_key
    elif id == "vendor":
        return c.vendor_public_key

def get_user_id(public_key):
    #gets id related to specific key
    return True

def verify_public_key(id_of_actor):
    #gets a response from server saying if public key is related to id
    return True

def verify_id(public_key):
    #gets a response from server saying if id is related to public key
    return True

def connect_to_key_registry():
    #will be used depending on the server implementation
    #if it's http it won't be used
    return True