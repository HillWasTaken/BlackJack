#imports
import random
from cards import *

#make the game loop
game = True

#get random card from the list of cards and card names
def getRandomCard():
    randomCard = (random.choice(test), random.choice(cardNames))
    return randomCard