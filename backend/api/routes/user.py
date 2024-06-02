# backend/api/routes/user.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.api.models.user import User
from backend.database.session import get_db

router = APIRouter()

@router.post("/users/post")
async def create_user(user: User, db: Session = Depends(get_db)):
    db.add(user)
    db.commit()
    return {"message": "User created successfully"}

@router.get("/users/get")
async def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users

@router.get("/users/get/{user_id}")
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

@router.put("/users/put/{user_id}")
async def update_user(user_id: int, user_data: dict, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id)
    if user.first():
        user.update(user_data)
        db.commit()
        return {"message": "User updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/delete/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id)
    if user.first():
        user.delete()
        db.commit()
        return {"message": "User deleted successfully"}