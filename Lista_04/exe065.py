answer = 'S'
media = sum = amount = 0
while answer in 'Ss':
  num = int (input('Enter a number: '))
  sum += sum 
  amount += 1
  answer = str(input('Want to continue ? [S/N] ')).upper().strip()[0]

media = sum / amount

print('You typed {} numbers and the average was {}'.format(amount, media))