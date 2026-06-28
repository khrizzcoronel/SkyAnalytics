import secrets
import hashlib
from passlib.hash import pbkdf2_sha256

class ApiKeyService:
    @staticmethod
    def generate_key_pair() -> dict:
        """
        Genera llaves Sandbox (Test) y Producción (Live).
        """
        test_key = f"sk_test_{secrets.token_urlsafe(32)}"
        live_key = f"sk_live_{secrets.token_urlsafe(32)}"
        
        return {
            "test_key": test_key,
            "live_key": live_key
        }
    
    @staticmethod
    def hash_key(api_key: str) -> str:
        """
        Calcula un hash seguro KDF para almacenar en la BD.
        Nunca se debe guardar la live_key en texto plano.
        """
        return pbkdf2_sha256.hash(api_key)
    
    @staticmethod
    def verify_key(plain_key: str, hashed_key: str) -> bool:
        """
        Verifica si la llave en texto plano corresponde al hash.
        """
        return pbkdf2_sha256.verify(plain_key, hashed_key)
