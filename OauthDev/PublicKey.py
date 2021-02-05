import development.Constants as c

def get_public_key(id_of_actor):
    id = id_of_actor.toLowerCase()
    if id is "agent":
        return c.agent_public_key
    elif id is "principal":
        return c.principal_public_key
    elif id is "vendor":
        return c.vendor_public_key

