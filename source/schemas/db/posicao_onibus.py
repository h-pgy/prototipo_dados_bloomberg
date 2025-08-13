from pydantic import BaseModel, Field
from datetime import datetime
from .onibus import Onibus as OnibusSchema

class PosicaoOnibus(BaseModel):

    latitude: float = Field(..., description="Latitude do ônibus")
    longitude: float = Field(..., description="Longitude do ônibus")
    data_hora: datetime = Field(..., description="Data e hora da posição")
    id_onibus: int = Field(..., description="Identificador do ônibus")