frase = str (input('Digite uma frase: '))

print('A letra A aparece {} vezes'.format(frase.upper().count('A')))
print('A letra A aparece pela primeira vez na posição {}'.format(frase.upper().find('A')+1))
print('A letra A aparece pela última vez na posição {}'.format(frase.upper().rfind('A')+1))