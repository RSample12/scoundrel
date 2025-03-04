# main.py
import tkinter as tk
from ui import ScoundrelUI

def main():
    """Main function to run the game with UI"""
    root = tk.Tk()
    app = ScoundrelUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()