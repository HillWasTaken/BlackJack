#imports
import random
from cards import *

#make the game loop
game = True

#get random card from the list of cards and card names
def getRandomCard():
    randomCard = [random.choice(test), random.choice(cardNames)]
    return randomCard

#get the score of the cards
def getScore(cards):
    total = 0
    for card in cards:
        cardName = card[0]['name']
        cardValue = card[0]['value']
        if cardName == 'Ace' and total < 21:
            cardValue = 11
        elif cardName == 'Ace' and total >= 21:
            cardValue = 1
        total += cardValue
    return total

randomCards = getRandomCard(), getRandomCard()
print(getScore(randomCards))