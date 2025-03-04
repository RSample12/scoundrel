import random
from .card import Card

class Deck:
    def __init__(self):
        self.cards = []
        self.initialize_deck()
        
    def initialize_deck(self):
        suits = ["clubs", "spades", "diamonds", "hearts"]
        values = list(range(2, 11)) + [11, 12, 13, 14]  # 2-10, J, Q, K, A
        
        for suit in suits:
            for value in values:
                # Skip red face cards and red aces as per rules
                if suit in ["hearts", "diamonds"] and value in [11, 12, 13, 14]:
                    continue
                self.cards.append(Card(suit, value))
                
        random.shuffle(self.cards)
        
    def draw_card(self):
        if not self.cards:
            return None
        return self.cards.pop(0)
        
    def cards_remaining(self):
        return len(self.cards)
        
    def place_at_bottom(self, cards):
        self.cards.extend(cards)