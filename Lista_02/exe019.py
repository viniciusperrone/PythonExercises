import random

aluno_01 = str (input('Digite o primeiro aluno: '))
aluno_02 = str (input('Digite o segundo aluno: '))
aluno_03 = str (input('Digite o terceiro aluno: '))
aluno_04 = str (input('Digite o qaurto aluno: '))

lista = [aluno_01, aluno_02, aluno_03, aluno_04]

print('O aluno escohido é {}'.format(random.choice(lista)))