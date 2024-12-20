import logging
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Модель данных для TODO
class Todo(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False

# В памяти хранилище для TODO
todos: List[Todo] = []

# Настройка логирования
log_directory = "logs"
log_file = os.path.join(log_directory, "app.log")

# Создаем директорию для логов, если она не существует
os.makedirs(log_directory, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Welcome to the TODO List API!"}

@app.post("/todos/")
def create_todo(todo: Todo):
    logger.info(f"Creating todo: {todo}")
    todos.append(todo)
    return todo

@app.get("/todos/")
def get_todos():
    logger.info("Getting all todos")
    return todos

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    logger.info(f"Getting todo with id: {todo_id}")
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    logger.info(f"Updating todo with id: {todo_id}")
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    logger.info(f"Deleting todo with id: {todo_id}")
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return
    raise HTTPException(status_code=404, detail="Todo not found")