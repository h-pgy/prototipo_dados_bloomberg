# source/database.py

from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker, Session
from .engine import get_engine

# Cria uma fábrica de sessões ligada ao engine
SessionLocal = sessionmaker(bind=get_engine(), autoflush=False, autocommit=False)

@contextmanager
def get_db_session() -> Session:
    """
    Provedor de sessão para uso com 'with'.
    Fecha a sessão automaticamente no final.
    """
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except:
        db.rollback()
        raise
    finally:
        db.close()
