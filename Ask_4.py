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

url='https://api.teleport.org/api/cities/?search=San%20Francisco'
req=requests.get(url)
reqJs=req.json()


print(reqJs['count'])
