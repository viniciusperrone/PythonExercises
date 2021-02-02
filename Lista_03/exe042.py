side_one = int (input('Reta 1: '))
side_two = int (input('Reta 2: '))
side_three = int (input('Reta 3: '))

if side_one < side_two + side_three and side_two < side_one + side_three and side_three < side_one + side_two:
  print('Os segmentos formam triângulo!')
  if side_one == side_two == side_three:
    print('EQUILÁTERO')
  elif side_one != side_two != side_three != side_one:
    print('ESCALENO')
  else: 
    print('ISÓSCELES')
  
else: 
  print('Os segmentos não formam triângulo!')