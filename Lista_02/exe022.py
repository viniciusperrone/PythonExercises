nome = str (input('Digite seu nome: '))

letras_maiusculas = nome.upper()
letras_minusculas = nome.lower()

print(letras_maiusculas)
print(letras_minusculas)
print(len(nome) - nome.count(' '))