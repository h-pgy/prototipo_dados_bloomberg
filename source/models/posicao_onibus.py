from source.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class PosicaoOnibus(BaseModel):
    __tablename__ = "posicoes_onibus"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    latitude: Mapped[float] = mapped_column(Float)
    longitude: Mapped[float] = mapped_column(Float)
    data_hora: Mapped[datetime] = mapped_column(DateTime)
    onibus_id: Mapped[int] = mapped_column(ForeignKey("onibus.id"))

    onibus: Mapped["Onibus"] = relationship(back_populates="posicoes")
