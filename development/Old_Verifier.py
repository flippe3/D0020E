import jwt
import datetime
import Constants as Const
import Register



# vet inte om vi kommer vilja ha en egen klass men gör en för tillfället
class Verifier:

        def verify_poa(payload):
                try:
                        agent_public_key        = payload["agent_public_key"]
                        principal_public_key    = payload["principal_public_key"]
                        resource_owner_id       = payload["resource_owner_id"]
                        exp                     = payload["exp"]    

                        return Verifier.verify_payload(agent_public_key, principal_public_key, resource_owner_id, exp)      
                except KeyError:
                        print("Payload is missing mandatory data")
                        return False
        
        
        def verify_payload(agent_public_key, principal_public_key, resource_owner_id, exp):

                # Check keys
                if(agent_public_key     != Const.agent_public_key):
                        print("Incorrect agent_public_key")
                        return False
                if(principal_public_key != Const.principal_public_key):
                        print("Incorrect principal_public_key")
                        return False
                if(resource_owner_id    != Const.vendor_public_key):
                        print("Incorrect vendor_public_key")
                        return False

                if(exp < datetime.datetime.utcnow().timestamp()):   # I think this is automatically checked when POA gets decoded 
                        print("POA has expired")
                        return False

                return True
