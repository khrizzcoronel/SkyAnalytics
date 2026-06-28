import re
from typing import Optional
from pydantic import BaseModel, EmailStr, field_validator
import uuid

# Blacklist básica (se puede extender o leer de un archivo)
BLACKLISTED_DOMAINS = {"gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "live.com", "aol.com"}

def pydantic_default_uuid():
    return str(uuid.uuid4())

class Tenant(BaseModel):
    id: str = pydantic_default_uuid() # We'll set it properly
    company_name: str
    contact_email: EmailStr
    country: Optional[str] = None
    
    @field_validator('contact_email')
    def validate_corporate_email(cls, v: str) -> str:
        # Extraer el dominio del correo
        domain = v.split('@')[-1].lower()
        if domain in BLACKLISTED_DOMAINS:
            raise ValueError(f"Por favor utiliza un correo corporativo válido. El dominio '{domain}' no está permitido.")
        return v

def pydantic_default_uuid():
    return str(uuid.uuid4())

# Arreglo para que Pydantic maneje el default
Tenant.model_fields['id'].default_factory = lambda: str(uuid.uuid4())
