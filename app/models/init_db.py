from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models.todo import Base

POSTGRES_USER = getenv('POSTGRES_USER')
POSTGRES_PASSWORD = getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = getenv('POSTGRES_HOST')
POSTGRES_PORT = getenv('POSTGRES_PORT')
POSTGRES_DB = getenv('POSTGRES_DB')

DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)