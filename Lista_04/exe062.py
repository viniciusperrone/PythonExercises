print('Arithmetic Pogression Generator')
print('-=' * 10)
first = int (input('First Term: '))
reason = int (input('Reason: '))
term  = first
cont = 1
total = 0
more = 10

while more != 0:
  total = total + more
  while cont <= total: 
    print('{} -> '.format(term), end='')
    term += reason 
    cont += 1
  print('BREAK')
  more = int (input('How many terms do you want to show the most ?'))