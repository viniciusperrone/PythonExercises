from random import randint

items = ('Stone', 'Paper', 'Scissors')
computer = randint(0,2)

print('{:-^50}'.format('Choose one of the options'))

print('[ 0 ] STONE')
print('[ 1 ] PAPER')
print('[ 2 ] SCISSORS')

player = int (input("What's your move ? "))

#computer threw stone

if computer == 0:
  if player == 0:
    print('Draw!')
  elif player == 1:
    print('You won!')
  elif player == 2:
    print('You lost!')

#computer threw paper

elif computer == 1:
  if player == 0:
    print('You lost!')
  elif player == 1:
    print('Draw!')
  elif player == 2:
    print('You won!')

#computer threw scissors

elif computer == 2:
  if player == 0:
    print('You lost!')
  elif player == 1:
    print('You won!')
  elif player == 2:
    print('Draw!')

else:
  print('INVALID MOVE!')