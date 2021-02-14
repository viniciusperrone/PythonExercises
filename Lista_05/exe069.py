age18 = totMen = totWoman = 0 

while True: 
  age = int (input('Age: '))
  sex = ' '
  while sex not in 'MF':
    sex = str (input('Sex: [M/F] ')).strip().upper()[0]
  if age >= 18:
    age18 += 1
  if sex == 'M':
    totMen += 1
  if sex == 'F' and age < 20:
    totWoman += 1
  answer = ' '
  answer = str (input('Do you want to continue ? [Y/N] ')).strip().upper()[0]
  if answer == 'N':
    break
print(f'Total people over 18 years old: {age18}')
print(f'Altogether we have {totMen} men registered') 
print(f'And we have {totWoman} women unger the age of 20')

