from source.use_cases.olho_vivo.registrar_posicao_onibus import registrar_posicao_onibus
from source.use_cases.olho_vivo.parse_posicao_onibus_api import parse_posicao_onibus_api

from source.connectors.api_olho_vivo import APIOlhoVivoClient
from sqlalchemy.orm import Session
from source.models.posicao_onibus import PosicaoOnibus

from typing import List

def registrar_todas_posicoes_onibus(db:Session)->List[PosicaoOnibus]:

    client = APIOlhoVivoClient()
    posicoes_data = client.get_posicoes_onibus()

    posicoes_api = parse_posicao_onibus_api(posicoes_data)

    posicoes_registradas = []
    for posicao_api in posicoes_api:
        posicao_registrada = registrar_posicao_onibus(db, posicao_api)
        posicoes_registradas.append(posicao_registrada)

    return posicoes_registradas


if __name__ == "__main__":

    from source.models.get_db_session import get_db_session
    with get_db_session() as db:
        posicoes = registrar_todas_posicoes_onibus(db)
        print(f"Total de posições registradas: {len(posicoes)}")