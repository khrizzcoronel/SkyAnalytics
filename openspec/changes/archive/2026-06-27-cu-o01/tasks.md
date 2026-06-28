## 1. Setup Base Operativo (Python)

## 1. Setup Base Operativo (Python)

- [x] 1.1 Crear la estructura del módulo operativo: `backend/src/services` y configurar un entorno virtual (venv) con dependencias iniciales (`pip install pydantic passlib`).
- [x] 1.2 Configurar el modelo de dominio `Tenant` en Python usando Pydantic para la validación estricta de dominios corporativos.

## 2. Lógica de Negocio

- [x] 2.1 Implementar el método `validate_corporate_email` que rechace dominios de una blacklist quemada en código (ej. gmail.com, hotmail.com).
- [x] 2.2 Implementar la clase `ApiKeyService` con el método `generate_key_pair` utilizando la librería nativa `secrets`.
- [x] 2.3 Implementar el algoritmo de hashing (SHA-256) en `ApiKeyService` para preparar el valor que se guardará en la DB.

## 3. Ensamblaje del Caso de Uso

- [x] 3.1 Crear el módulo orquestador `tenant_onboarding.py` que recibe el payload, ejecuta la validación del correo, y si pasa, llama a la generación de llaves.
- [x] 3.2 Retornar un diccionario estructurado (simulando la respuesta JSON) asegurando que el hash y la llave plana están disponibles donde corresponden (según las Reglas de Negocio).
