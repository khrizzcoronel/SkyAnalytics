## Why
Entrenar modelos en aislamiento provoca modelos in-reproducibles. Necesitamos registrar cada corrida experimental y controlar qué modelos llegan a Producción (MAPE <= 15%).

## What Changes
- `backend/src/tactical/mlops_registry.py`: Script en Python simulando un Registry de Modelos.

## Capabilities
- `mlops-registry`: Control de versiones y promoción de modelos de Machine Learning.
