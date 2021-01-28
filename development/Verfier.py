import jwt
import datetime
import Constants
import Register



# vet inte om vi kommer vilja ha en egen klass men gör en för tillfället
class Verifier:

        def verify_poa(poa):
                try:
                        sender_public_key = poa["sender_public_key"]
                        receiver_public_key = poa["receiver_public_key"]
                        #return Verifier.verify_payload( decrypt_payload( poa["payload"]))
                
                        return Verifier.verify_payload( sender_public_key, receiver_public_key, jwt.decode( poa["payload"], Constants.principal_public_key, algorithms=["RS256"])) 
                except:
                        return False
        
        
        #def decrypt_payload(sender_public_key, receiver_public_key, encrypted_payload):
        #       return jwt.decode( jwt.decode( encrypted_payload, sender_public_key, algorithms=["RS256"]), receiver_public_key, algorithms=["RS256"])



        def verify_payload(sender_public_key, receiver_public_key, payload):

                try:
                        exp = payload["exp"]
                        Agent_MAC_Address = payload["Agent_MAC_Address"]
                        Agent_Name = payload["Agent_Name"]
                        Agent_Public_key = payload["Agent_Public_key"]
                        payload["Message"]
                        Mining_Station_ID = payload["Mining_Station_ID"]
                        Principal_Name = payload["Principal_Name"]
                        Principal_Public_Key = payload["Principal_Public_Key"]
                                                        #Valid_from = datetime.datetime.strptime( payload["Valid_from"], '%Y-%m-%d %H:%M:%S')
                                                        #Valid_to = datetime.datetime.strptime( payload["Valid_to"], '%Y-%m-%d %H:%M:%S')
                        payload["id"]
                        
                                                        #now = datetime.datetime.now()


                        if(Agent_Public_key != sender_public_key):
                                return False
                        if(Principal_Public_Key != receiver_public_key):
                                return False
                                                        #if(Valid_from > now or Valid_to < now):        ~Automatically checked when payload gets decoded~
                                                        #        return False
        

                        if( Register.key[Agent_Public_key]["MAC_Address"] != Agent_MAC_Address):
                                return False
                        if( Register.key[Agent_Public_key]["Agent_Name"] != Agent_Name):
                                return False
                        
                        if( Register.key[Principal_Public_Key]["Principal_Name"] != Principal_Name):
                                return False

                        
                except:
                        return False

                return True




















#                                         ~TESTING~

expires = datetime.datetime.utcnow() + datetime.timedelta(seconds=180)
# I didn't seem to love being double encrypted, but it's probably doable. 
payload = jwt.encode( { "exp": expires, "Agent_MAC_Address": "00:0a:95:9d:68:16", "Agent_Name": "Truck device", "Agent_Public_key": Constants.agent_public_key, "Message": "sadwd", "Mining_Station_ID": "121", "Principal_Name": "Entrepreneur", "Principal_Public_Key": Constants.principal_public_key, "Valid_from": "2020-07-15 09:48:31", "Valid_to": "2021-07-31 18:00:00", "id": "3"}, Constants.principal_private_key, algorithm="RS256")
poa = {"sender_public_key": Constants.agent_public_key, "receiver_public_key": Constants.principal_public_key, "payload": payload}


print(Verifier.verify_poa(poa))

