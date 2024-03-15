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

        if user_sum == 21 and len(self.user_card) == 2:
            return 0
        
        if 11 in self.user_card and sum(self.cards) > 21:
            self.cards.remove(11)
            self.cards.append(1)

        return user_sum, diller_sum
    
    def check_score(self, user_sum, diller_sum):
        if user_sum == 21:
            return "user_won"
        elif user_sum < 21:
            pass
        else:
            return "user_lose"
        
        if diller_sum == 21:
            return "diller_won"
        elif diller_sum < 21 and diller_sum > 16:
            pass
        elif diller_sum < 17:
            pass
        else:
            return "diller_lose"

        
    

c = BlackJact()

        
