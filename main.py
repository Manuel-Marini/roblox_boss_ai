from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class PlayerData(BaseModel):
    bossName: str
    playerJumps: int
    playerDodges: int
    favoriteAttack: str

@app.get("/")
def home():
    return {"status": "Cloud AI Server läuft online!"}

@app.post("/api/boss-decision")
def boss_decision(data: PlayerData):
    print(f"Roblox Anfrage: Jumps={data.playerJumps}, Dodges={data.playerDodges}, Skill={data.favoriteAttack}")
    
    if data.playerJumps > 10:
        counter_move = "AntiAirSigmaRay"
    elif data.playerDodges > 5:
        counter_move = "PredictionBlast"
    elif data.favoriteAttack == "ToiletAttack":
        counter_move = "SkibidiShield"
    else:
        counter_move = "DefaultGroundSmash"
        
    return {
        "status": "success",
        "counterMove": counter_move,
        "aiConfidence": random.randint(85, 99)
    }
