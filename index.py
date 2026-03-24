#imports
import random
from cards import *

randomCard = (random.choice(test), random.choice(cardNames))

print(f"{randomCard[0]['name']} of {randomCard[1]}")