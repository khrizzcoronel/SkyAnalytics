## Context

SkyAnalytics necesita exponer los datos de los vuelos (`CU-O02`) a los sistemas M2M (Máquina a Máquina) de los clientes corporativos. El volumen de estas transacciones requerirá tiempos de respuesta estrictos (<50ms) y defensas perimetrales contra abuso (DDoS o consumo excesivo de cuota Freemium).

## Goals / Non-Goals

**Goals:**
- Montar un API Server en Python utilizando `FastAPI` por su asincronismo y velocidad.
- Implementar un interceptor (Middleware o Dependency Injection) para validar el header `x-api-key`.
- Construir lógica de Rate Limiting simulada en memoria (Diccionario) que devuelva HTTP 429 si se excede.
- Construir lógica de Caché simulada en memoria que intercepte peticiones a `GET /v1/flights/{id}`.

**Non-Goals:**
- Instalar e implementar Redis real o una base de datos real en este paso (se usará In-Memory LRU para demostrar la arquitectura sin incurrir en complejidad de infraestructura en este sprint).
- Entrenamiento del modelo ML real (solo devolveremos una predicción mockeada).

## Decisions

- **Framework FastAPI:** Ideal para APIs de alto rendimiento en Python. Su soporte nativo para `async/await` es fundamental para alcanzar el SLA de 50ms (RNF-O02-001).
- **Dependency Injection para Seguridad:** En FastAPI, las cabeceras como `x-api-key` y los límites de cuota se manejarán elegantemente inyectando una función `Depends()` en las rutas, manteniendo el código del controlador limpio.
- **In-Memory Store:** Para simular Redis y la Base de Datos, se utilizarán diccionarios globales de Python. Esto garantiza que la prueba se pueda ejecutar y probar instantáneamente.

## Risks / Trade-offs

- **Diccionarios en Memoria vs Redis Real:** En un entorno multi-proceso (Gunicorn/Uvicorn workers), los diccionarios en memoria no se comparten.
  - *Mitigación:* Se asume como un Trade-off temporal (Stub) para probar la lógica. En la fase de Despliegue, se reemplazará por un cliente asíncrono de Redis (`aioredis`).
