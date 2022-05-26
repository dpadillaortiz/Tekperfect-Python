#! /usr/bin/python3

from pymetasploit3.msfrpc import MsfRpcClient

print('\nMake sure MSF is running on another tab.\n')
print('In termial type:\n\n msfconsole \n load msgrpc [pass=yourpasswd] \n')

print('Take note of MSGRPC Password.')
PASSWORD = input('Enter your password: ')

client = MsfRpcClient(PASSWORD, port=55552, ssl=False)

print(client.modules.exploits)
