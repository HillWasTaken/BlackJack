#imports
import random
from cards import *

#get random card from the list of cards and card names
randomCard = (random.choice(test), random.choice(cardNames))

#print the random card
print(f"{randomCard[0]['name']} of {randomCard[1]}")