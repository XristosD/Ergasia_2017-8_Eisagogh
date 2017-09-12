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
import re


def startRequest():
    city=input('\n Πληκτρολογήστε τα στοιχεία της πόλης: ')
    city.strip()
    city=re.sub('\(.*\)','',city)
    url='https://api.teleport.org/api/cities/?search='+city+'&embed=city:search-results/city:item/city:urban_area/ua:scores'
    req=requests.get(url)
    reqJs=req.json()
    if reqJs['count']==0:
        print('  Η αναζήτηση δεν έδωσε αποτελέσματα. δοκιμάστε ξανά: ')
        [city,retScore]=startRequest()
    elif reqJs['count']>1:
        print('  Η αναζήτση επέστρεψε πολλαπλά αποτελέσματα. Δοκιμάστε κάποια από τις παρακάτω προτάσεις: ')
        for x in reqJs['_embedded']['city:search-results']:
            results=x['matching_full_name']
            results=re.sub('\(.*\)','',results)
            print('    '+results)
        [city,retScore]=startRequest()
    elif reqJs['count']==1:
        city=''
        city=reqJs['_embedded']['city:search-results'][0]['matching_full_name']
        city=re.sub('\(.*\)','',city)
        try:
            retScore = reqJs['_embedded']['city:search-results'][0]['_embedded']['city:item']['_embedded']['city:urban_area']['_embedded']['ua:scores']
                
        except KeyError:
            print('    Η πόλη δεν διαθετει στοιχεια προς σύγκριση. Δοκιμαστε ξανα... ')
            [city,retScore]=startRequest()
    return [city,retScore]

print('Αναζήτηση Πρώτης Πόλης... ')
firstC=startRequest()
print('\n\n')
print('Αναζήτηση Δεύτερης Πόλης... ')
secondC=startRequest()
print('\n\n')

finalResult=''
score=0
for x,y in zip(firstC[1]['categories'],secondC[1]['categories']):
    result=''
    if x['score_out_of_10']>y['score_out_of_10']:
        result=result+'Η πόλη '+firstC[0]+' υπερέχει της πόλης '+secondC[0]+' στον τομεα '+x['name']+'.\n'
        score+=1
    elif x['score_out_of_10']<y['score_out_of_10']:
        result=result+'Η πόλη '+secondC[0]+' υπερέχει της πόλης '+firstC[0]+' στον τομεα '+x['name']+'.\n'
        score-=1
    elif x['score_out_of_10']==y['score_out_of_10']:
        result=result+'Η πόλεις ισοβαθμούν στον τομεα '+x['name']+'.\n'
    finalResult=finalResult+result

print(finalResult)
print('\n')

if score>0:
    print('Η πρώτη πόλη υπερτερεί σε '+str(abs(score))+' τομείς.')
elif score<0:
    print('Η δεύτερη πόλη υπερτερεί σε '+str(abs(score))+' τομείς.')
elif score==0:
    print('Οι πόλεις συγκέντρωσαν το ίδιο score.')
	
