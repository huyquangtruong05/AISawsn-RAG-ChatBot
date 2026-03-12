from sqlalchemy import Column, Integer, String, Text, DateTime
from .database import Base

class User(Base) : 
    __tablename__  =  "users"
    id = Column(Integer, primary_key = True, index=True)
    name = Column(String(255), nullable=False, index = True)
    email = Column(String(50), nullable=False, index=True)
    password = Column(String(50), nullable=False, index=True)
    