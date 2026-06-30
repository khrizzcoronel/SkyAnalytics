from typing import Optional
from pydantic import BaseModel, Field

class FlightRecordContract(BaseModel):
    """
    Data Contract para un registro de Vuelo (basado en el esquema BTS).
    Si una fila de Staging no cumple esto formalmente, cuenta como Bad Record.
    """
    fl_date: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$", description="Fecha ISO 8601 YYYY-MM-DD")
    op_unique_carrier: str = Field(..., min_length=2, max_length=3, description="Código de la aerolínea")
    op_carrier_fl_num: Optional[float] = Field(None, description="Número de vuelo (a menudo parseado como float o int)")
    origin: Optional[str] = Field(None, description="Código IATA del aeropuerto de origen")
    dest: Optional[str] = Field(None, description="Código IATA del aeropuerto de destino")
    dep_delay: Optional[float] = Field(None, ge=-120, le=1440, description="Retraso de salida en minutos (debe estar en un rango razonable)")
    distance: Optional[float] = Field(None, gt=0, description="Distancia en millas (debe ser mayor a 0)")
