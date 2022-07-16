#! /usr/bin/python3

import random

print('Welcome to Rock, Paper, Scissors!')

options = ['rock', 'paper', 'scissors']

myChoice = input('Choose your option: ').lower()
botChoice = random.choice(options)
print(f'The computer chose: {botChoice}')

win = 'You win!'

if myChoice == 'rock' and botChoice == 'scissors':
   print(win)
elif myChoice == 'paper' and botChoice == 'rock':
   print(win)
elif myChoice == 'scissors' and botChoice == 'paper':
   print(win)
elif myChoice == botChoice:
   print('Tied!')
else:
   print('You lose')

