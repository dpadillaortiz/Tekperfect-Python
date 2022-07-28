#! /usr/bin/python3

import random

print('Lets play rock, paper, scissors!')

options = ['rock', 'paper', 'scissors']

'''
Control Flow Cont'd
- Loops i.e. for and while
- break, continue, pass
'''

while True:
   myChoice = input('Choose your option: ').lower()
   if myChoice not in options:
      # pass 
      # - Executes nothing (does nothing) and continues with the rest of the code
      continue 
      # = Skips the iteration of the loop and restarts the loops so the bottom part of the code does not execute
   
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
      print('You lose!')

