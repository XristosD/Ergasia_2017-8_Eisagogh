'''
Χρήστος Διαμαντής, Π16168
Εισαγωγή στην επιστήμη των υπολογιστών
Εργασία 8/2017
Python 3,6
Εργασία 6:
Χρησιμοποιείστε το API https://api.chucknorris.io/ για να πάρετε ένα τυχαίο κείμενο. 
Στην συνέχεια χωρίστε το κείμενο σε λέξεις και για κάθε λέξη που είναι μεγαλύτερη
από 2 χαρακτήρες προσθέτετε σαν αριθμούς τον πρώτο και τον τελευταίο χαρακτήρα και επιστρέφετε για το 
υπόλοιπο με το 3. Αν η λέξη έχει μήκος 1, επιστρέφετε το -1 . Στο τέλος εκτυπώνεται στην οθόνη μια 
ακολουθία αριθμών.
'''

import requests # includes package requests not part of standard library:  http://docs.python-requests.org/en/master/
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
 
