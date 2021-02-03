first = int (input('First term: '))
reason = int (input('Reason: '))

tenth = first + ((10 - 1) * reason)

for c in range(first, tenth, reason):
  print('{}'.format(c), end='-> ')
print('ENDED!')