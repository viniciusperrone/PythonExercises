phrase = str (input('Digite uma frase:')).strip().upper()

words = phrase.split()
together = ''.join(words)
reverse = ''

for letters in range(len(together) -1, -1, -1):
  reverse += together[letters] 

print(reverse + ' ' + together)
if reverse == together:
  print('We have word palindrome!')
else: 
  print('The phrase entered is not a palindrome!')
