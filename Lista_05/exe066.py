sum = 0

while True:
  number = int (input('Enter a value [999 to stop]: '))
  if number == 999:
    break
  sum += number

print('The sum of the values is {sum}')