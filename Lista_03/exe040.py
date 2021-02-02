first_note = float (input('Digite sua primeira nota: '))
second_note = float (input('Digite sua segunda nota: '))

arithmetic_average = (first_note + second_note) / 2

if 0 <= arithmetic_average < 5.0:
  print('REPROVADO')
elif 5 <= arithmetic_average < 7:
  print ('RECUPERAÇÃO')
elif 7 <= arithmetic_average <= 10:
  print('APROVADO')
else: 
  print('NOTAS INVÁLIDAS! ')