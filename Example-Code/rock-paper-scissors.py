#! /usr/bin/python3

import random

print('Lets play rock, paper, scissors!')
print('Type "exit" to exit the game.')

options = ['rock', 'paper', 'scissors']

while True:
    myChoice = input('Choose your option: ').lower()
    
    if myChoice == 'exit':
        break

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

