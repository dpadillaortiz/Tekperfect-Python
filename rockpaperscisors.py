#! /usr/bin/python3

import random

print('Welcome to Rock, Paper, Scissors!')
print('Type "exit" to exit the game.')
options = ['rock', 'paper', 'scissors']

while True:
   myChoice = input('Choose your option: ').lower()

   win = 'You win!'
   if myChoice == 'exit':
      print('Thank you for playing.')
      break
   if myChoice not in options:
      print('Your options are rock, paper, scissors.')
      continue


   botChoice = random.choice(options)
   print(f'The computer chose: {botChoice}')

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

