salario = int (input('Salário: '))

if salario > 1250:
  salario = salario + salario * 0.1
else: 
  salario = salario + salario * 0.15

print('O novo salário é de R${}'.format(salario))