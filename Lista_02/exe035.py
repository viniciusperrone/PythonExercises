reta01 = int (input('Reta 1: '))
reta02 = int (input('Reta 2: '))
reta03 = int (input('Reta 3: '))

if reta01 > reta02 > reta03: 
  if (reta02 - reta03) < reta01 < (reta02 + reta03):
    print('Forma um triângulo!')
  else: 
    print('Não forma um triângulo!')

elif reta01 > reta03 > reta02: 
  if (reta03 - reta02) < reta01 < (reta03 + reta02):
    print('Forma um triângulo!')
  else: 
    print('Não forma um triângulo!')

elif reta02 > reta01 > reta03: 
  if (reta01 - reta03) < reta02 < (reta01 + reta03):
    print('Forma um triângulo!')
  else: 
    print('Não forma um triângulo!')

elif reta02 > reta03 > reta01: 
  if (reta03 - reta01) < reta02 < (reta03 + reta01):
    print('Forma um triângulo!')
  else: 
    print('Não forma um triângulo!')

elif reta03 > reta01 > reta02: 
  if (reta01 - reta02) < reta03 < (reta01 + reta02):
    print('Forma um triângulo!')
  else: 
    print('Não forma um triângulo!')

elif reta03 > reta02 > reta01: 
  if (reta02 - reta01) < reta03 < (reta02 + reta01):
    print('Forma um triângulo!')
  else: 
    print('Não forma um triângulo!')

else: 
  print('Não forma triângulo')