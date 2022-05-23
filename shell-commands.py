#! /usr/bin/python3


import os
import subprocess

# os.system("echo Hello from Python")
'''
homeDir = os.system("cd ~")

print("`cd ~` ran with exit code %d" % homeDir)

unknownDir = os.system("cd doesnotexist")

print("`cd doesnotexist` ran with exit code %d" % unknownDir)
'''

# listFiles = subprocess.run(["ls", "-l"])

# listFiles = subprocess.run(["ls", "-l"], stdout=subprocess.DEVNULL)
# print('The exit code was: %d' % listFiles.returncode)


# useless = subprocess.run(['cat'], stdout=subprocess.PIPE, text=True, input="Hello from Python")
# print(useless.stdout)

# failed = subprocess.run(['false'], check=True)
# print('The exit code was: %d' % failed.returncode)

# listDir = subprocess.Popen(['ls','-l'])
# listDir.wait()
# listDir.poll()


# useless = subprocess.run(['cat'], stdout=subprocess.PIPE, text=True, input="Hello from Python")
'''
useless = subprocess.Popen(['cat'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
output, errors = useless.communicate(input="Hello")
useless.wait()
print(output)
print(errors)
'''


# homeDir = os.system("sudo netdiscover -r 192.168.0.0/24")
# print(homeDir)

netDisc = subprocess.run(['netdiscover','-r','192.168.0.0/24'])
print(netDisc)













