number = int(input('Digite um número: '))

print('-----CONVERSÃO-----')
print('1 - BINÁRIO')
print('2 - OCTAL')
print('3 - HEXADECIMAL')

choice = int(input('SUA COVERSÃO É: '))

if choice==1:
  print('{} convertido para BINÁRIO é igual a {}'.format(number, bin(number)))
elif choice==2:
  print('{} convertido para BINÁRIO é igual a {}'.format(number, oct(number)))
elif choice==3: 
  print('OK part III')
else: 
  print('{} convertido para BINÁRIO é igual a {}'.format(number, hex(number)))