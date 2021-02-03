sum_age = 0

for p in range(1, 5):
  print('----- {} PERSON -----'.format(p))
  name = str (input('Name: ')).strip()
  age = int (input('Age: '))
  sex = str (input('Sex [M/F]: ')).strip()
  sum_age += age

average = sum_age / 4

print('Average ages {:.2}'.format(average))