# objects.py
import random
from enum import Enum, auto

class CardType(Enum):
    MONSTER = auto()
    WEAPON = auto()
    POTION = auto()

class Suit(Enum):
    CLUBS = auto()
    SPADES = auto()
    DIAMONDS = auto()
    HEARTS = auto()

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        
        # Determine card type based on suit
        if suit in [Suit.CLUBS, Suit.SPADES]:
            self.type = CardType.MONSTER
        elif suit == Suit.DIAMONDS:
            self.type = CardType.WEAPON
        elif suit == Suit.HEARTS:
            self.type = CardType.POTION
            
    def get_damage(self):
        """Return the damage value of the card."""
        if self.type == CardType.MONSTER:
            # Face cards and Ace have special values
            if self.value == 1:  # Ace
                return 14
            elif self.value == 11:  # Jack
                return 11
            elif self.value == 12:  # Queen
                return 12
            elif self.value == 13:  # King
                return 13
            else:
                return self.value
        elif self.type == CardType.WEAPON:
            return self.value
        else:  # Potion
            return self.value
            
    def __str__(self):
        value_map = {1: "Ace", 11: "Jack", 12: "Queen", 13: "King"}
        card_value = value_map.get(self.value, str(self.value))
        return f"{card_value} of {self.suit.name}"
    
    def __repr__(self):
        return self.__str__()

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        
    def build(self):
        """Build the Scoundrel deck (standard deck without Red Face Cards and Red Aces)"""
        self.cards = []
        
        # Add Clubs and Spades (monsters) - all values
        for suit in [Suit.CLUBS, Suit.SPADES]:
            for value in range(1, 14):  # 1-13 (Ace to King)
                self.cards.append(Card(value, suit))
                
        # Add Diamonds (weapons) - all values
        for value in range(1, 10):  # 1-9 (Ace to 9)
            self.cards.append(Card(value, Suit.DIAMONDS))
                
        # Add Hearts (potions) - all values
        for value in range(1, 10):  # 1-9 (Ace to 9)
            self.cards.append(Card(value, Suit.HEARTS))
            
        # Remove Red Face Cards and Red Aces as per rules
        self.cards = [card for card in self.cards if not (
            (card.suit == Suit.DIAMONDS or card.suit == Suit.HEARTS) and 
            (card.value == 1 or card.value >= 11)
        )]
            
    def shuffle(self):
        """Shuffle the deck"""
        random.shuffle(self.cards)
        
    def draw(self):
        """Draw a card from the deck"""
        if len(self.cards) > 0:
            return self.cards.pop()
        return None
        
    def add_to_bottom(self, cards):
        """Add cards to the bottom of the deck"""
        if isinstance(cards, list):
            self.cards = cards + self.cards
        else:
            self.cards = [cards] + self.cards
            
    def cards_remaining(self):
        """Return the number of cards remaining in the deck"""
        return len(self.cards)

class Player:
    def __init__(self):
        self.health = 20
        self.max_health = 20
        self.equipped_weapon = None
        self.monster_stack = []  # Monsters slain by current weapon
        
    def equip_weapon(self, weapon):
        """Equip a new weapon and discard the previous one"""
        self.monster_stack = []
        self.equipped_weapon = weapon
        
    def add_monster_to_weapon(self, monster):
        """Add a monster to the equipped weapon's stack"""
        if self.equipped_weapon:
            self.monster_stack.append(monster)
            
    def get_weapon_value(self):
        """Get the current weapon's damage value"""
        if self.equipped_weapon:
            return self.equipped_weapon.get_damage()
        return 0
        
    def get_last_monster_value(self):
        """Get the value of the last monster slain with the current weapon"""
        if self.monster_stack:
            return self.monster_stack[-1].get_damage()
        return 0
        
    def drink_potion(self, potion):
        """Drink a health potion"""
        potion_value = potion.get_damage()
        self.health = min(self.health + potion_value, self.max_health)
        return potion_value
        
    def take_damage(self, damage):
        """Take damage from a monster"""
        self.health -= damage
        
    def is_alive(self):
        """Check if the player is still alive"""
        return self.health > 0

class Room:
    def __init__(self):
        self.cards = []
        
    def add_card(self, card):
        """Add a card to the room"""
        self.cards.append(card)
        
    def remove_card(self, index):
        """Remove a card from the room at the given index"""
        if 0 <= index < len(self.cards):
            return self.cards.pop(index)
        return None
        
    def clear(self):
        """Clear all cards from the room"""
        self.cards = []
        
    def get_cards(self):
        """Get all cards in the room"""
        return self.cards
        
    def size(self):
        """Get the number of cards in the room"""
        return len(self.cards)

class DiscardPile:
    def __init__(self):
        self.cards = []
        
    def add_card(self, card):
        """Add a card to the discard pile"""
        self.cards.append(card)
        
    def add_cards(self, cards):
        """Add multiple cards to the discard pile"""
        self.cards.extend(cards)
        
    def clear(self):
        """Clear all cards from the discard pile"""
        self.cards = []