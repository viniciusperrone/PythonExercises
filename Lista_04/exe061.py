print('Arithmetic Pogression Generator')
print('-=' * 10)
first = int (input('First Term: '))
reason = int (input('Reason: '))
term  = first
cont = 1

while cont <= 10: 
  print('{} -> '.format(term), end='')
  term = term + reason
  cont += 1

print('END')