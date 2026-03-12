from pydantic import BaseModel

class User (BaseModel) :
    name : str
    email : str
    password : str

class CreateUser(BaseModel) :
    name : str
    email : str
    password : str

class UserLogin(BaseModel):
    email: str
    password: str


class ChatRequest(BaseModel) :
    question : str
