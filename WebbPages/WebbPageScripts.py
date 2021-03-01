import jwt
import json
def project(poas):
    script =  "<script>" \
           "\nconsole.log(document.getElementById('Items').innerHTML);"

    for poa in poas:
        #a = jwt.decode(poa[0],poa[1],algorithms=["RS256"])
        a = jwt.decode(poa, options={"verify_signature": False})
        script += "\ndocument.getElementById('Items').innerHTML = '<div>"+json.dumps(a.get("metadata")) + " </div>'"

    script +="\n</script>"

    return script