import development.Constants as c

def get_public_key(id_of_actor):
    id = id_of_actor
    if id == "agent":
        return c.agent_public_key
    elif id == "principal":
        return c.principal_public_key
    elif id == "vendor":
        return c.vendor_public_key

