print('-'*30)
print('Fibonacci Sequence')
print('-'*30)
number = int(input('How many numbers do you want to show ? '))

t1 = 0
t2 = 1

print('~'*30)
print('{} -> {}'.format(t1, t2), end='')
t3 = t1 + t2
cont = 3 

while cont <= n:
  t3 = t1 + t2
  print(' -> {}'.format(t3), end='')
  cont += 1
  t1 = t2
  t2 = t3
print(' -> END')