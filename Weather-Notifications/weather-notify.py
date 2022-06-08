#! /usr/local/bin/python3

import json
import requests
from twilio.rest import Client

'''
# Making sure requests works
x = requests.get('https://w3schools.com/python/demopage.htm')
print(x)
'''

with open('credentials.json') as data_file:
    secret = json.load(data_file)

baseURL = 'http://api.weatherstack.com'
endpoint = 'current'
query = 'Oakland'
access_key = secret['weather_key']
apiReq = '{}/{}?access_key={}&query={}'.format(baseURL,endpoint, access_key, query)
weather = requests.get(apiReq).text
print(weather)

weatherDict = json.loads(weather)

accountID = secret['twilio_sid']
authToken = secret['twilio_token']

client = Client(accountID, authToken)
txtMsg = 'The temperature is {}'.format(weatherDict['current']['temperature'])

message = client.messages.create(
    to = secret['to'],
    from_ = secret['from'],
    body = txtMsg
)

print(message)
