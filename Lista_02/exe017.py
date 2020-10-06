from math import pow, sqrt

cateto_oposto = int(input('Cateto oposto: '))
cateto_adjacente = int(input('Cateto adjacente: '))

hipotenusa = sqrt((pow(cateto_oposto, 2)) + (pow(cateto_adjacente, 2)))

print('O Hipotenusa é {}'.format(hipotenusa))
