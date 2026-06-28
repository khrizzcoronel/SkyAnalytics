## 1. Setup API y Entorno (Python)

## 1. Setup API y Entorno (Python)

- [x] 1.1 Instalar dependencias necesarias en el venv de Python (`pip install fastapi uvicorn`).
- [x] 1.2 Crear la estructura base del servidor API en `backend/src/api_server.py`.

## 2. Middleware y Dependencias de Seguridad

- [x] 2.1 Crear el mecanismo `verify_api_key` usando `fastapi.Security` o `Header` para interceptar `x-api-key`.
- [x] 2.2 Implementar Rate Limiting (In-Memory `API_USAGE` dict) que evalúe si la key ha sobrepasado las 1000 requests y lance `HTTPException(429)`.

## 3. Caché y Controladores

- [x] 3.1 Implementar Caché In-Memory (`FAKE_REDIS_CACHE`) para almacenar el payload de respuesta de los vuelos.
- [x] 3.2 Desarrollar el endpoint `GET /v1/flights/{flight_id}` que lea de caché, y si no existe, procese la data mockeada, la guarde en caché y la retorne.
