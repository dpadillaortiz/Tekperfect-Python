#! /usr/bin/python3

from sys import argv

name = 'Jose'

x = f'My name is {name}'

print(x)

# these arguments are passed when the file is ran
script, first, second, third = argv

print('This script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:', third)
