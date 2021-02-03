from datetime import date
current = date.today().year

bigger = 0
smaller = 0

for person in range(1,8):
  year = str (input('What year was the {} person born ? '.format(person)))
  age = current - year
  if year >= 21:
    bigger += 1
  else:
    smaller += 1

print('Altogether we had {} older people'.format(bigger))
print('Altogether we had {} underage people'.format(smaller))
