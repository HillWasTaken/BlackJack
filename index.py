#imports
import random

# lists with all the cards
cardNames = ["Spades", "Hearts", "Diamonds", "Clubs"]
test = [
    {"value": 1, "name": "Ace"}, {"value": 2, "name": "Two"}, {"value": 3, "name": "Three"}, {"value": 4, "name": "Four"}, {"value": 5, "name": "Five"},
    {"value": 6, "name": "Six"}, {"value": 7, "name": "Seven"}, {"value": 8, "name": "Eight"}, {"value": 9, "name": "Nine"}, {"value": 10, "name": "Ten"},
    {"value": 10, "name": "Jack"}, {"value": 10, "name": "Queen"}, {"value": 10, "name": "King"}
]

randomCard = (random.choice(test), random.choice(cardNames))

print(f"{randomCard[0]['name']} of {randomCard[1]}")