import uvicorn
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id: int | None = None #automatically assign id
    name: str
    desc: str
    days_to_complete: int
    author: str

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

memory_db = {"tasks": []}
next_id = 1 #counter for ids

@app.get("/tasks", response_model=Tasks)
def get_tasks():
    return Tasks(tasks=memory_db["tasks"])

@app.post("/tasks", response_model=Task)
def add_task(task: Task):
    global next_id
    task.id = next_id
    next_id += 1

    memory_db["tasks"].append(task)
    return task

@app.delete("/tasks/{task_id}", response_model=Task)
def delete_task(task_id: int):
    for i, task in enumerate(memory_db["tasks"]): #get task and index
        if task.id == task_id:
            deleted_task = memory_db["tasks"].pop(i) #removes and returns deleted task
            return deleted_task
        
    raise HTTPException(status_code=404, detail="Task id not found")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)