

import requests
import json

seq=''
url='https://api.chucknorris.io/jokes/random'
req=requests.get(url)
reqJs=req.json()
joke=reqJs['value']
print(joke)
joke=joke.split()
joke[-1]=joke[-1].strip('.')
for word in joke:
    if len(word)>1:
      seq=seq+ str((ord(word[0])+ord(word[-1]))%3) +', '
    else:
        seq =seq + '-1, '

print('Ακολουθία: '+seq)
 
