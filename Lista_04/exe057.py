sex = str (input('Tell your gender: [M/F]')).strip().upper()[0]

while sexo not in 'MmFf':
  sex = str (input('Invalid data. Please enter your gender: ')).strip().upper()[0]

print('Successfully registered {} gender'.format(sex))


