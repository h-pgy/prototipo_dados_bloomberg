from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

class PosicaoOnibus(BaseModel):

    id_onibus : int = Field(..., title="ID do ônibus", gt=1000, lt=99999)
    id_linha : str = Field(..., min_length=3, max_length=20, title="ID da linha")
    posit_x : float = Field(..., title="Posição X do ônibus")
    posit_y  : float = Field(..., title="Posição Y do ônibus")
    dtime_extracao : str = Field(..., min_length=1, max_length=20, title="Data e hora da extração")



    @field_validator("posit_x", "posit_y", mode="after")
    @classmethod
    def garantir_float_negativo(cls, v, info):
        if v >= 0:
            raise ValueError(f"O campo '{info.field_name}' deve ser um float negativo")
        return v

    @field_validator('dtime_extracao')
    @classmethod
    def validate_dtime_extracao(cls, value) -> datetime:
        """Valida o horário e converte para o fuso de São Paulo."""

        try:
            dt_utc = datetime.strptime(value, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
            dt_sp = dt_utc.astimezone(ZoneInfo("America/Sao_Paulo"))
        except ValueError:
            raise ValueError("Data e hora devem estar no formato 'YYYY-MM-DDTHH:MM:SSZ'")

        return dt_sp