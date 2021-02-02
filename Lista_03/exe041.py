from datetime import date

birth =  int (input('Digite seu ano de nascimento: '))
age = date.today().year - birth

if age <= 9:
  print('MIRIN')
elif 9 < age <= 14:
  print('INFANTIL')
elif 14 < age <= 19:
  print('JUNIOR')
elif age == 20: 
  print('SÊNIOR')
else: 
  print('CATEGORIA NÃO CORRESPODENTE') 

