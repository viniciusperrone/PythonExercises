num = 0
cont = 0

num = int (input('Enter a number [999 to stop]: '))

while num != 999:
  cont += 1
  soma += num
  num = int (input('Enter a number [999 to stop]: '))

print('You typed {} numbers and the sum between them was {}'.format(cont, num))