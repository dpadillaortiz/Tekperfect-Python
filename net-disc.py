#! /usr/bin/python3


import subprocess as sp

file = 'test.txt'

ipRange = input('Enter IP range: ')

print('Discovering networks...')

with open(file,'w') as data:
    sp.run(['sudo', 'netdiscover', '-r', ipRange, '-P'], stdout=data, text=True)


ipList = []
with open(file,'r') as data:
    display = data.read()
    
print(display)

with open(file, 'r') as data:
    lines = data.readlines()
    for i in range(3,len(lines)-2):
        print(lines[i].split()[0])
        ipList.append(lines[i].split()[0])

print(ipList)

ipTarget = input('Enter target IP for nmap: ')

nmap_text = 'nmap-text.txt'

print('Running nmap scan...')

with open(nmap_text,'w') as data:
    sp.run(['sudo', 'nmap', '-sV', ipTarget, '-O'], stdout=data, text=True)

with open(nmap_text,'r') as data:
    display = data.read()

print(display)























