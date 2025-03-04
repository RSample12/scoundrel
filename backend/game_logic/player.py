class Player:
    def __init__(self):
        self.health = 20
        self.max_health = 20
        self.equipped_weapon = None
        self.slain_monsters = []
        self.used_potion_this_turn = False
        
    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        
    def equip_weapon(self, weapon):
        self.equipped_weapon = weapon
        self.slain_monsters = []
        
    def use_potion(self, potion):
        if not self.used_potion_this_turn:
            self.health = min(self.max_health, self.health + potion.get_value())
            self.used_potion_this_turn = True
            return True
        return False
            
    def fight_monster(self, monster):
        monster_value = monster.get_value()
        
        if not self.equipped_weapon:
            # Fighting barehanded
            return monster_value
            
        # Check if weapon can be used against this monster
        if self.slain_monsters and monster_value > self.slain_monsters[-1].get_value():
            # Monster is stronger than last monster slain with this weapon
            return monster_value
            
        # Use weapon
        self.slain_monsters.append(monster)
        damage = max(0, monster_value - self.equipped_weapon.get_value())
        return damage
        
    def is_alive(self):
        return self.health > 0