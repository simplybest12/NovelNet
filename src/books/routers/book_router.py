from fastapi import APIRouter,Depends,status
from ...db import database
from sqlalchemy.orm import Session
from ..services.book_service import BookService
from typing import Annotated
from ..schema import BookCreate, BookResponse
from ..models import model_book

router = APIRouter()
book_service = BookService()

@router.post("/",status_code=status.HTTP_201_CREATED)
async def create_book(book_instance: BookCreate,db: Annotated[Session, Depends(database.get_db)]):
    new_book = await book_service.create_book(db,book_instance)
    return new_book


