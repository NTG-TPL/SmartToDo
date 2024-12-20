from fastapi import FastAPI
from app.routes.todo import router as todo_router
from app.models.init_db import Base, engine
app = FastAPI()
app.include_router(todo_router)

Base.metadata.create_all(bind=engine)