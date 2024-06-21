from typing import List
from sqlalchemy.orm import Session
from app.models.task_model import Task
from app.repositories.task_repository import TaskRepository

class TaskService:

    def __init__(self, db: Session):
        self.task_repository = TaskRepository(db)

    def create_task(self, title: str, description: str) -> Task:
        task = Task(title=title, description=description)
        return self.task_repository.create_task(task)

    def get_task_by_id(self, task_id: int) -> Task:
        return self.task_repository.get_task_by_id(task_id)

    def update_task(self, task_id: int, title: str, description: str, status: str) -> Task:
        task = self.get_task_by_id(task_id)
        if task:
            updated_task = {"title": title, "description": description, "status": status}
            return self.task_repository.update_task(task, updated_task)
        return None

    def delete_task(self, task_id: int):
        return self.task_repository.delete_task(task_id)

    def list_tasks(self) -> List[Task]:
        return self.task_repository.list_tasks()
