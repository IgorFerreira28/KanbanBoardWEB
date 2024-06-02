# backend/api/routes/task.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.api.models.task import Task
from backend.database.session import get_db

router = APIRouter()

@router.post("/create/")
async def create_task(task_data: dict, db: Session = Depends(get_db)):
    task = Task(**task_data)
    db.add(task)
    db.commit()
    return {"message": "Task created successfully"}

@router.get("/get/")
async def get_tasks(db: Session = Depends(get_db)):
    tasks = db.query(Task).all()
    return tasks

@router.get("/get/{task_id}")
async def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        return task
    raise HTTPException(status_code=404, detail="Task not found")

@router.put("/update/{task_id}")
async def update_task(task_id: int, task_data: dict, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id)
    if task.first():
        task.update(task_data)
        db.commit()
        return {"message": "Task updated successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/delete/{task_id}")
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id)
    if task.first():
        task.delete()
        db.commit()
        return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")