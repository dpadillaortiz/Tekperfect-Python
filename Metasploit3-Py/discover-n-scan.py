#! /usr/bin/python3


import subprocess as sp

DISCOVER_FILE = 'discover-networks.txt'
NMAP_FILE = 'nmap-recon.txt'

'''
    1. Need to know my IP address
        a. Use `ip address` to find out
            - write to a file
            - read and printed from a file
    2. Discover networks
        a. Ask for target ip range
        b. Use `netdiscover` with target ip range
            - needs to written to a file
            - file needs to be read and printed out
    3. Run nmap scan on an ip from discovered above
        a. Ask for ip tager
        b. use `nmap` on ip target 
            - write to a file
            - read from file and print it
'''

def cmdOutputToFile(command, file):
    with open(file, 'w') as data:
        sp.run(command, stdout=data, text=True)

def printFile(file):
    with open(file, 'r') as data:
        display = data.read()
    print(display)


def ipAddr():
    FILE = 'ip-address.txt'
    CMD = ['ip', 'address']
    print('Grabbing IP information...')
    cmdOutputToFile(CMD, FILE)
    printFile(FILE)
    
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

ipAddr()
