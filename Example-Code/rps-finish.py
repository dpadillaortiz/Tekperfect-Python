#! /usr/bin/python3

# Introduce Modules
# - don't reinvent the wheel
# - useful tools

import random

print('Lets play rock, paper, scissors!')

# Now we want a way out
print('Type "exit" to exit the game.')

options = ['rock', 'paper', 'scissors']

# Introduce Control Flow

while True:
    # talk about methods
    myChoice = input('Choose your option: ').lower()
    # assert statement for myChoice or use if-statement
    
    if myChoice == 'exit':
        # Talk about break, continue, pass
        break

    botChoice = random.choice(options)

    print(f'The computer chose: {botChoice}')

    win = 'You win!'
    
    # What are your conditions to win? lose? tie?
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

