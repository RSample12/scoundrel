import uuid
from .deck import Deck
from .player import Player

class Game:
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.deck = Deck()
        self.player = Player()
        self.current_room = []
        self.discard_pile = []
        self.avoided_previous_room = False
        self.cards_chosen_this_room = 0
        self.initialize_room()
        
    def initialize_room(self):
        """Start with a fresh room of 4 cards"""
        self.current_room = []
        while len(self.current_room) < 4 and self.deck.cards_remaining() > 0:
            self.current_room.append(self.deck.draw_card())
        self.cards_chosen_this_room = 0
        self.player.used_potion_this_turn = False
            
    def select_card(self, index):
        """Select a card from the current room"""
        if index < 0 or index >= len(self.current_room):
            raise ValueError("Invalid card index")
            
        card = self.current_room.pop(index)
        self.cards_chosen_this_room += 1
        card_type = card.get_card_type()
        
        if card_type == "weapon":
            self.handle_weapon(card)
        elif card_type == "potion":
            self.handle_potion(card)
        elif card_type == "monster":
            self.handle_monster(card)
            
        # Check if we need to draw a new room (after 3 cards)
        if self.cards_chosen_this_room >= 3:
            # If there's a card left in the room, keep it
            remaining_card = self.current_room[0] if len(self.current_room) == 1 else None
            self.current_room = []
            if remaining_card:
                self.current_room.append(remaining_card)
                
            # Draw new cards
            while len(self.current_room) < 4 and self.deck.cards_remaining() > 0:
                self.current_room.append(self.deck.draw_card())
                
            # Reset room state
            self.cards_chosen_this_room = 0
            self.player.used_potion_this_turn = False
            self.avoided_previous_room = False
                
    def handle_weapon(self, card):
        """Handle equipping a weapon"""
        # Discard old weapon if exists
        if self.player.equipped_weapon:
            self.discard_pile.append(self.player.equipped_weapon)
            # Discard monsters slain by old weapon
            for monster in self.player.slain_monsters:
                self.discard_pile.append(monster)
                
        self.player.equip_weapon(card)
        
    def handle_potion(self, card):
        """Handle using a potion"""
        if self.player.use_potion(card):
            self.discard_pile.append(card)
        
    def handle_monster(self, card):
        """Handle fighting a monster"""
        damage = self.player.fight_monster(card)
        self.player.take_damage(damage)
        if self.player.equipped_weapon:
            # If fought with weapon, add to monster stack
            if damage < card.get_value():
                self.player.slain_monsters.append(card)
            else:
                # If fought barehanded or weapon couldn't be used
                self.discard_pile.append(card)
        else:
            # If fought barehanded
            self.discard_pile.append(card)
        
    def avoid_room(self):
        """Avoid the current room"""
        if self.avoided_previous_room:
            raise ValueError("Cannot avoid two rooms in a row")
            
        # Place all room cards at bottom of deck
        self.deck.place_at_bottom(self.current_room)
        self.current_room = []
        
        # Draw new room
        while len(self.current_room) < 4 and self.deck.cards_remaining() > 0:
            self.current_room.append(self.deck.draw_card())
            
        self.avoided_previous_room = True
        self.cards_chosen_this_room = 0
        self.player.used_potion_this_turn = False
        
    def get_state(self):
        """Get the current game state"""
        return {
            "health": self.player.health,
            "max_health": self.player.max_health,
            "equipped_weapon": self.player.equipped_weapon.to_dict() if self.player.equipped_weapon else None,
            "slain_monsters": [m.to_dict() for m in self.player.slain_monsters],
            "current_room": [c.to_dict() for c in self.current_room],
            "cards_remaining": self.deck.cards_remaining(),
            "avoided_previous_room": self.avoided_previous_room,
            "used_potion_this_turn": self.player.used_potion_this_turn,
            "cards_chosen_this_room": self.cards_chosen_this_room,
            "game_over": not self.player.is_alive() or (self.deck.cards_remaining() == 0 and len(self.current_room) == 0),
            "score": self.calculate_score()
        }
        
    def calculate_score(self):
        """Calculate the current game score"""
        if not self.player.is_alive():
            # If player died, calculate negative score
            remaining_monsters = [c for c in self.deck.cards if c.get_card_type() == "monster"]
            monster_values = sum(m.get_value() for m in remaining_monsters)
            return -1 * (abs(self.player.health) + monster_values)
        elif self.deck.cards_remaining() == 0 and len(self.current_room) == 0:
            # If survived, score is remaining health
            # Plus potion value if last card was potion and health is max
            if (self.discard_pile and 
                self.discard_pile[-1].get_card_type() == "potion" and 
                self.player.health == self.player.max_health):
                return self.player.health + self.discard_pile[-1].get_value()
            return self.player.health
        return self.player.health  # Current score during game