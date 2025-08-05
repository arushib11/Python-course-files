class Deck:
    values=[str(i) for i in range(2,11)]+["J","Q","K","A"]
    suits=["D","H","C","S"]
    
    def __init__(self):
        self.cards=[]
    
    def create_deck(self):
        for suit in Deck.suits:
            for value in Deck.values:
                card=value+suit
                self.cards.append(card)


    





     
    