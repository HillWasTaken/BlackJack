#imports
import random
from cards import *

#make the game loop
game = True

#get random card from the list of cards and card names
def getRandomCard():
    randomCard = (random.choice(test), random.choice(cardNames))
    return randomCard

currentScore = 0
def gameFunction():
    global game
    global currentScore
    currentScore = 0
    while game:
        randomCard = getRandomCard()
        currentScore += randomCard[0]['value']
        print(f"{randomCard[0]['name']} of {randomCard[1]}, current score: {currentScore}")
        if currentScore >= 21:
            game = False

while game:
    gameFunction()