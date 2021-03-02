import requests

url = 'http://fnilsson.com/getPk/'
data = {"search_value": "1"}

print("Post request to get PublicKey")
get_pk = requests.post(url, json=data)

pk = get_pk.text

print(get_pk)
print(pk)


url2 = 'http://fnilsson.com/getUserId/'
data2 = {"search_value": pk}

print("Post request to get ID with PublicKey")
get_id = requests.post(url2, json=data2)

print(get_id)
print(get_id.text)

url3 = 'http://fnilsson.com/verifyPk/'
data3 = {"search_value": pk}

print("Post request to verify PublicKey")
verify_pk = requests.post(url3, json=data3)

print(verify_pk)
print(verify_pk.text)

url4 = 'http://fnilsson.com/verifyUserId/'
data4 = {"search_value": get_id.text}

print("Post request to verify userId")
verify_id = requests.post(url4, json=data4)

print(verify_id)
print(verify_id.text)
