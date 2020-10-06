import random

nome_01 = str (input('Primeiro nome: '))
nome_02 = str (input('Segundo nome: '))
nome_03 = str (input('Terceiro nome: '))
nome_04 = str (input('Quarto nome: '))

lista = [nome_01, nome_02, nome_03, nome_04]
random.shuffle(lista)

print('Ordem de apresentação: ')
print(lista)