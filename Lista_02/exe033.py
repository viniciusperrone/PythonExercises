a = int (input('Digite um número: '))
b = int (input('Digite um número: '))
c = int (input('Digite um número: '))

maior = 0
menor = 0

if a > b > c:
  maior = a
  menor = c
elif a > c > b:
  maior = a
  menor = b
elif b > a > c:
  maior = b
  menor = c
elif b > c > a:
  maior = b
  menor = a
elif c > a > b:
  maior = c
  menor = b
else: 
  maior = c
  menor = b

print('Maior é {}'.format(maior))
print('Menor é {}'.format(menor))