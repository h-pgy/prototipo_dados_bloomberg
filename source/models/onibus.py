from source.models.base import BaseModel
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class Onibus(BaseModel):
    __tablename__ = "onibus"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    id_onibus: Mapped[int] = mapped_column(Integer, unique=True, nullable=False)
    id_linha: Mapped[str] = mapped_column(String(20), nullable=False)

    posicoes: Mapped[list["PosicaoOnibus"]] = relationship(back_populates="onibus", cascade="all, delete-orphan")