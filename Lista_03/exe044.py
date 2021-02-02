print('{:-^40}'.format('LOJAS PERRONE'))

price = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('[1] à vista dinheiro/cheque')
print('[2] à vista cartão')
print('[3] 2x no cartão')
print('[4] 3x ou mais no cartão')

option = int (input('Qual é sua opção: '))

if option == 1:
  total = price - (price * 10 / 100)
elif option == 2:
  total = price - (price * 5 / 100)
elif option == 3:
  total = price
  parceled = total / 2
  print('Sua compra será parcelada 2x de R${:.2f} SEM JUROS'.format(total))
elif option == 4: 
  total = price + (price * 20 / 100)
  count_parceled = int (input('Quantas parcelas: '))
  parceled = total / count_parceled
  print('Sua compra será parcelada {}x de R${:.2f} COM JUROS'.format(count_parceled, total))

print('Sua compra de R${:.2f} vai custar R${:.2} no final'.format(price, total))