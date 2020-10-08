import random

number = ['0', '1', '2', '3', '4', '5']

number = int (random.choice(number))

n = int (input('Digite um numero: '))

if n == number:
  print('Você acertou!')
else: 
  print('Você errou!')

print('Acabou o game!')
