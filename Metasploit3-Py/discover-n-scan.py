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
    
def discoverMyNet(ip_range):
    FILE = 'discovered-nets.txt'
    CMD = ['sudo', 'netdiscover', '-r', ip_range, '-P']
    print('Discovering networks...')
    cmdOutputToFile(CMD, FILE)
    printFile(FILE)

def nmapFastScan(ip_range):
    FILE = 'nmap-fast-scan.txt'
    CMD = ['sudo', 'nmap', '-F', ip_range]
    print('Running a fast scan...')
    cmdOutputToFile(CMD, FILE)
    printFile(FILE)

def nmapSlowScan(ip_target):
    FILE = 'nmap-slow-scan.txt'
    CMD = ['sudo', 'nmap', '-sV', '-O', ip_target]
    print('Running slow scan...')
    cmdOutputToFile(CMD, FILE)
    printFile(FILE)



ipAddr()
ipRange = input('Enter ip range: ')
discoverMyNet(ipRange)
print('Using previous ip range for fast scan.')
nmapFastScan(ipRange)
ipTarget = input('Enter ip target: ')
nmapSlowScan(ipTarget)

