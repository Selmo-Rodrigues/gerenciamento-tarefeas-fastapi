from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.services.task_service import TaskService
from app.database import get_db
from app.models.task_schema import Task, TaskCreate, TaskUpdate
import logging

router = APIRouter()

logging.basicConfig(level=logging.INFO)

@router.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    logging.info(f"Creating task with title: {task.title}")
    task_service = TaskService(db)
    try:
        return task_service.create_task(task.title, task.description)
    except Exception as e:
        logging.error(f"Error creating task: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/tasks/", response_model=List[Task])
def list_tasks(db: Session = Depends(get_db)):
    logging.info("Listing tasks")
    task_service = TaskService(db)
    return task_service.list_tasks()

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, db: Session = Depends(get_db)):
    logging.info(f"Getting task with ID: {task_id}")
    task_service = TaskService(db)
    task = task_service.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task: TaskUpdate, db: Session = Depends(get_db)):
    logging.info(f"Updating task with ID: {task_id}")
    task_service = TaskService(db)
    updated_task = task_service.update_task(task_id, task.title, task.description, task.status)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    logging.info(f"Deleting task with ID: {task_id}")
    task_service = TaskService(db)
    task = task_service.delete_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task
