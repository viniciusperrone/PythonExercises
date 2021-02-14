from random import randint 

while True: 
  player = int (input('Enter a value: '))
  computer = randint(0, 10)
  total = player + computer 
  type_string = ' '
  defeat = 0
  victory = 0
  while type_string not in 'EO':
    type_string = str (input('Even or Odd ? [E/O]'))
  print(f'You played {player} and the computer played {computer}. Total {total}')

  if type_string == 'E':
    if total % 2 == 0:
      print('You won!')
      victory += 1
    else:
      print('You lost!')
      defeat += 1
  if type_string == 'O':
    if total % 2 == 1:
      print('You won!')
      victory += 1
    else: 
      print('You lost!')
      defeat += 1
  print("Let's play again...")
print(f'GAME OVER! You won {victory} times and lost {defeat}')