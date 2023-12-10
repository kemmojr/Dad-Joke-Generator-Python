from urllib import request
import json

def CmonDad():
    try:    
        url = 'https://icanhazdadjoke.com/'
        req = request.Request(url, headers = {
            'Accept': 'application/json',
            'User-Agent': 'My Library (https://github.com/kemmojr/Dad-Joke-generator-Python)'
        })
        content = request.urlopen(req).read().decode('utf-8')
        data = json.loads(content)
        joke = data['joke']
        return joke
    except:
        return "Error: it seems we're out of dad jokes"

while (True):
    print('Dad Joke generator\n')
    print('\tHello There\t\n')
    print('\tWould you care for a dad joke?\t\n')
    input('\tok dad (press enter)\t\n')
    print(f'\t{CmonDad()}\n')
    input('\t*groan* (press enter)\t\n')
    
