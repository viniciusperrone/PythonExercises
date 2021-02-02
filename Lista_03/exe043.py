weight = float (input('Digite seu peso: '))
height = float (input('Digite sua altura: '))

imc = weight / (height ** 2)

print('O IMC dessa pessoa é de {:.2f}'.format(imc))

if imc < 18.5:
  print('VOCÊ ESTÁ ABAIXO DO PESO NORMAL')

elif 18.5 <= imc < 25:
  print('VOCÊ ESTÁ NO PESO IDEAL')
elif 25 <= imc < 30: 
  print('VOCÊ ESTÁ SOBREPESO')
elif 30 <= imc < 40:
  print('VOCÊ ESTÁ OBESO')
elif imc >= 40:
  print('VOCÊ ESTÁ COM OBESIDADE MORBIDA')
