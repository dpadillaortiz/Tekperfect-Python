


import json
import requests
from twilio.rest import Client

with open('secrets.json', 'r') as j:
   secrets = json.load(j)
   
account_sid = secrets['account_sid']
auth_token = secrets['auth_token']
phone = secrets['phone']
weather_api_token = secrets['weather_api']

client = Client(account_sid, auth_token)
body = 'Hello World'
from_ = phone
to = ''
# message = client.messages.create(body=body, from_=from_, to=to)

weather_url = 'http://api.weatherstack.com/current'
access_key = weather_api_token
query = 'Oakland'
api_request = f'{weather_url}?access_key={access_key}&query={query}'
r = requests.get(api_request).text

api_response = json.loads(r)

api_keys = api_response.keys()

temp = api_response['current']['temperature']

msg = f'The temperature for today is {temp}'

message = client.messages.create(body=msg, from_=from_, to=to)

