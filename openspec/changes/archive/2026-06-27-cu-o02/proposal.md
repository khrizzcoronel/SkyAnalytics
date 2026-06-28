## Why

Los clientes B2B (Aerolíneas y Agencias) necesitan una API para consultar el estado y predicciones de los vuelos en tiempo real. Sin embargo, exponer una API sin controles (Rate Limiting) y sin Caché provocará que el Módulo Operativo y la Base de Datos colapsen bajo picos de tráfico masivo (miles de peticiones por segundo). 

## What Changes

- **Motor API de Alto Rendimiento**: Configuración de un servidor FastAPI en Python que responda peticiones JSON ultra-rápidas.
- **Middleware de Seguridad (Rate Limiting)**: Implementación de un control de cuotas que devuelva HTTP 429 si un Tenant excede su Soft Limit (simulando 1000 requests/hr).
- **Caché en Memoria**: Para evitar conectar a la base de datos en cada consulta idéntica, implementaremos un sistema de caché que almacene la respuesta (simulando Redis en un diccionario para la prueba inicial).

## Capabilities

### New Capabilities
- `flight-api-service`: Microservicio en FastAPI para consultas de vuelo (`/v1/flights/{id}`).
- `rate-limiter-middleware`: Componente interceptor para controlar las cuotas por `API_KEY`.
- `api-cache-layer`: Lógica de retención de respuestas para reducir latencia (<50ms).

### Modified Capabilities
- 

## Impact

- **Backend (Python)**: Agregaremos `FastAPI` y `Uvicorn` a los requerimientos y montaremos el servidor.
- **Rendimiento**: El tiempo de respuesta para llamadas cacheadas bajará a fracciones de milisegundo.
- **Seguridad Perimetral**: Los clientes abusivos serán bloqueados automáticamente.
