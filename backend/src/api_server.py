import time
from fastapi import FastAPI, Depends, HTTPException, Header
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="SkyAnalytics API Gateway", version="1.0.0")

# --- In-Memory Stores (Simulating Redis) ---
API_USAGE = {}
FAKE_REDIS_CACHE = {}

# Configuraciones
RATE_LIMIT_MAX = 1000

# --- Dependencies ---
async def verify_api_key(x_api_key: str = Header(None)):
    if not x_api_key:
        raise HTTPException(status_code=401, detail="Missing x-api-key header")
    
    # Check Rate Limit
    usage = API_USAGE.get(x_api_key, 0)
    if usage >= RATE_LIMIT_MAX:
        # Devolvemos un error 429 como dice la regla
        raise HTTPException(
            status_code=429, 
            detail="Monthly quota exceeded. Upgrade to Pro plan."
        )
    
    # Incrementamos el uso
    API_USAGE[x_api_key] = usage + 1
    return x_api_key

# --- Modelos ---
class FlightResponse(BaseModel):
    flight_id: str
    status: str
    prediction_delay_minutes: int
    _cached: bool = False

# --- Endpoints ---
@app.get("/v1/flights/{flight_id}")
async def get_flight(flight_id: str, api_key: str = Depends(verify_api_key)):
    # 1. Checar Caché
    cache_key = f"flight_{flight_id}"
    if cache_key in FAKE_REDIS_CACHE:
        data = FAKE_REDIS_CACHE[cache_key]
        return {
            "flight_id": data["flight_id"],
            "status": data["status"],
            "prediction_delay_minutes": data["prediction_delay_minutes"],
            "_cached": True,
            "rate_limit_remaining": RATE_LIMIT_MAX - API_USAGE[api_key]
        }
    
    # 2. Simulación de procesamiento pesado (Base de Datos + ML)
    # En la realidad esto invocaría a MonetDB y al modelo XGBoost.
    time.sleep(0.1) # Simulando 100ms de procesamiento de backend
    
    response_data = {
        "flight_id": flight_id,
        "status": "ON_TIME",
        "prediction_delay_minutes": 5
    }
    
    # 3. Guardar en Caché
    FAKE_REDIS_CACHE[cache_key] = response_data
    
    return {
        **response_data,
        "_cached": False,
        "rate_limit_remaining": RATE_LIMIT_MAX - API_USAGE[api_key]
    }

if __name__ == "__main__":
    import uvicorn
    # Correr servidor en modo debug local
    uvicorn.run(app, host="0.0.0.0", port=8000)
