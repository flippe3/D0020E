import jwt
import json
import datetime

def project(poas, agentID, princId):
    script = "<script>" \
             "\nconsole.log(document.getElementById('Items').innerHTML);"

    script+= "\nvar a = 0;\n"
    d = 0
    for poa in poas:
        poc = json.JSONDecoder().decode(poa)
        pid = poc["pid"]
        a = jwt.decode(poc["poa"], options={"verify_signature": False})
        script += "\nfunction clipboard"+str(d)+"(){\n" \
                  "var copyText = document.getElementById(\'a"+str(d)+"\');\n" \
                  "copyText.select();\n" \
                  "copyText.setSelectionRange(0, 99999); /* For mobile devices */\n" \
                  "document.execCommand(\'copy\');} "
        #script += "\ndocument.getElementById(\'Items\').innerHTML += \'<div> <textarea id=\"a"+str(d)+"\">"+poa+"</textarea> <a>" + json.dumps(
        #    a.get("metadata")) + " Iat:" + a.get('iat') + " Exp: " + a.get('exp') + \
        #          "</a> <button onClick=\"clipboard"+str(d)+"()\">Copy To clipbord</button>"
        script+=  "\ndocument.getElementById(\'Items\').innerHTML += \'<div>\'"
        script+=  "\ndocument.getElementById(\'Items\').innerHTML += \'<a>" + json.dumps(a.get("metadata")) + " Iat:" + datetime.datetime.fromtimestamp( a.get('iat') ).strftime("%Y-%m-%d-%H:%M") + " UTC TIME Exp: " + a.get('exp') + "  AgentID: "+str(agentID) + "  Principal ID: "+str(pid)+"</a>\'"
        script+=  "\ndocument.getElementById(\'Items\').innerHTML += \' <textarea hidden id=\"a"+str(d)+"\">"+ poa +"</textarea>\'"
        script+=  "\ndocument.getElementById(\'Items\').innerHTML += \'<button onClick=\"clipboard"+str(d)+"()\">Copy To clipbord</button>\'"
        d= d+1
    script += "\n</script>"

    print(script)
    return script
