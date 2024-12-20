from typing import List, Type
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models.todo import Todo as TodoModel
from app.schemas.todo import TodoCreate, TodoUpdate, Todo
from app.models.init_db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=dict[str, str])
def healthcheck() -> dict[str, str]:
    return {"message": "Welcome to the TODO List API!"}

@router.post("/todos/", response_model=Todo)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)) -> Todo:
    db_todo = TodoModel(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.get("/todos/", response_model=List[Todo])
def get_todos(db: Session = Depends(get_db)) -> list[Type[Todo]]:
    return db.query(TodoModel).all()

@router.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int, db: Session = Depends(get_db)) -> Type[Todo]:
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo

@router.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate, db: Session = Depends(get_db)) -> Type[Todo]:
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in updated_todo.model_dump(exclude_unset=True).items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return todo

@router.delete("/todos/{todo_id}", response_model=dict[str, str])
def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    todo = db.query(TodoModel).filter(TodoModel.id == todo_id).first()
    if todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted"}