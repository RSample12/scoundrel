# ui.py
import tkinter as tk
from tkinter import messagebox, scrolledtext
from gameplay import GameEngine

class ScoundrelUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Scoundrel - A Rogue-like Card Game")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Setup game engine
        self.game = GameEngine()
        
        # UI colors
        self.bg_color = "#2C3E50"  # Dark blue
        self.text_color = "#ECF0F1"  # White
        self.button_color = "#3498DB"  # Light blue
        self.button_active_color = "#2980B9"  # Darker blue
        self.card_colors = {
            "CLUBS": "#95A5A6",     # Gray
            "SPADES": "#34495E",    # Dark gray
            "DIAMONDS": "#E74C3C",  # Red
            "HEARTS": "#27AE60"     # Green
        }
        
        # Configure root
        self.root.configure(bg=self.bg_color)
        
        # Create UI elements
        self.create_ui()
        
        # Start the game
        self.game.initialize_game()
        self.update_ui()
        
    def create_ui(self):
        """Create the main UI elements"""
        # Main frame
        self.main_frame = tk.Frame(self.root, bg=self.bg_color)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Title
        title_label = tk.Label(
            self.main_frame, 
            text="SCOUNDREL", 
            font=("Arial", 24, "bold"), 
            fg=self.text_color, 
            bg=self.bg_color
        )
        title_label.pack(pady=(0, 10))
        
        # Info frame (left side)
        self.info_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.info_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False, padx=(0, 10))
        
        # Player info
        self.player_frame = self.create_info_section(self.info_frame, "PLAYER")
        self.health_label = tk.Label(
            self.player_frame, 
            text="Health: 20/20", 
            font=("Arial", 12), 
            fg=self.text_color, 
            bg=self.bg_color,
            anchor="w"
        )
        self.health_label.pack(fill=tk.X, pady=2)
        
        self.weapon_label = tk.Label(
            self.player_frame, 
            text="Weapon: None", 
            font=("Arial", 12), 
            fg=self.text_color, 
            bg=self.bg_color,
            anchor="w"
        )
        self.weapon_label.pack(fill=tk.X, pady=2)
        
        self.monsters_label = tk.Label(
            self.player_frame, 
            text="Monsters slain: None", 
            font=("Arial", 12), 
            fg=self.text_color, 
            bg=self.bg_color,
            anchor="w"
        )
        self.monsters_label.pack(fill=tk.X, pady=2)
        
        # Game info
        self.game_frame = self.create_info_section(self.info_frame, "GAME")
        self.deck_label = tk.Label(
            self.game_frame, 
            text="Cards in dungeon: 44", 
            font=("Arial", 12), 
            fg=self.text_color, 
            bg=self.bg_color,
            anchor="w"
        )
        self.deck_label.pack(fill=tk.X, pady=2)
        
        self.discard_label = tk.Label(
            self.game_frame, 
            text="Cards in discard: 0", 
            font=("Arial", 12), 
            fg=self.text_color, 
            bg=self.bg_color,
            anchor="w"
        )
        self.discard_label.pack(fill=tk.X, pady=2)
        
        # Game log
        self.log_frame = self.create_info_section(self.info_frame, "GAME LOG")
        self.log_text = scrolledtext.ScrolledText(
            self.log_frame, 
            height=10, 
            bg="#34495E", 
            fg=self.text_color,
            font=("Arial", 10)
        )
        self.log_text.pack(fill=tk.BOTH, expand=True, pady=5)
        self.log_text.config(state=tk.DISABLED)
        
        # Room frame (right side)
        self.room_frame = tk.Frame(self.main_frame, bg=self.bg_color)
        self.room_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Room label
        room_label = tk.Label(
            self.room_frame, 
            text="ROOM", 
            font=("Arial", 14, "bold"), 
            fg=self.text_color, 
            bg=self.bg_color
        )
        room_label.pack(pady=(0, 10))
        
        # Cards frame
        self.cards_frame = tk.Frame(self.room_frame, bg=self.bg_color)
        self.cards_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Button frame
        self.button_frame = tk.Frame(self.room_frame, bg=self.bg_color)
        self.button_frame.pack(fill=tk.X, pady=10)
        
        # Avoid room button
        self.avoid_button = tk.Button(
            self.button_frame,
            text="Avoid Room",
            font=("Arial", 12),
            bg=self.button_color,
            fg=self.text_color,
            activebackground=self.button_active_color,
            activeforeground=self.text_color,
            command=self.avoid_room
        )
        self.avoid_button.pack(side=tk.LEFT, padx=5)
        
        # New game button
        self.new_game_button = tk.Button(
            self.button_frame,
            text="New Game",
            font=("Arial", 12),
            bg=self.button_color,
            fg=self.text_color,
            activebackground=self.button_active_color,
            activeforeground=self.text_color,
            command=self.new_game
        )
        self.new_game_button.pack(side=tk.RIGHT, padx=5)
    
    def create_info_section(self, parent, title):
        """Create a labeled section in the info frame"""
        frame = tk.Frame(parent, bg=self.bg_color)
        frame.pack(fill=tk.X, pady=5)
        
        label = tk.Label(
            frame, 
            text=title, 
            font=("Arial", 14, "bold"), 
            fg=self.text_color, 
            bg=self.bg_color
        )
        label.pack(anchor="w")
        
        separator = tk.Frame(frame, height=2, bg=self.button_color)
        separator.pack(fill=tk.X, pady=2)
        
        content_frame = tk.Frame(frame, bg=self.bg_color)
        content_frame.pack(fill=tk.X, pady=5)
        
        return content_frame
    
    def log_message(self, message):
        """Add a message to the game log"""
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
    
    def create_card_button(self, index, card):
        """Create a button representing a card in the room"""
        # Get card value and suit name
        value_map = {1: "A", 11: "J", 12: "Q", 13: "K"}
        display_value = value_map.get(card.value, str(card.value))
        suit_name = card.suit.name
        
        # Card button
        card_frame = tk.Frame(
            self.cards_frame,
            width=120,
            height=180,
            bg="white",
            highlightbackground=self.card_colors.get(suit_name, "black"),
            highlightthickness=2
        )
        
        # Calculate grid position (2x2 grid)
        row = index // 2
        col = index % 2
        card_frame.grid(row=row, column=col, padx=10, pady=10)
        card_frame.grid_propagate(False)
        
        # Card content
        card_type_label = tk.Label(
            card_frame,
            text=card.type.name,
            font=("Arial", 10),
            bg="white"
        )
        card_type_label.pack(pady=(10, 0))
        
        card_value_label = tk.Label(
            card_frame,
            text=f"{display_value} of {suit_name}",
            font=("Arial", 14, "bold"),
            bg="white"
        )
        card_value_label.pack(pady=5)
        
        damage_text = ""
        if card.type.name == "MONSTER":
            damage_text = f"Damage: {card.get_damage()}"
        elif card.type.name == "WEAPON":
            damage_text = f"Power: {card.get_damage()}"
        elif card.type.name == "POTION":
            damage_text = f"Healing: {card.get_damage()}"
            
        damage_label = tk.Label(
            card_frame,
            text=damage_text,
            font=("Arial", 12),
            bg="white"
        )
        damage_label.pack(pady=5)
        
        # Choose button
        choose_button = tk.Button(
            card_frame,
            text="Choose",
            font=("Arial", 10),
            bg=self.button_color,
            fg=self.text_color,
            activebackground=self.button_active_color,
            activeforeground=self.text_color,
            command=lambda i=index: self.choose_card(i)
        )
        choose_button.pack(pady=(15, 0))
        
        return card_frame
    
    def update_ui(self):
        """Update the UI to reflect the game state"""
        # Update player info
        player_info = self.game.get_player_info()
        self.health_label.config(text=player_info[0])
        
        if len(player_info) > 1:
            weapon_text = player_info[1]
            if "Equipped weapon" in weapon_text:
                self.weapon_label.config(text=weapon_text.split("(")[0])
                if "slain monsters" in weapon_text:
                    monsters_text = weapon_text.split("(")[1].replace(")", "")
                    self.monsters_label.config(text=monsters_text)
                else:
                    self.monsters_label.config(text="Monsters slain: None")
            else:
                self.weapon_label.config(text="Weapon: None")
                self.monsters_label.config(text="Monsters slain: None")
        
        # Update game info
        game_info = self.game.get_game_info()
        self.deck_label.config(text=game_info[0])
        self.discard_label.config(text=game_info[1])
        
        # Clear the cards frame
        for widget in self.cards_frame.winfo_children():
            widget.destroy()
        
        # Create new card buttons
        for i, card in enumerate(self.game.room.get_cards()):
            self.create_card_button(i, card)
            
        # Update avoid button state
        self.avoid_button.config(state=tk.NORMAL if not self.game.last_avoided else tk.DISABLED)
        
        # Check if game is over
        game_over, message = self.game.check_game_state()
        if game_over:
            self.log_message(message)
            messagebox.showinfo("Game Over", message)
            # Disable card buttons and avoid button
            self.avoid_button.config(state=tk.DISABLED)
            for widget in self.cards_frame.winfo_children():
                for child in widget.winfo_children():
                    if isinstance(child, tk.Button):
                        child.config(state=tk.DISABLED)
    
    def choose_card(self, index):
        """Handle user choosing a card from the room"""
        success, result = self.game.choose_card(index)
        if success:
            self.log_message(result)
            
            # Check if we need to draw more cards after 3 selections
            cards_chosen = 3 - self.game.room.size()
            if cards_chosen >= 3 or self.game.room.size() <= 1:
                self.game.draw_room()
                self.log_message("Turn complete. New room drawn.")
            
            # Update UI
            self.update_ui()
        else:
            messagebox.showerror("Error", result)
    
    def avoid_room(self):
        """Handle user choosing to avoid the room"""
        if self.game.avoid_room():
            self.log_message("Room avoided. Cards placed at the bottom of the dungeon.")
            self.update_ui()
        else:
            messagebox.showerror("Error", "You cannot avoid two rooms in a row.")
    
    def new_game(self):
        """Start a new game"""
        self.game.initialize_game()
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.log_message("New game started.")
        self.update_ui()


def main():
    root = tk.Tk()
    app = ScoundrelUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()