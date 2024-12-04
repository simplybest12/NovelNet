from fastapi import FastAPI
from .core.config import settings
from typing import Optional
from .db.database import engine, Base
from .books.routers import book_router
from .core.config import settings

version = settings.project_version

def create_table():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(
        title="NovelNet",
        description="A FastAPI application for novel and book reviews",
        version = settings.project_version)
    create_table()
    return app

app = start_application()

app.include_router(book_router.router,prefix=f"/api/{version}/books",tags=["Books"])



