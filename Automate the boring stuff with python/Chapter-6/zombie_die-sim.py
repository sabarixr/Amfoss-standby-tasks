import random

import zombiedice


class MyZombie(object):

    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        shotguns = 0

        while True:
            diceRollResults = zombiedice.roll()
            print(diceRollResults)

            if diceRollResults is None:
                return

            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            print('\n\n\nloop here\n\n\n')
            if shotguns == 3 or brains >= 13:
                return

            ques = input("Do you want to roll again? (yes/no): ").lower()
            if ques != 'yes':
                return


class RandomlyDecides(object):

        def __init__(self, name):
            self.name = name

        def turn(self, gameState):
            results = zombiedice.roll()
            print('\n\n\n\nloop here1\n\n\n\n')
            while results and random.randint(0, 1) == 0:
                return
class TwoBrains(object):
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0


        while True:
            dicerollresults = zombiedice.roll()
            if dicerollresults is None:
                return
            brains += dicerollresults['brains']
            print('\n\n\nloop hereyy\n\n\n')
            if brains == 2:
                return


class StopROllingMorebrains(object):
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        shotguns = 0
        while True:
            diceRollResults = zombiedice.roll()
            if diceRollResults is None:
                return
            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            print('\n\n\nloop herell\n\n\n')
            if diceRollResults is None:
                continue
            if shotguns > brains:
                return

import zombiedice

class FourTime(object):
    def __init__(self, name):
        self.name = name

    def turn(self, gameState):
        brains = 0
        shotguns = 0
        rolls = 0

        while rolls < 4:
            diceRollResults = zombiedice.roll()
            rolls += 1

            if diceRollResults is None:
                return

            brains += diceRollResults['brains']
            shotguns += diceRollResults['shotgun']
            print('\n\n\nloop heregg\n\n\n')
            print(shotguns)
            if shotguns >= 2:
                return


zombies = (
    zombiedice.examples.RandomCoinFlipZombie(name='Random'),
    zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),
    RandomlyDecides(name='Randomly decision bot'),
    MyZombie(name='My Zombie Bot'),
    StopROllingMorebrains(name='Shotgun win Bot'),
    TwoBrains(name = 'Two Brian bot'),
    FourTime(name = 'Dice four times bot')
    # Add any other zombie players here.
)




zombiedice.runWebGui(zombies=zombies, numGames=2)
