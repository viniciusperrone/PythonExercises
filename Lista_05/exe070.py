total = cont = totThousand = smallest = 0
low_price = ' '

while True: 
  product = str (input("Product's name: "))
  price = float (input("Price: "))
  cont += 1
  total += price

  if price > 1000: 
    totThousand += 1
  if cont == 1:
    smallest = price
    low_price = product

  else:
    if price < smallest:
      smallest = price
      low_price = product

  answer = ' '

  while answer not in 'YN':
    answer = str (input('Do you want to continue ? [Y/N]')).strip().upper()[0]

  if answer == 'N':
    break

print('{:-^40}'.format(' End of program '))
print(f'Total purchase was R${total:.2f}'.format(' End of program '))
print(f'We have {totThousand} products consting over R$1000.00')
print(f'The cheapest product was the {low_price} which costs R${smallest:.2f}')



