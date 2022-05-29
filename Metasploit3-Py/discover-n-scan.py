#! /usr/bin/python3


import subprocess as sp

DISCOVER_FILE = 'discover-networks.txt'
NMAP_FILE = 'nmap-recon.txt'

# Get ip addres
# Ask for ip range to scan
# Run netdiscover
# Run nmap scan 

def getIpAddr():
    print('Grabbing IP information...')
    sp.run(['ip', 'address'], stdout=sp.PIPE, text=True)
    # Task: return the ip address

def discoverMyNet():
    print('Preparing to discover...')
    ipRange = input('Enter IP range: ')
    print('Discovering networks...')
 

def writeToFile(file, ip_range):
    with open(file, 'w') as data:
        sp.run(['sudo', 'netdiscover', '-r', ip_range, '-P'], stdout=data, text=True)

def readFromFile(file):
    with open(file, 'r') as data:
        display = data.read()
    return display

getIpAddr()
