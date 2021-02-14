while True:
  number = int (input('Multiplication table of: '))
  if number < 0:
    print('Invalid number!')
    break
  print('-'*30)
  for c in range(1, 11):
    print(f'{number} x {c} = {number * c}')
  print('-'*30)