rank = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
suit = ['H', 'D', 'C', 'S']
deck_of_cards = []
for r in rank:
    for s in suit:
        card = (r , s)
        deck_of_cards.append(card)