from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine
from alembic.config import Config


def get_db() -> Session:
    alembic_cfg = Config("alembic.ini")
    url = alembic_cfg.get_main_option("sqlalchemy.url")
    engine = create_engine(url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    return db
