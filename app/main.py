from fastapi import FastAPI
from app.database import engine, Base
from app.controllers import task_controller
import logging

logging.basicConfig(level=logging.INFO)

# Criação das tabelas
logging.info("Creating all tables...")
Base.metadata.create_all(bind=engine)
logging.info("All tables created")

app = FastAPI()

app.include_router(task_controller.router)
