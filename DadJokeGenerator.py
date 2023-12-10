from urllib import request
import json

url = 'https://icanhazdadjoke.com/'
req = request.Request(url, headers = {
    'Accept': 'application/json',
    'User-Agent': 'My Library (https://github.com/kemmojr/Dad-Joke-generator-Python)'
})
content = request.urlopen(req).read().decode('utf-8')
data = json.loads(content)
print(data['joke'])
