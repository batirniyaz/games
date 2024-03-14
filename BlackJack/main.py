import random

class BlackJact():
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]


    def deal_card(self):
        return random.choice(self.cards)
    
