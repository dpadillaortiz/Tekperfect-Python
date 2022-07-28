#! /usr/bin/python3
'''
Introduce Modules
- don't reinvent the wheel
- useful tools
- useful to look at documentation
'''

import random

print('Lets play rock, paper, scissors!')

options = ['rock', 'paper', 'scissors']

'''
Intro to Methods
- take a look at the documentation on input()
- Take a look at documentation for random
'''
myChoice = input('Choose your option: ').lower()
botChoice = random.choice(options)

print(f'The computer chose: {botChoice}')

win = 'You win!'

'''
Introduce Control Flow
- We've been using one typ, sequencial
- Now we have decision/branching i.e. if/elif/else
'''
if myChoice == 'rock' and botChoice == 'scissors':
   # Why print over return?
   print(win)
elif myChoice == 'paper' and botChoice == 'rock':
   print(win)
elif myChoice == 'scissors' and botChoice == 'paper':
   print(win)
elif myChoice == botChoice:
   print('Tied!')
else:
   print('You lose!')

# What if we wanted to keep playing the game? It would be nice if we could loop over this code!
