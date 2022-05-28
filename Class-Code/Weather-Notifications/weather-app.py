#! /usr/local/bin/python3

import json
import requests

'''
# Making sure requests works
x = requests.get('https://w3schools.com/python/demopage.htm')
print(x)
'''

with open('ACCESS-KEY.json') as data_file:
    secret = json.load(data_file)

baseURL = 'http://api.weatherstack.com'
endpoint = 'current'
query = 'Oakland'
access_key = secret['key']
apiReq = '{}/{}?access_key={}&query={}'.format(baseURL,endpoint, access_key, query)
weather = requests.get(apiReq)
print(weather.json())

