from datetime import date

current = date.today().year

birth = int(input('Ano de nascimento: '))
age = current - birth

print('Quem nasceu em {} tem {} anos em {}'.format(birth, age, current))

if age==18:
  print('Você tem que se alistar IMEDITAMENTE! ')
elif age < 18: 
  print('Você ainda não tem 18 anos. Você tem só {}. Deverá se alistar em {}'.format(age, birth + 18))
else:
  print('Você está com {}! Você deveria ter se alistado em {}'.format(age, birth + 18))