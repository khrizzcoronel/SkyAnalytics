from typing import Literal
from pydantic import BaseModel, Field

class FlightRecordContract(BaseModel):
    """
    Data Contract para un registro de Vuelo en Staging.
    Si una fila de Staging no cumple esto, cuenta como Bad Record.
    """
    flight_id: str = Field(..., min_length=2, description="ID único del vuelo (ej. AA123)")
    departure_date: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$", description="Fecha ISO 8601 YYYY-MM-DD")
    airline: str = Field(..., min_length=2, max_length=3)
    status: Literal['ON_TIME', 'DELAYED', 'CANCELLED'] = Field(..., description="Estado oficial")
    monto_pago: float = Field(..., gt=0, description="El pago debe ser mayor a 0")
