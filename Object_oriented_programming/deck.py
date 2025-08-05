# class deck that represents a deck of 52 playing cards. The Deck should maintain which cards are currently in the deck(never duplicate cards)
# Cards should be represented by a string containing their value (2-10,J,Q,K,A) followed by their suit (D,H,C,S)
# Deck should implement following:
# shuffle() shuffles cards randomly in place - use random.shuffle()
# deal(n) removes and returns last n cards from the deck in a list. If deck does not have enough cards, returns all cards.
# sort_by_suit() sorts cards by suit placing hearts, diamonds,clubs and spades(this order). It should not sort in place and does not return anything
# contains(card) Returns True if given card exists, False otherwise
# copy() Returns new Deck object that is copy of currents deck. Any modifications to new Deck object should not affect Deck object that was copied
# get_cards() Returns all the cards in the deck in a list. Any modifications to returned list should not change Deck object.
# __len__() This method returns number of cards in the Deck
# Deck should always start with exactly 52 cards distributed across 4 suits and 13 values with no duplicate cards

import random

class Deck:
    values=[str(i) for i in range(2,11)]+["J","Q","K","A"]
    suits=["D","H","C","S"]

    def __init__(self):
        self.cards=[]
        self.make_deck()

    def make_deck(self):
        for suit in self.suits:
            for value in self.values:
                card=value+suit
                self.cards.append(card)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self,n):
        dealt_cards=[]
        for i in range(n):
            if len(self.cards)==0:
                break
            card=self.cards.pop()
            dealt_cards.append(card)
        return dealt_cards
    
    def sort_by_suit(self):
        cards_by_suit={"H":[],"D":[],"C":[],"S":[]}
        for card in self.cards:
            suit=card[-1]
            cards_by_suit[suit].append(card)
        self.cards=[cards_by_suit["H"]+cards_by_suit["D"]+cards_by_suit["C"]+cards_by_suit["S"]]

    def contains(self,card):
        return card in self.cards
    
    def copy(self):
        new_deck=Deck()
        new_deck.cards=self.cards[:]
        return new_deck
    
    def get_cards(self):
        return self.cards[:]
    
    def __len__(self):
        return len(self.cards)


'''
** Checks run **
def test_case_1(self):
        fs = FileSystem()
        fs.create_directory("/dir1")
        fs.create_directory("/dir2")
        fs.create_directory("/dir1/dir3")
        with self.assertRaises(ValueError):
            fs.create_directory("/dir3/dir4")

    def test_case_2(self):
        fs = FileSystem()
        fs.create_file("/tim.txt", "Tim is great!")
        with self.assertRaises(ValueError):
            fs.create_file("/dir1/simon.txt", "ProgrammingExpert is fun!")
        self.assertEqual("Tim is great!", fs.read_file("/tim.txt"))

    def test_case_3(self):
        fs = FileSystem()
        fs.create_file("/tim.txt", "12345")
        self.assertEqual(fs.size(), 5)
        fs.create_file("/alex.txt", "67890")
        self.assertEqual(fs.size(), 10)

    def test_case_4(self):
        fs = FileSystem()
        fs.create_directory("/dir1")
        fs.create_directory("/dir1/dir2")
        fs.create_directory("/dir1/dir2/dir3")
        fs.create_file("/dir1/dir2/file1.txt", "1")
        fs.create_file("/dir1/dir2/dir3/file2.txt", "1")
        self.assertEqual(fs.size(), 2)

    def test_case_5(self):
        fs = FileSystem()
        with self.assertRaises(ValueError):
            fs.delete_directory_or_file("/dir1")
        fs.create_directory("/dir1")
        fs.create_file("/dir1/simon.txt", "ProgrammingExpert is fun!")
        self.assertEqual(25, fs.size())
        with self.assertRaises(ValueError):
            fs.delete_directory_or_file("/dir2")
        fs.delete_directory_or_file("/dir1")
        self.assertEqual(0, fs.size())

    def test_case_6(self):
        fs = FileSystem()
        fs.create_directory("/dir1")
        fs.create_directory("/dir1/dir2")
        fs.create_file("/dir1/dir2/file1.html", "Hello World")
        self.assertEqual(11, fs.size())
        self.assertEqual("Hello World", fs.read_file("/dir1/dir2/file1.html"))
        fs.delete_directory_or_file("/dir1")
        self.assertEqual(0, fs.size())
        with self.assertRaises(ValueError):
            fs.read_file("/dir1/dir2/file1.html")


'''

