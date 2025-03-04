from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from game_logic.game import Game

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store active games
games = {}

class GameAction(BaseModel):
    game_id: str
    action_type: str
    card_index: int = None

@app.post("/new-game")
async def create_game():
    game = Game()
    game_id = game.id
    games[game_id] = game
    return {"game_id": game_id, "state": game.get_state()}

@app.post("/action")
async def perform_action(action: GameAction):
    if action.game_id not in games:
        raise HTTPException(status_code=404, detail="Game not found")
    
    game = games[action.game_id]
    
    if action.action_type == "select_card":
        game.select_card(action.card_index)
    elif action.action_type == "avoid_room":
        game.avoid_room()
    
    return {"state": game.get_state()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)