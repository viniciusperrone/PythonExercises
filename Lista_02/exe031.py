distancia = float (input('Distância percorrida: '))

preco = 0
if distancia <= 200:
  preco = float (distancia * 0.5)
else: 
  preco = float (distancia * 0.45)

print('Preço pela corrida é de: R${:.2f}'.format(preco))