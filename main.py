from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CombatData(BaseModel):
    bossName: str = ""
    playerJumps: int = 0
    playerDodges: int = 0
    favoriteAttack: str = ""

class BuildData(BaseModel):
    prompt: str = ""

@app.get("/")
def read_root():
    return {"status": "AI Server is running!"}

# Endpunkt 1: Boss-Entscheidungen
@app.post("/api/boss-decision")
def boss_decision(data: CombatData):
    if data.playerJumps > 10:
        return {"counterMove": "AntiAirSigmaRay"}
    elif data.playerDodges > 5:
        return {"counterMove": "AreaOfEffectExplosion"}
    else:
        return {"counterMove": "DefaultGroundSmash"}

# Endpunkt 2: Bau-Befehle für Objekte
@app.post("/api/build-command")
def build_command(data: BuildData):
    text = data.prompt.lower()
    
    if "wand" in text or "mauer" in text:
        return {
            "shape": "Block",
            "size": [12, 6, 2],
            "color": [255, 0, 0],    # Rot
            "position": [0, 3, -10]
        }
    elif "turm" in text:
        return {
            "shape": "Block",
            "size": [6, 20, 6],
            "color": [100, 100, 100], # Grau
            "position": [5, 10, -15]
        }
    else:
        return {
            "shape": "Block",
            "size": [4, 4, 4],
            "color": [0, 255, 0],   # Grün
            "position": [0, 2, -5]
        }
