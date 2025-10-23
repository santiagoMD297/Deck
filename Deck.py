import random
class deck_code:
    def create_deck(self):
        rank = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
        suit = ['H', 'D', 'C', 'S']
        deck_of_cards = []
        for r in rank:
            for s in suit:
                card = (r , s)
                deck_of_cards.append(card)
        return deck_of_cards
    
    def get_top(self, the_deck):
        return the_deck[0]
    
    def get_bottom(self, the_deck):
        return the_deck[-1]
    
    def get_selected_card(self, the_deck, num):
        return the_deck[num-1]
    
    def get_random(self, the_deck):
        number = random.randint(0, 51)
        return the_deck[number]
    
    def 


