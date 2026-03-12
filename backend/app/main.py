from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models
from . import schemas
from . import crud
from .database import engine, get_db
from .auth import verify_password

from backend.app.schemas import User
from backend.app.schemas import ChatRequest


from backend.app.rag.rag_pipeline import rag_answer

app = FastAPI(
    title = "AISawsn Platform",
    description= "An chatbot platform for AI-based applications",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Welcome to AISawsn Platform"}

@app.post("/register")
def register(user:schemas.CreateUser, db:Session = Depends(get_db)) :
    db_user = crud.check_user_exists(db, user.email)
    if db_user :
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)


@app.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)): 
    db_user = crud.check_user_exists_for_login(db, user.email, user.password) 
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {"message": "Login successful", "user_id": db_user.id}


@app.get("/user/{user_id}", response_model=User)
def get_user(user_id : int, db: Session = Depends(get_db)) :
    user = crud.get_user(db, user_id)
    if not user :
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.post("/chat")
def send_message(message : ChatRequest) :

    question = f"Received your question: {message.question}"
    print("User question:", message.question)

    answer = rag_answer(question)

    return {"response": answer}


# uvicorn backend.app.main:app --reload