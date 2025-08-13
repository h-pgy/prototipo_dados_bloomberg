from source.models.onibus import Onibus
from source.schemas.db import OnibusSchema
from sqlalchemy import select
from sqlalchemy.orm import Session

def criar_onibus(db:Session, onibus_data:OnibusSchema)->Onibus:
    
    onibus_exists = select(Onibus).where(Onibus.id_onibus == onibus_data.id_onibus)
    instance = db.scalar(onibus_exists)

    if instance:
        return instance

    novo_onibus = Onibus(
        id_onibus = onibus_data.id_onibus,
        id_linha = onibus_data.id_linha
    )
    db.add(novo_onibus)
    db.commit()
    db.refresh(novo_onibus)

    print('Ônibus criado:', novo_onibus.id_onibus)

    return novo_onibus