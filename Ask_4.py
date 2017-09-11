'''
Χρήστος Διαμαντής, Π16168
Εισαγωγή στην επιστήμη των υπολογιστών
Εργασία 8/2017
Python 3,6

Εργασία 4:
Χρησιμοποιείστε το API https://developers.teleport.org/api/getting_started/
προκειμένου να συγκρίνετε δύο πόλεις που θα εισάγει ο χρήστης.
Στο τέλος, το πρόγραμμα θα εμφανίζει το ποια πόλη υπερείχε της άλλης και
σε πόσους τομείς υπερείχε η κάθε μία.
'''

import requests # includes package requests not part of standard library:  http://docs.python-requests.org/en/master/
import json


def startRequest():
    city=input(' Πληκτρολογήστε τα στοιχεία της πόλης: ')
    city.strip()
    url='https://api.teleport.org/api/cities/?search='+city
    req=requests.get(url)
    reqJs=req.json()
    if reqJs['count']==0:
        print('  Η αναζήτηση δεν έδωσε αποτελέσματα. δοκιμάστε ξανά: ')
        city=startRequest()
    elif reqJs['count']>1:
        print('  Η αναζήτση επέστρεψε πολλαπλά αποτελέσματα. Δοκιμάστε κάποια από τις παρακάτω προτάσεις: ')
        for x in reqJs['_embedded']['city:search-results']:
            print('    '+x['matching_full_name'])
        city=startRequest()
    elif reqJs['count']==1:
        city=''
        city=reqJs['_embedded']['city:search-results'][0]['matching_full_name']
    return city

print('Αναζήτηση Πρώτης Πόλης... ')
firstC=startRequest()
print('\nΕπιλέξατε '+firstC)
print('\n\n')
print('Αναζήτηση Δεύτερης Πόλης... ')
secondC=startRequest()
print('\nΕπιλέξατε '+secondC)
print(firstC)
print(secondC)
