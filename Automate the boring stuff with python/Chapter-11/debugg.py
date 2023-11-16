import random

guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')

# guess is getting entered as a string value while the toss is a random int between 0 and 1 so ofc it never become equal so the program will always print Nope. You are really bad at this game.


# corrected code
#
#
#     import random
#     guess = ''
#      while guess not in ('heads', 'tails'):
#          print('Guess the coin toss! Enter heads or tails:')
#          guess = input()
#      toss = random.choice(['heads', 'tails']) # 0 is tails, 1 is heads
#      if toss == guess:
#          print('You got it!')
#       else:
#           print('Nope! Guess again!')
#           guesss = input()
#           if toss == guess:
#               print('You got it!')
#           else:
#                 print('Nope. You are really bad at this game.')
#
#
#       or
#
#       you can use if to assign head or tail as string to a variable and
#        then checking it with toss then it will oth be string
