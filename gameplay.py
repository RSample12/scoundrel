# gameplay.py
from objects import CardType, Deck, Player, Room, DiscardPile

class GameEngine:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.room = Room()
        self.discard = DiscardPile()
        self.last_avoided = False
        self.game_over = False
        
    def initialize_game(self):
        """Initialize the game"""
        self.deck.build()
        self.deck.shuffle()
        self.player = Player()
        self.room = Room()
        self.discard = DiscardPile()
        self.last_avoided = False
        self.game_over = False
        self.draw_room()
        
    def draw_room(self):
        """Draw cards from the deck to fill the room"""
        # If there's a card from the previous room, keep it
        cards_needed = 4 - self.room.size()
        
        for _ in range(cards_needed):
            card = self.deck.draw()
            if card:
                self.room.add_card(card)
            else:
                # No more cards in the deck
                break
                
    def avoid_room(self):
        """Avoid the current room"""
        if self.last_avoided:
            return False  # Cannot avoid two rooms in a row
            
        # Add all cards to the bottom of the deck
        cards = self.room.get_cards()
        self.deck.add_to_bottom(cards)
        self.room.clear()
        self.last_avoided = True
        self.draw_room()
        return True
        
    def enter_room(self):
        """Enter the current room"""
        self.last_avoided = False
        return True
        
    def choose_card(self, index):
        """Choose a card from the room"""
        if index < 0 or index >= self.room.size():
            return False, "Invalid card index"
            
        card = self.room.remove_card(index)
        
        if card.type == CardType.WEAPON:
            # Discard current weapon and monsters if any
            if self.player.equipped_weapon:
                self.discard.add_card(self.player.equipped_weapon)
                self.discard.add_cards(self.player.monster_stack)
            
            # Equip new weapon
            self.player.equip_weapon(card)
            return True, f"Equipped {card} as your weapon"
            
        elif card.type == CardType.POTION:
            # Check if we've already used a potion this turn
            for discarded in self.discard.cards:
                if discarded.type == CardType.POTION and self._is_same_turn():
                    self.discard.add_card(card)
                    return True, f"Discarded {card} - only one potion per turn"
                    
            # Use the potion
            healing = self.player.drink_potion(card)
            self.discard.add_card(card)
            return True, f"Used {card} and healed for {healing}. Current health: {self.player.health}"
            
        elif card.type == CardType.MONSTER:
            # Check if we can use the equipped weapon
            weapon_usable = False
            if self.player.equipped_weapon:
                if not self.player.monster_stack or card.get_damage() <= self.player.get_last_monster_value():
                    weapon_usable = True
                    
            if weapon_usable:
                # Fight with weapon
                monster_damage = card.get_damage()
                weapon_damage = self.player.get_weapon_value()
                damage_taken = max(0, monster_damage - weapon_damage)
                
                self.player.take_damage(damage_taken)
                self.player.add_monster_to_weapon(card)
                
                result = f"Fought {card} with your weapon. "
                if damage_taken > 0:
                    result += f"Took {damage_taken} damage. "
                else:
                    result += "Took no damage. "
                result += f"Current health: {self.player.health}"
                
                # Check if player died
                if not self.player.is_alive():
                    self.game_over = True
                    result += "\nYou have died!"
                
                return True, result
            else:
                # Fight barehanded
                damage_taken = card.get_damage()
                self.player.take_damage(damage_taken)
                self.discard.add_card(card)
                
                result = f"Fought {card} barehanded. Took {damage_taken} damage. Current health: {self.player.health}"
                
                # Check if player died
                if not self.player.is_alive():
                    self.game_over = True
                    result += "\nYou have died!"
                
                return True, result
        
        return False, "Unknown card type"
        
    def _is_same_turn(self):
        """Helper method to determine if we're in the same turn (using card count as a proxy)"""
        # In a real implementation, we'd track turns more explicitly
        # Here we simplify by assuming cards chosen in the same room = same turn
        return True
        
    def check_game_state(self):
        """Check if the game is over"""
        if not self.player.is_alive():
            # Player is dead
            score = self._calculate_dead_score()
            return True, f"Game Over! You died. Final Score: {score}"
            
        if self.deck.cards_remaining() == 0 and self.room.size() == 0:
            # Player has completed the dungeon
            score = self._calculate_victory_score()
            return True, f"Congratulations! You completed the dungeon. Final Score: {score}"
            
        # Game continues
        return False, ""
        
    def _calculate_dead_score(self):
        """Calculate score when player dies"""
        # Find all remaining monsters in the deck
        remaining_monster_value = 0
        for card in self.deck.cards:
            if card.type == CardType.MONSTER:
                remaining_monster_value += card.get_damage()
                
        # Add remaining monsters in the room
        for card in self.room.get_cards():
            if card.type == CardType.MONSTER:
                remaining_monster_value += card.get_damage()
                
        # Calculate negative score
        return -(abs(self.player.health) + remaining_monster_value)
        
    def _calculate_victory_score(self):
        """Calculate score when player completes the dungeon"""
        # Check if the last card was a health potion
        if self.discard.cards and self.discard.cards[-1].type == CardType.POTION and self.player.health == 20:
            # Perfect score + potion value
            return 20 + self.discard.cards[-1].get_damage()
        else:
            # Just the remaining health
            return self.player.health
            
    def get_room_info(self):
        """Get information about the current room"""
        cards_info = []
        for i, card in enumerate(self.room.get_cards()):
            cards_info.append(f"{i+1}: {card}")
        return cards_info
        
    def get_player_info(self):
        """Get information about the player"""
        info = [f"Health: {self.player.health}/{self.player.max_health}"]
        
        if self.player.equipped_weapon:
            weapon_info = f"Equipped weapon: {self.player.equipped_weapon}"
            if self.player.monster_stack:
                monster_values = [str(m.get_damage()) for m in self.player.monster_stack]
                weapon_info += f" (slain monsters: {', '.join(monster_values)})"
            info.append(weapon_info)
        else:
            info.append("No weapon equipped")
            
        return info
        
    def get_game_info(self):
        """Get general game information"""
        return [
            f"Cards remaining in dungeon: {self.deck.cards_remaining()}",
            f"Cards in discard pile: {len(self.discard.cards)}"
        ]