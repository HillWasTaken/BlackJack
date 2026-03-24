#imports
import random
import time
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

def playGame():
    playerCards = [getRandomCard(), getRandomCard()]
    dealerCards = [getRandomCard(), getRandomCard()]
    playerHand = [f"{playerCards[0][0]['name']} of {playerCards[0][1]}", f"{playerCards[1][0]['name']} of {playerCards[1][1]}"]

    gameOver = False
    input('Welcome to blackjack! Press enter to start playing...')
    print('Dealing cards...\n')
    time.sleep(1)
    while not gameOver:
        playerScore = getScore(playerCards)
        dealerScore = getScore(dealerCards)
        print(f'Your cards: {playerHand} - Total score: {playerScore}')
        print(f'Dealer cards: {dealerCards[0][0]['name']} of {dealerCards[0][1]}')
        
        if playerScore > 21:
            print(f"You're bust... Your total score was: {playerScore}.")
            gameOver = True
            return
        
        choice = input("Do you want to draw another card(hit) or stand(stand)...")
        
        if choice == 'hit':
            addedCard = getRandomCard()
            playerCards.append(addedCard)
            playerHand.append(f"{addedCard[0]['name']} of {addedCard[1]}")
        elif choice == 'stand':
            print(f"Dealer cards: {dealerCards[0][0]['name']} of {dealerCards[0][1]}, {dealerCards[1][0]['name']} of {dealerCards[1][1]} - Total score: {dealerScore}")
        
playGame()