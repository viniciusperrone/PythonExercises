number_first = int (input('First value: '))
number_second = int (input('Second value: '))

option = 0

while option != 5:
  print('''
  [1] Add
  [2] Multiply
  [3] Higher
  [4] New numbers
  [5] Get out''')

  option = int (input('>>>>>>> What is your option ?'))

  if option == 1: 
    sum = number_first + number_second
    print('The sum of {} plus {} is equal to {}'.format(number_first, number_second, sum))
  elif option == 2: 
    product = number_first * number_second
    print('The product of {} times {} is equal to {}'.format{number_first, number_second, product})
  elif option == 3: 
    if number_first > number_second:
      higher = number_first
      print('The first number is the largest')
    else: 
      higher = number_second
      print('The second number is the largest')
    elif option == 4:
      print('Enter the two numbers agains')
      number_first = int (input('First value: '))
      number_second = int (input('Second value: '))
    elif option == 5:
      print('Finishing...')
    else: 
      print('Option invalid...try again')
print('End od program! Check back often!')