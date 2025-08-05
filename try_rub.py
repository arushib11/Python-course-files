import random
class Deck:
    values=["i" for i in range(1,11)]+["J","Q","K","A"]
    suits=["D","H","C","S"]
    
    def __init__(self):
        self.cards=[]
        self.deck_cards()

    def deck_cards(self):
        for suit in Deck.suits:
            for value in Deck.values:
                card=value+suit
                self.deck_cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self,n):
        dealt_deck=[]
        for i in range(n):
            if len(self.cards)==0:
                break
            dealt_card=self.deck_cards.pop()
            dealt_deck.append(dealt_card)
        return dealt_deck
    
    def sort_by_suit(self):
        sorted_deck={"H":[],"D":[],"C":[],"S":[]}
        for card in self.deck_cards:
            suit=card[-1]
            sorted_deck[suit].append(card)
        self.deck_cards=[sorted_deck["H"]+sorted_deck["D"]+sorted_deck["C"]+sorted_deck["S"]]

    def contains(self,card):
        if card in self.deck_cards:
            return True
        return False
    
    def copy(self):
        new_deck_cards=self.deck_cards[:]
        new_deck=Deck()
        return new_deck
    
    def get_cards(self):
        new_deck_cards=self.deck_cards[:]
        return new_deck_cards
    
    def __len__(self):
        return len(self.deck_cards)
    





