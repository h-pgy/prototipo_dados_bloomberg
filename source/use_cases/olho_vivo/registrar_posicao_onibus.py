from source.connectors.api_olho_vivo import APIOlhoVivoClient
from source.models.onibus import Onibus
from source.models.posicao_onibus import PosicaoOnibus
from source.schemas.olho_vivo import PosicaoOnibusSchema as PosicaoOnibusAPISchema
from source.schemas.db import OnibusSchema, PosicaoOnibusSchema
from sqlalchemy.orm import Session

from .criar_onibus import criar_onibus


def registrar_posicao_onibus(db:Session, posicao_api:PosicaoOnibusAPISchema)->PosicaoOnibus:

    onibus_schema = OnibusSchema(
        id_onibus = posicao_api.id_onibus,
        id_linha = posicao_api.id_linha
    )

    onibus = criar_onibus(db, onibus_schema)

    posicao_onibus_schema = PosicaoOnibusSchema(
        latitude = posicao_api.posit_x,
        longitude = posicao_api.posit_y,
        data_hora = posicao_api.dtime_extracao,
        id_onibus = onibus.id_onibus
    )

    dados_onibus = posicao_onibus_schema.model_dump()
    dados_onibus['onibus'] = onibus
    del dados_onibus['id_onibus']


    posicao_onibus = PosicaoOnibus(
        **dados_onibus
    )

    db.add(posicao_onibus)
    db.commit()
    db.refresh(posicao_onibus)

    return posicao_onibus
