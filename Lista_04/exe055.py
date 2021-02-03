bigger = 0
smaller = 0

for c in range(1,7):
  weight = float (input('The weight of the {} person is 80 kiles'.format(c)))
  if c == 1:
    bigger = weight
    smaller = weight
  else: 
    if weight > bigger:
      bigger = weight
    elif weight < smaller:
      smaller = weight

print('The highest weight read was {}Kg'.format(bigger))
print('The smallest weigth was {}Kg'.format(smaller))