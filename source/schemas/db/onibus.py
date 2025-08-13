from pydantic import BaseModel, Field

class Onibus(BaseModel):

    id_onibus: int = Field(..., description="ID do ônibus")
    id_linha: str = Field(..., description="ID da linha do ônibus")