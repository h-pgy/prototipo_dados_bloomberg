from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from source.config import DB_STRING
from source.models.base import BaseModel

from source.models.onibus import Onibus
from source.models.posicao_onibus import PosicaoOnibus


def get_engine():
    engine = create_engine(DB_STRING, echo=False, future=True)
    return engine

def create_all_tables(engine) -> None:
    """Cria todas as tabelas definidas nos modelos."""
    BaseModel.metadata.create_all(engine)
    print("Tabelas criadas com sucesso.")


if __name__ == "__main__":

    engine = get_engine()
    create_all_tables(engine)