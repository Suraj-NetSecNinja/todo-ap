from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# In-memory task list
tasks = []

# Define the structure of a task
class Task(BaseModel):
    id: int
    title: str
    done: bool = False

@app.get("/")
def home():
    return {"message": "Welcome to To-Do API with FastAPI!"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task.dict())
    return {"message": "Task added", "task": task}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return {"message": f"Task {task_id} deleted"}
