import urllib2
import json
import random
import time

url = 'http://10.126.6.85:5005/webhooks/rest/webhook/'
text = "repeat"

data = '{"sender":"nao", "message":"' + text + '"}'

req = urllib2.Request(url, data=data)
f = urllib2.urlopen(req)
class Response:
    pass
response = Response()
response.code = f.getcode()
response.body = f.read()
print(response.body)
r = json.loads(response.body)[0]['text'].encode("UTF-8")
print(r)
