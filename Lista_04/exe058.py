from random import randint
computer = randint(0,10)

print("I'm your computer...I just thought of a number between 0 and 10")
print('Can you guess ?')

hit = False

hunch = 0

while not hit:
  player = int (input("What's your guess ? "))
  hunch += 1
  if player == computer:
    hit = True
  else: 
    if player < computer:
      print('More...try again')
    elif player > computer
      print('Less...try again')
print("You guessed right with {} guesses!".format(hunch)) 