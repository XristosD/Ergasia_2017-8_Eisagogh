'''
Χρήστος Διαμαντής, Π16168
Εισαγωγή στην επιστήμη των υπολογιστών
Εργασία 8/2017
Python 3,6

Εργασία 3:
Γράψτε ένα πρόγραμμα το οποίο χρησιμοποιεί το REST interface του virustotal
https://www.virustotal.com/en/documentation/public-api/ ώστε να ανεβάσει ένα
αρχείο που επιλέγει ο χρήστης. Στην συνέχεια, ελέγχει ανά 3 δευτερόλεπτα αν
υπάρχει το αποτέλεσμα της ανάλυσης και εμφανίζει μία ταξινομημένη λίστα με το
ποια antivirus βρήκαν το αρχείο να περιέχει κάποιο κακόβουλο λογισμικό.
'''

import requests # includes package requests not part of standard library:  http://docs.python-requests.org/en/master/
import json
import time

path=''
def startFunc():
    try:
        path=input("Πληκτρολοηστε τη διαδρομή του αρχείου: ")
        file=open(path,'rb')
        return file
    except FileNotFoundError:
        print("Το αρχείο δε βρέθηκε δοκιμάστε ξανα.")
        startFunc()


file=startFunc()
url = 'https://www.virustotal.com/vtapi/v2/file/scan' 
apikey = '6b97b8967c8f5e43c29e711d58b0b3a0643e960155e03c0fdc4f6df637b00c78'

params = {'apikey': apikey}
files = {'file': ('a', file)}
response = requests.post('https://www.virustotal.com/vtapi/v2/file/scan', files=files, params=params)
json_response = response.json()
resource=json_response['scan_id']

def reqResponce():
    global resource
    params = {'apikey': apikey, 'resource': resource }
    headers = {
      "Accept-Encoding": "gzip, deflate",
      "User-Agent" : "gzip,  My Python requests library example client or username"
      }
    response = requests.get('https://www.virustotal.com/vtapi/v2/file/report',params=params, headers=headers)
    json_response = response.json()
    if(json_response['response_code']==1):
        infList=[]
        for x in json_response['scans']:
            if json_response['scans'][x]['detected'] == True :
                infList.append(x)
    else:
        time.sleep(3)
        reqResponce()

    return infList

infList = reqResponce()

if len(infList) == 0:
    print('Δεν βρέθηκε κακόβουλο λογισμικό')
else:
    for name in infList:
        print(name)
