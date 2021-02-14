print('='*30)
print('{:^30}'.format('BANK SERVER'))
print('='*30)

value = int (input('What value do you want to withdraw ?'))
total = value
ced = 50
totalCed = 0

while True:
  if total >= ced:
    total -= ced
    totalCed += 1
  else:
    if totalCed > 0:
      print(f'Total was {totalCed} cells of R${ced}')
    if ced == 50:
      ced = 20
    elif ced == 20:
      ced = 10
    elif ced == 10:
      ced = 1
    totalCed = 0
    if total == 0:
      break

print('='*30)
print('Always come back to BANK SERVER! Have a nice day!')

