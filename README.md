Scoundrel Card Game:
based on the Single Player Rogue-like Card Game by Zach Gage and Kurt Bieg

```
scoundrel/
├── backend/               # Python backend
│   ├── app.py             # FastAPI main file
│   ├── game_logic/        # Game logic modules
│   │   ├── __init__.py
│   │   ├── card.py        # Card class definitions
│   │   ├── deck.py        # Deck management
│   │   ├── game.py        # Game state and rules
│   │   └── player.py      # Player state
│   ├── requirements.txt   # Python dependencies
│   └── Dockerfile         # For containerization
└── frontend/              # React Native frontend
    ├── App.js             # Main app component
    ├── app.json           # App configuration
    ├── assets/            # Images, fonts, etc.
    │   └── cards/         # Card images
    ├── babel.config.js
    ├── components/        # React components
    │   ├── Card.js        # Card component
    │   ├── Deck.js        # Deck visualization
    │   ├── GameBoard.js   # Main game board
    │   ├── HealthBar.js   # Player health display
    │   ├── Room.js        # Room of 4 cards
    │   └── Weapon.js      # Equipped weapon display
    ├── contexts/
    │   └── GameContext.js # Game state management
    ├── package.json
    ├── screens/           # App screens
    │   ├── GameScreen.js  # Main gameplay screen
    │   ├── HomeScreen.js  # Start screen
    │   └── RulesScreen.js # Game rules
    └── services/
        └── api.js         # API communication
```
