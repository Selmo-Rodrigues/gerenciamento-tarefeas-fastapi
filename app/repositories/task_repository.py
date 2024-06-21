from sqlalchemy.orm import Session
from app.models.task_model import Task

class TaskRepository:

    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task: Task):
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_task_by_id(self, task_id: int):
        return self.db.query(Task).filter(Task.id == task_id).first()

    def update_task(self, task: Task, updated_task: dict):
        for key, value in updated_task.items():
            setattr(task, key, value)
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self, task_id: int):
        task = self.db.query(Task).filter(Task.id == task_id).first()
        if task:
            self.db.delete(task)
            self.db.commit()
        return task

    def list_tasks(self):
        return self.db.query(Task).all()
