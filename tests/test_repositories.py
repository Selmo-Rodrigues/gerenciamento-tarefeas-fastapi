import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.task_model import Base, Task
from app.repositories.task_repository import TaskRepository

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def test_create_task():
    db = TestingSessionLocal()
    repository = TaskRepository(db)
    task = Task(title="Test Task", description="Test Description")
    repository.create_task(task)
    assert task.id is not None
    db.close()
