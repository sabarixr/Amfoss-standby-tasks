import random

numberOfStreaks = 0

flips = []
for experimentNumber in range(10000):
    choice = ['H', 'T']
    for i in range(100):
        flips.append(random.choice(choice))

test_case_h = ['H', 'H', 'H', 'H', 'H', 'H']
test_case_t = ['T', 'T', 'T', 'T', 'T', 'T']

for i in range(len(flips)):
    if flips[i: i + 6] == test_case_h or flips[i: i + 6] == test_case_t:
        numberOfStreaks += 1

print('Chance of streak: %s%%' % (numberOfStreaks / 100))
