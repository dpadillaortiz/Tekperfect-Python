#! /usr/bin/python3

import random

print('Rock, paper, scissors!')

options = ['rock', 'paper', 'scissors']

myChoice = input('Rock, paper, or scissors: ')

botChoice = random.choice(options)
print(f'The computer chose: {botChoice}')

results = {
	'rock':{'scissors':'Win', 'paper':'Lose', 'rock':'Tie'},
	'paper':{'rock':'Win', 'scissors':'Lose', 'paper':'Tie'},
	'scissors':{'paper':'Win', 'rock':'Lose', 'scissors':'Tie'}
}

if results[myChoice][botChoice] == 'Win':
	print('I win')
elif results[myChoice][botChoice] == 'Lose':
	print('I lose')
else:
	print('Tied')
