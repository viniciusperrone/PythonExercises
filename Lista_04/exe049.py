number = int (input('Enter a number for your multiplication table: '))

for c in range(1, 11):
  print('{} x {:2} = {}'.format(number, c, number*c))