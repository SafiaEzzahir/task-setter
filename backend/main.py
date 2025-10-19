import uvicorn
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from datetime import date
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./tasks.db"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False} #needed for SQLite
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    desc = Column(String, nullable=False)
    days_to_complete = Column(Integer, nullable=False)
    author = Column(String, nullable=False)

Base.metadata.create_all(bind=engine)

class Task(BaseModel):
    id: int | None = None #automatically assign id
    name: str
    desc: str
    days_to_complete: int
    author: str
    date_created: date | None = None

    class Config:
        from_attributes = True  # allows returning SQLAlchemy objects directly

class Tasks(BaseModel):
    tasks: List[Task]

app = FastAPI()

origins = [
    "https://localhost:5173",
    "http://localhost:5173",
]

#add origins to allowed origins (cors)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

next_id = 1 #counter for ids

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/tasks", response_model=List[Task])
def get_tasks(db: SessionLocal = Depends(get_db)):
    tasks = db.query(TaskDB).all()
    return tasks

@app.post("/tasks", response_model=Task)
def add_task(task: Task, db: SessionLocal = Depends(get_db)):
    db_task = TaskDB(
        name=task.name,
        desc=task.desc,
        id=task.id,
        days_to_complete=task.days_to_complete,
        author=task.author,
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int, db: SessionLocal = Depends(get_db)):
    task = db.query(TaskDB).filter(TaskDB.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task id not found")
        
    db.delete(task)
    db.commit()
    return task

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)