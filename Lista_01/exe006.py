import math

number = int (input('Digite um número: '))

dobro = number*2
triplo = number*3
raiz = math.sqrt(number)

print(' O Dobro é {} \n O Triplo é {} \n A raiz quadrada é {:.3f}'.format(dobro, triplo, raiz))