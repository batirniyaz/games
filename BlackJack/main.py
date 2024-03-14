import random

class BlackJact():
    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,]
        self.user_card = []
        self.diller_card = []


    def deal_card(self):
        rand_card = random.choice(self.cards)
        return rand_card
        
    
    def get_card(self):
        self.user_card.append(self.deal_card())
        self.diller_card.append(self.deal_card())

    def calculate_score(self):
        user_sum = sum(self.user_card)
        diller_sum = sum(self.diller_card)
        return user_sum, diller_sum
    
    d

c = BlackJact()

        
