import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.task_model import Base, Task
from app.services.task_service import TaskService

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def test_create_task():
    db = TestingSessionLocal()
    service = TaskService(db)
    task = service.create_task(title="Test Task", description="Test Description")
    assert task.id is not None
    db.close()
