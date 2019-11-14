import urllib.request
import urllib.parse
 
def sendSMS(numbers, message):
    apikey='api key-VxL+paM+fvA-LiPZ7Olfis96j3oEq4QqJqhaRhL5h'
    sender='TXTLCL'
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

#sender_name = getGroups('EsIjzzHxEDQ-tdk8phvleAwNHQYM7huAFGgOQEvd2c')
#print(sender_name)
