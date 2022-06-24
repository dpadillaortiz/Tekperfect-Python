#! /usr/bin/python3

# Introduce Modules
# - don't reinvent the wheel
# - useful tools

import random

print('Lets play rock, paper, scissors!')

options = ['rock', 'paper', 'scissors']

# Introduce Control Flow
# Start with if/elif/else statements

# talk about methods
myChoice = input('Choose your option: ').lower()
# Add an assert here for myChoice
    
botChoice = random.choice(options)

# talk about string formatting
print(f'The computer chose: {botChoice}')

win = 'You win!'
    
# What are your conditions to win? lose? tie?
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
