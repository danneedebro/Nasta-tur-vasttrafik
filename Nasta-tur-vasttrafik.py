import requests
import base64
from datetime import datetime

# USER INPUT
KEY = 'fYzsg6smhs3eysZLUGsTBrFl2cQa'
SECRET = '0es63wTfFJAsteDgl6s7Khskb2Ia'
STOP = 'svingeln'

# Step 1: Get Access token
parameters = {'format': 'json', 'grant_type': 'client_credentials'}
url = 'https://api.vasttrafik.se/token'
head = {'Authorization': 'Basic ' + base64.b64encode((KEY + ':' + SECRET).encode()).decode(),
        'Content-Type': 'application/x-www-form-urlencoded'}

r = requests.post(url,headers = head, params=parameters)

tmp = r.json()

ACCESS_TOKEN = tmp['access_token']
print("Access token är: ",ACCESS_TOKEN)


# Step 2: Get stop id from stop string using api method 'location.name'
url = 'https://api.vasttrafik.se/bin/rest.exe/v2/location.name'
parameters = {'format': 'json', 'input': STOP}
head = {'Authorization': 'Bearer ' + ACCESS_TOKEN}
#print(url)
r = requests.get(url,headers=head, params=parameters)

tmp = r.json()

STOP_ID = tmp['LocationList']['StopLocation'][0]['id']
print("\nStopID för hållplats '", STOP, "' är ",STOP_ID)


# Step 3: Get list of depatures using api method 'departureBoard'
now = datetime.now()
url = 'https://api.vasttrafik.se/bin/rest.exe/v2/departureBoard'
parameters = {'format': 'json', 'id': STOP_ID, 'date':now.strftime("%Y-%m-%d"), 'time':now.strftime("%H:%M")}
head = {'Authorization': 'Bearer ' + ACCESS_TOKEN}

r = requests.get(url,headers = head, params=parameters)

tmp = r.json()

print("\nAvgångar från " + STOP)
for i in range(0,len(tmp['DepartureBoard']['Departure'])):
    currItem = tmp['DepartureBoard']['Departure'][i]
    serverDateTime = datetime.strptime(tmp['DepartureBoard']['serverdate'] + ' ' + tmp['DepartureBoard']['servertime'],"%Y-%m-%d %H:%M")
    if 'rtTime' in currItem:
        departInSeconds = datetime.strptime(currItem['rtDate'] + " " + currItem['rtTime'], "%Y-%m-%d %H:%M") - serverDateTime
        #print(hmp)
        print("Linje ",currItem['sname']," mot ",currItem['direction']," avgår kl ",currItem['rtTime'],' (real), om ',round(departInSeconds.seconds/60,0), ' minuter')
    else:
        departInSeconds = datetime.strptime(currItem['date'] + " " + currItem['time'],"%Y-%m-%d %H:%M") - serverDateTime
        print("Linje ", currItem['sname'], " avgår kl ", currItem['time'],' (real), om ',round(departInSeconds.seconds/60,0), ' minuter')


