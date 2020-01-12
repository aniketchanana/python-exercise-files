from random import randint,shuffle

class Card:
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value
    
    def __repr__(self):
        return f"{self.value} of {self.suit}"

class Deck:
    suits = ["Hearts","Diamonds","Clubs","Spades"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    def __init__(self):
        self.cards = [ Card(suit=suit,value=value) for suit in Deck.suits for value in Deck.values ]
    
    def __repr__(self):
        return f"Deck of {self.count()} cards"

    def count(self):
        return len(self.cards)
    
    def _deal(self,num):
        count = self.count()
        actual = min([count,num])
        if count == 0:
            raise ValueError("All Cards have been dealt")
        
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards
    
    def shuffle(self):
        if self.count != 52:
            raise ValueError("Only full card can be shuffled")
        shuffle(self.cards)
        return self
    
    def deal_card():
        return self._deal(1)[0]
        
    
    def deal_hand(num):
        return self._deal(num)

