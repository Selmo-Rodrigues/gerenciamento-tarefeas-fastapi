from sqlalchemy.orm import declarative_base  # Atualizado
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import logging

logging.basicConfig(level=logging.INFO)

# Obtém o caminho absoluto para o diretório do projeto
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
database_url = f"sqlite:///{os.path.join(project_dir, 'test.db')}"

logging.info(f"Database URL: {database_url}")

engine = create_engine(database_url, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
