import urllib.request
import urllib.parse
 
def sendSMS(apikey, numbers, sender, message):
    data =  urllib.parse.urlencode({'apikey': apikey, 'numbers': numbers,
        'message' : message, 'sender': sender})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/send/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)


def getGroups(apikey):
    data =  urllib.parse.urlencode({'apikey': apikey})
    data = data.encode('utf-8')
    request = urllib.request.Request("https://api.textlocal.in/get_sender_names/?")
    f = urllib.request.urlopen(request, data)
    fr = f.read()
    return(fr)

resp =  sendSMS('V+CnFVrIf/E-r7OVG45o2OH4wsYhyrTouivYHLa6ts', '916282516951', 'TXTLCL', 'This is your message')
print(resp)