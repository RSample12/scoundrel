class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
    def get_card_type(self):
        if self.suit in ["clubs", "spades"]:
            return "monster"
        elif self.suit == "diamonds":
            return "weapon"
        elif self.suit == "hearts":
            return "potion"
            
    def get_value(self):
        """Get the true value of the card, accounting for face cards and aces"""
        if self.get_card_type() == "monster":
            if self.value == 1:  # Ace
                return 14
            elif self.value == 11:  # Jack
                return 11
            elif self.value == 12:  # Queen
                return 12
            elif self.value == 13:  # King
                return 13
        return self.value
            
    def to_dict(self):
        return {
            "suit": self.suit,
            "value": self.value,
            "type": self.get_card_type(),
            "true_value": self.get_value()
        }