import jwt
import datetime


# vet inte om vi kommer vilja ha en egen klass men gör en för tillfället
class Verifier:

	def verify_poa(poa):
		try:
			sender_public_key = poa["sender_public_key"]
			receiver_public_key = poa["receiver_public_key"]
			#return Verifier.verify_payload( decrypt_payload( poa["payload"]))
			
			return Verifier.verify_payload( sender_public_key, receiver_public_key, poa["payload"]) 
		except:
			return False
	
	
	def decrypt_payload(sender_public_key, receiver_public_key, encrypted_payload):
		return jwt.decode( jwt.decode( encrypted_payload, sender_public_key, algorithms=["RS256"]), receiver_public_key, algorithms=["RS256"])
		
		
	
	def verify_payload(sender_public_key, receiver_public_key, payload):
		try:
			payload["Agent_MAC_Address"]
			payload["Agent_Name"]
			Agent_Public_key = payload["Agent_Public_key"]
			payload["Message"]
			payload["Mining_Station_ID"]
			payload["Principal_Name"]
			Principal_Public_Key = payload["Principal_Public_Key"]
			Valid_from = datetime.datetime.strptime( payload["Valid_from"], '%Y-%m-%d %H:%M:%S') 
			Valid_to = datetime.datetime.strptime( payload["Valid_to"], '%Y-%m-%d %H:%M:%S')
			payload["id"]
			
			now = datetime.datetime.now()
			
			if(Agent_Public_key != sender_public_key):
				return False
			if(Principal_Public_Key != receiver_public_key):
				return False
			if(Valid_from > now or Valid_to < now):
				return False

		except:
			return False
			
		return True
	
	
	
	
# Testing
poa = {"sender_public_key": "truckdevice123", "receiver_public_key": "entrepreneur123", "payload": {"Agent_MAC_Address": "00:0a:95:9d:68:16", "Agent_Name": "Truck device", "Agent_Public_key": "truckdevice123", "Message": "sadwd", "Mining_Station_ID": "121", "Principal_Name": "Entrepreneur", "Principal_Public_Key": "entrepreneur123", "Valid_from": "2020-07-15 09:48:31", "Valid_to": "2021-07-31 18:00:00", "id": "3"}}
print(Verifier.verify_poa(poa))


