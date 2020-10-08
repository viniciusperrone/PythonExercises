velocidade = int (input('Velocidade: '))

preco = 0

if velocidade > 80: 
  preco = float (velocidade - 80) * 7
else: 
  print('Você não ultrapassou o limite de velocidade!')

print('Multa: R${:.2f}'.format(preco))