# backend/api/models/user.py

from sqlalchemy import Column, Integer, String
from backend.database.base import Base

# Modelo de dados para usuários
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True, unique=True)
    password = Column(String, index=True)